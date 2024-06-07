# https://github.com/carla-simulator/carla/blob/master/PythonAPI/carla/source/libcarla/Snapshot.cpp
from __future__ import annotations
from ._c.rpc import ActorId
from .geom import Transform, Vector3D
from .world import Timestamp
from typing import Optional
from typing_extensions import Self


class ActorSnapshot:
    @property
    def id(self) -> int:
        raise NotImplementedError

    def get_transform(self) -> Transform:
        raise NotImplementedError

    def get_velocity(self) -> Vector3D:
        raise NotImplementedError

    def get_angular_velocity(self) -> Vector3D:
        raise NotImplementedError

    def get_acceleration(self) -> Vector3D:
        raise NotImplementedError

    def __str__(self) -> str:
        raise NotImplementedError


class WorldSnapshot:
    @property
    def id(self) -> int:
        raise NotImplementedError

    @property
    def frame(self) -> int:
        raise NotImplementedError

    @property
    def timestamp(self) -> Timestamp:
        raise NotImplementedError

    @property
    def frame_count(self) -> int:
        """deprecated; using `WorldSnapshot.timestamp`"""
        raise NotImplementedError

    @property
    def elapsed_seconds(self) -> float:
        """deprecated; using `WorldSnapshot.timestamp`"""
        raise NotImplementedError

    @property
    def delta_seconds(self) -> float:
        """deprecated; using `WorldSnapshot.timestamp`"""
        raise NotImplementedError

    @property
    def platform_timestamp(self) -> float:
        """deprecated; using `WorldSnapshot.timestamp`"""
        raise NotImplementedError

    def has_actor(self, actor_id: ActorId) -> bool:
        raise NotImplementedError

    def find(self, actor_id: ActorId) -> Optional[ActorSnapshot]:
        raise NotImplementedError

    def __len__(self) -> int:
        raise NotImplementedError

    def __iter__(self) -> Self:
        raise NotImplementedError

    def __next__(self) -> ActorSnapshot:  # TODO: verify
        raise NotImplementedError

    def __eq__(self, __o: Self) -> bool:
        raise NotImplementedError

    def __ne__(self, __o: Self) -> bool:
        raise NotImplementedError

    def __str__(self) -> str:
        raise NotImplementedError
