from datetime import datetime, timezone

from cccat import dto
from cccat.events.event_handlers import handle_cat_created

UTC = timezone.utc


def test_handle_cat_created() -> None:
    data: dto.JSON = {
        "cat_id": "000000000000000000000101",
        "partial_update_cat": {
            "name": "Sammybridge Cat",
            "ctime": datetime(2020, 1, 1, 0, 0, tzinfo=UTC),
            "mtime": datetime(2020, 1, 1, 0, 0, tzinfo=UTC),
            "url": "http://placekitten.com/200/300",
        },
    }

    handle_cat_created(data)
