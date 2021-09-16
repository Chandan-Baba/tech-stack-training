import asyncio
import logging
from typing import Callable, Mapping

from cccat import dto
from cccat.domains import cat_domain
from cccat.exceptions import EventException

logger = logging.getLogger(__name__)


def handle_ping(data: dto.JSON) -> None:
    """
    All consumers listen to `ping` event.

    Event payload schema is:

    {
        "event_id": <event correlation id>
    }
    """
    event_id = data.get("event_id")

    logger.info(f"[{event_id}] pong")


def handle_cat_created(data: dto.JSON) -> None:
    event_id = data.get("event_id")
    cat_id = data.get("cat_id")
    partial_update_cat = data.get("partial_update_cat")
    required_keys = {"cat_id", "partial_update_cat"}

    if not all(key in data for key in required_keys):
        exception_message = (
            f"Cannot process event: missing required keys. "
            f"Got: {', '.join(data.keys())}. Expected: {', '.join(required_keys)}"
        )
        logger.exception(f"[{event_id}] {exception_message}")
        raise EventException(exception_message)

    logger.info(f"[{event_id}] Cat {cat_id} has been created")
    # TODO: Handle the async postprocessing of a created Cat here.

    dto_cat_id = dto.CatID(str(cat_id))

    # partial_update = dto.PartialUpdateCat(url="http://placekitten.com/200/300")

    try:
        partial_update = dto.PartialUpdateCat.parse_obj(partial_update_cat)
    except ValueError:
        exception_message = (
            f"Cannot process event: invalid partial update. Got: {partial_update_cat}"
        )
        logger.exception(f"[{event_id}] {exception_message}")
        raise EventException(exception_message)

    loop = asyncio.get_event_loop()
    coroutine = cat_domain.partial_update_cat_metadata(
        cat_id=dto_cat_id, partial_update=partial_update
    )
    loop.run_until_complete(coroutine)


EVENT_HANDLERS: Mapping[str, Callable] = {
    "ping": handle_ping,
    "cccat-ping": handle_ping,
    "cat.created": handle_cat_created,
}
