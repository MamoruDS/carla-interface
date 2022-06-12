# https://github.com/carla-simulator/carla/blob/master/PythonAPI/carla/source/libcarla/Geom.cpp
from __future__ import annotations
from ._generic import vector_of
from typing import List, overload
from typing_extensions import Self


class _Vector:
    def squared_length(self) -> float:
        raise NotImplementedError

    def length(self) -> float:
        raise NotImplementedError

    def make_unit_vector(self) -> Self:
        raise NotImplementedError

    def __eq__(self, __o: Self) -> bool:
        raise NotImplementedError

    def __ne__(self, __o: Self) -> bool:
        raise NotImplementedError

    def __iadd__(self, __o: Self) -> Self:
        raise NotImplementedError

    def __add__(self, __o: Self) -> Self:
        raise NotImplementedError

    def __isub__(self, __o: Self) -> Self:
        raise NotImplementedError

    def __sub__(self, __o: Self) -> Self:
        raise NotImplementedError

    def __imul__(self, __o: float) -> Self:
        raise NotImplementedError

    def __rmul__(self, __o: float) -> Self:
        raise NotImplementedError

    def __mul__(self, __o: float) -> Self:
        raise NotImplementedError

    def __rtruediv__(self, __o: float) -> Self:
        raise NotImplementedError

    def __truediv__(self, __o: float) -> Self:
        raise NotImplementedError

    def __str__(self) -> str:
        raise NotImplementedError


class Vector2D(_Vector):
    def __init__(self, x: float = 0.0, y: float = 0.0) -> None:
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



class vector_of_vector2D(vector_of[Vector2D]):
    ...


class Vector3D(_Vector):
    @overload
    def __init__(self, x: float = 0.0, y: float = 0.0, z: float = 0.0) -> None:
        ...

    @overload
    def __init__(self, rhs: Location) -> None:
        ...

    def __init__(self, *args) -> None:  # type: ignore
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

    @property
    def z(self) -> float:
        raise NotImplementedError

    @z.setter
    def z(self, val: float) -> None:
        raise NotImplementedError


    def cross(self, vector: Vector3D) -> Vector3D:
        raise NotImplementedError

    def dot(self, vector: Vector3D) -> float:
        raise NotImplementedError

    def dot_2d(self, vector: Vector3D) -> float:
        raise NotImplementedError

    def distance(self, vector: Vector3D) -> float:
        raise NotImplementedError

    def distance_2d(self, vector: Vector3D) -> float:
        raise NotImplementedError

    def distance_squared(self, vector: Vector3D) -> float:
        raise NotImplementedError

    def distance_squared_2d(self, vector: Vector3D) -> float:
        raise NotImplementedError

    def get_vector_angle(self, vector: Vector3D) -> float:
        raise NotImplementedError

    def __abs__(self) -> Self:
        raise NotImplementedError


class Location(Vector3D):
    def distance(self, location: Location) -> float:
        raise NotImplementedError

    def __eq__(self, __o: Location) -> bool:
        raise NotImplementedError

    def __ne__(self, __o: Location) -> bool:
        raise NotImplementedError

    def __abs__(self) -> Self:
        raise NotImplementedError

    def __str__(self) -> str:
        raise NotImplementedError


class Rotation:
    def __init__(
        self, pitch: float = 0.0, yaw: float = 0.0, roll: float = 0.0
    ) -> None:
        raise NotImplementedError

    @property
    def pitch(self) -> float:
        raise NotImplementedError

    @pitch.setter
    def pitch(self, val: float) -> None:
        raise NotImplementedError

    @property
    def yaw(self) -> float:
        raise NotImplementedError

    @yaw.setter
    def yaw(self, val: float) -> None:
        raise NotImplementedError

    @property
    def roll(self) -> float:
        raise NotImplementedError

    @roll.setter
    def roll(self, val: float) -> None:
        raise NotImplementedError

    def get_forward_vector(self) -> Vector3D:
        raise NotImplementedError

    def get_right_vector(self) -> Vector3D:
        raise NotImplementedError

    def get_up_vector(self) -> Vector3D:
        raise NotImplementedError

    def __eq__(self, __o: Self) -> bool:
        raise NotImplementedError

    def __ne__(self, __o: Self) -> bool:
        raise NotImplementedError

    def __str__(self) -> str:
        raise NotImplementedError


class Transform:
    def __init__(
        self,
        location: Location = Location(),
        extent: Vector3D = Vector3D(),
        rotation: Rotation = Rotation(),
    ) -> None:
        raise NotImplementedError

    @property
    def location(self) -> Location:
        raise NotImplementedError

    @location.setter
    def location(self, val: Location) -> None:
        raise NotImplementedError

    @property
    def rotation(self) -> Rotation:
        raise NotImplementedError

    @rotation.setter
    def rotation(self, val: Rotation) -> None:
        raise NotImplementedError


    # TODO:
    # https://github.com/carla-simulator/carla/blob/master/PythonAPI/carla/source/libcarla/Geom.cpp#L236
    @overload
    def transform(self, _: List[float]) -> None:
        """
        Applies this transformation to @a in_point (first translation then rotation).
        """
        ...
    @overload
    def transform(self, in_point: Vector3D) -> Vector3D:
        """
        Applies this transformation to @a in_point (first translation then rotation).
        """
        ...
    def transform(self *args): # type: ignore
        raise NotImplementedError

    # TODO:
    # https://github.com/carla-simulator/carla/blob/master/PythonAPI/carla/source/libcarla/Geom.cpp#L240
    def transform_vector(self, in_point: Vector3D) -> Vector3D:
        raise NotImplementedError

    def get_forward_vector(self) -> Vector3D:
        raise NotImplementedError

    def get_right_vector(self) -> Vector3D:
        raise NotImplementedError

    def get_up_vector(self) -> Vector3D:
        raise NotImplementedError

    def get_matrix(self) -> List[float]:
        raise NotImplementedError

    def get_inverse_matrix(self) -> List[float]:
        raise NotImplementedError

    def __eq__(self, __o: Self) -> bool:
        raise NotImplementedError

    def __ne__(self, __o: Self) -> bool:
        raise NotImplementedError

    def __str__(self) -> str:
        raise NotImplementedError


class vector_of_transform(vector_of[Transform]):
    ...


class BoundingBox:
    def __init__(
        self,
        location: Location = Location(),
        extent: Vector3D = Vector3D(),
        rotation: Rotation = Rotation(),
    ) -> None:
        raise NotImplementedError

    @property
    def location(self) -> Location:
        raise NotImplementedError

    @location.setter
    def location(self, val: Location) -> None:
        raise NotImplementedError

    @property
    def extent(self) -> Vector3D:
        raise NotImplementedError

    @extent.setter
    def extent(self, val: Vector3D) -> None:
        raise NotImplementedError

    @property
    def rotation(self) -> Rotation:
        raise NotImplementedError

    @rotation.setter
    def rotation(self, val: Rotation) -> None:
        raise NotImplementedError


    def contains(self, point: Location, bbox_transform: Transform) -> bool:
        raise NotImplementedError

    def get_local_vertices(self) -> List[Location]:
        """
        Returns the positions of the 8 vertices of this BoundingBox in local space.
        """
        raise NotImplementedError

    def get_world_vertices(self, bbox_transform: Transform) -> List[Location]:
        """
        Returns the positions of the 8 vertices of this BoundingBox in world space.
        """
        raise NotImplementedError

    def __eq__(self, __o: Self) -> bool:
        raise NotImplementedError

    def __ne__(self, __o: Self) -> bool:
        raise NotImplementedError

    def __str__(self) -> str:
        raise NotImplementedError


class GeoLocation:
    def __init__(
        self,
        latitude: float = 0.0,
        longitude: float = 0.0,
        altitude: float = 0.0,
    ) -> None:
        raise NotImplementedError

    @property
    def latitude(self) -> float:
        raise NotImplementedError

    @latitude.setter
    def latitude(self, val: float) -> None:
        raise NotImplementedError

    @property
    def longitude(self) -> float:
        raise NotImplementedError

    @longitude.setter
    def longitude(self, val: float) -> None:
        raise NotImplementedError

    @property
    def altitude(self) -> float:
        raise NotImplementedError

    @altitude.setter
    def altitude(self, val: float) -> None:
        raise NotImplementedError

    def __eq__(self, __o: Self) -> bool:
        raise NotImplementedError

    def __ne__(self, __o: Self) -> bool:
        raise NotImplementedError

    def __str__(self) -> str:
        raise NotImplementedError
