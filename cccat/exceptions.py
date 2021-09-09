class CccatError(Exception):
    pass


class EventException(CccatError):
    pass


class DuplicateEntityError(CccatError):
    pass


class DuplicateCatError(DuplicateEntityError):
    pass


class EmptyResultsFilter(CccatError):
    pass


class EntityNotFoundError(CccatError):
    pass


class CatNotFoundError(EntityNotFoundError):
    pass
