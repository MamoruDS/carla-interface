from typing import Generic, Iterable, TypeVar
T = TypeVar('T')

class vector_of(Generic[T]):
    def extend(self, _: Iterable[T]) -> None:
        raise NotImplementedError

    def append(self, _: int) -> None:
        raise NotImplementedError

    def __str__(self) -> str:
        raise NotImplementedError
