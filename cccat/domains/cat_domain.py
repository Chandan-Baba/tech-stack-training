import logging
from typing import Optional

from cccat import dto
from cccat.libs import dates
from cccat.models import cat_model

# from cccat.models.common import get_collection

logger = logging.getLogger(__name__)

_COLLECTION_NAME = "cats"


async def create_cat(new_cat: dto.UnsavedCat) -> dto.Cat:
    now = dates.get_utcnow()
    return await cat_model.create_cat(new_cat, now=now)


async def find_one(cat_filter: dto.CatFilter) -> Optional[dto.Cat]:
    return await cat_model.find_one(cat_filter=cat_filter)


async def find_many(
    cat_filter: Optional[dto.CatFilter] = None,
    cat_sort_params: Optional[dto.CatSortPredicates] = None,
    page: Optional[dto.Page] = None,
) -> dto.PagedResult[dto.CatSummary]:
    results = await cat_model.find_many(
        cat_filter=cat_filter,
        cat_sort_params=cat_sort_params,
        page=page,
    )
    return results


async def partial_update_cat_metadata(
    cat_id: dto.CatID, partial_update: dto.PartialUpdateCat
) -> dto.BulkUpdateResult:
    result = await cat_model.partial_update_cat_metadata(
        cat_id=cat_id,
        partial_update=partial_update,
    )
    return result
