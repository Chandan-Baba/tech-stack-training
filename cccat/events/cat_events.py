from bson.json_util import dumps

from cccat import dto
from cccat.events import common
from cccat.models.common import BSONDocument


def fire_cat_created(cat_id: str) -> None:
    """
    Fired after a new Cat has been created, so that this
    service can do some background post-processing and so that other services can subscribe to
    info on new Cats.
    """
    common.fire_event("cat.created", {"cat_id": cat_id})


def fire_handle_cat_created(created_cat_id: str, partial_update_cat: str) -> None:
    print("here", partial_update_cat)
    common.fire_event(
        "cat.handle_cat_created",
        {"cat_id": created_cat_id, "partial_update_cat": partial_update_cat.url},
    )
