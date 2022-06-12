# https://github.com/carla-simulator/carla/blob/master/PythonAPI/carla/source/libcarla/Blueprint.cpp
from enum import IntEnum
from typing import Generic, List, TypeVar, Union
from typing_extensions import Self


# https://github.com/carla-simulator/carla/blob/master/LibCarla/source/carla/rpc/ActorAttributeType.h
class ActorAttributeType(IntEnum):
    Bool = 0
    Int = 1
    Float = 2
    String = 3
    RGBColor = 4


_C = TypeVar("_C", bound=Union[int, float])


class _Color(Generic[_C]):
    def __init__(self, r: _C, g: _C, b: _C, a: _C = 255) -> None:
        pass

    @property
    def r(self) -> _C:
        raise NotImplementedError

    @r.setter
    def r(self, val: _C) -> None:
        raise NotImplementedError

    @property
    def g(self) -> _C:
        raise NotImplementedError

    @g.setter
    def g(self, val: _C) -> None:
        raise NotImplementedError

    @property
    def b(self) -> _C:
        raise NotImplementedError

    @b.setter
    def b(self, val: _C) -> None:
        raise NotImplementedError

    @property
    def a(self) -> _C:
        raise NotImplementedError

    @a.setter
    def a(self, val: _C) -> None:
        raise NotImplementedError

    def __eq__(self, __o: Self) -> bool:
        raise NotImplementedError

    def __ne__(self, __o: Self) -> bool:
        raise NotImplementedError


class Color(_Color[int]):
    def __str__(self) -> str:
        raise NotImplementedError


class FloatColor(_Color[float]):
    ...


class OpticalFlowPixel:
    def __init__(self, x: float = 0, y: float = 0) -> None:
        raise NotImplementedError

    @property
    def x(self) -> float:
        raise NotImplementedError

    @x.setter
    def x(self, val: float) -> None:
        raise NotImplementedError

    @property
    def y(self) -> float:
        raise NotImplementedError

    @y.setter
    def y(self, val: float) -> None:
        raise NotImplementedError

    def __eq__(self, __o: Self) -> bool:
        raise NotImplementedError

    def __ne__(self, __o: Self) -> bool:
        raise NotImplementedError

    def __str__(self) -> str:
        raise NotImplementedError


class ActorAttribute:
    @property
    def id(self) -> str:
        raise NotImplementedError

    @property
    def type(self) -> ActorAttributeType:
        raise NotImplementedError

    @property
    def recommended_values(self) -> List[str]:
        raise NotImplementedError

    @property
    def is_modifiable(self) -> bool:
        raise NotImplementedError

    def as_bool(self) -> bool:
        raise NotImplementedError

    def as_int(self) -> int:
        raise NotImplementedError

    def as_float(self) -> float:
        raise NotImplementedError

    def as_str(self) -> str:
        raise NotImplementedError

    def as_color(self) -> Color:
        raise NotImplementedError

    def __eq__(self, __o: Union[bool, int, float, str, Color, Self]) -> bool:
        raise NotImplementedError

    def __ne__(self, __o: Union[bool, int, float, str, Color, Self]) -> bool:
        raise NotImplementedError

    def __nonzero__(self) -> bool:
        raise NotImplementedError

    def __bool__(self) -> bool:
        raise NotImplementedError

    def __int__(self) -> int:
        raise NotImplementedError

    def __float__(self) -> float:
        raise NotImplementedError

    def __str__(self) -> str:
        raise NotImplementedError


class ActorBlueprint:
    @property
    def id(self) -> str:
        raise NotImplementedError

    @property
    def tags(self) -> List[str]:
        raise NotImplementedError

    def has_tag(self, _tag: str) -> bool:
        raise NotImplementedError

    def match_tags(self, _wildcard_pattern: str) -> bool:
        raise NotImplementedError

    def has_attribute(self, _id: str) -> bool:
        raise NotImplementedError

    def get_attribute(self, id: str) -> ActorAttribute:
        """
        @throw std::out_of_range if no such element exists.
        """
        raise NotImplementedError

    def set_attribute(self, id: str, value: str) -> None:
        """
        Set the value of the attribute given by @a id.

        @throw std::out_of_range if no such element exists.
        @throw InvalidAttributeValue if attribute is not modifiable.
        @throw InvalidAttributeValue if format does not match the attribute type.
        """
        raise NotImplementedError

    def __len__(self) -> int:
        raise NotImplementedError

    def __iter__(self) -> Self:
        raise NotImplementedError

    def __next__(self) -> ActorAttribute:  # FIXME
        raise NotImplementedError

    def __str__(self) -> str:
        raise NotImplementedError


class BlueprintLibrary:
    def find(self, id: str) -> ActorBlueprint:
        raise NotImplementedError

    def filter(self, wildcard_pattern: str) -> List[ActorBlueprint]:
        """
        Filters a list of ActorBlueprint with id or tags matching
        @a wildcard_pattern.
        """
        raise NotImplementedError

    def __getitem__(self, i: int) -> ActorBlueprint:
        raise NotImplementedError

    def __len__(self) -> int:
        raise NotImplementedError

    def __iter__(self) -> Self:
        raise NotImplementedError

    def __next__(self) -> ActorBlueprint:  # FIXME
        raise NotImplementedError

    def __str__(self) -> str:
        raise NotImplementedError


bl = BlueprintLibrary()

for i in bl:
    print(i)
