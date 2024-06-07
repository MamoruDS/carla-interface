# https://github.com/carla-simulator/carla/blob/master/PythonAPI/carla/source/libcarla/LightManager.cpp
from ._c.rpc import LightId
from ._c.sensor.data import Color
from .geom import Location
from enum import IntEnum
from typing import List


class LightGroup(IntEnum):
    NONE = 0
    Vehicle = 1
    Street = 2
    Building = 3
    Other = 4


class LightState:
    _location: Location

    def __init__(
        self,
        intensity: float = 0.0,
        color=Color(),
        group: LightGroup = LightGroup.NONE,
    ) -> None:
        raise NotImplementedError

    @property
    def intensity(self) -> float:
        raise NotImplementedError

    @intensity.setter
    def intensity(self, val: float) -> None:
        raise NotImplementedError

    @property
    def color(self) -> Color:
        raise NotImplementedError

    @color.setter
    def color(self, val: Color) -> None:
        raise NotImplementedError

    @property
    def group(self) -> LightGroup:
        raise NotImplementedError

    @group.setter
    def group(self, val: LightGroup) -> None:
        raise NotImplementedError

    @property
    def active(self) -> bool:
        raise NotImplementedError

    @active.setter
    def active(self, val: bool) -> None:
        raise NotImplementedError


class Light:
    @property
    def color(self) -> Color:
        raise NotImplementedError

    @property
    def id(self) -> LightId:
        raise NotImplementedError

    @property
    def intensity(self) -> float:
        raise NotImplementedError

    @property
    def is_on(self) -> bool:
        raise NotImplementedError

    @property
    def location(self) -> Location:
        raise NotImplementedError

    @property
    def light_group(self) -> LightGroup:
        raise NotImplementedError

    @property
    def light_state(self) -> LightState:
        raise NotImplementedError

    def set_color(self, color: Color) -> None:
        raise NotImplementedError

    def set_intensity(self, intensity: float) -> None:
        raise NotImplementedError

    def set_light_group(self, light_group: LightGroup) -> None:
        raise NotImplementedError

    def set_light_state(self, light_state: LightState) -> None:
        raise NotImplementedError

    def turn_on(self) -> None:
        raise NotImplementedError

    def turn_off(self) -> None:
        raise NotImplementedError


class LightManager:
    def get_all_lights(self, light_group: LightGroup = LightGroup.NONE) -> List[Light]:
        raise NotImplementedError

    def turn_on(self, lights: List[Light]) -> None:
        raise NotImplementedError

    def turn_off(self, lights: List[Light]) -> None:
        raise NotImplementedError

    def set_active(self, lights: List[Light], active: List[bool]) -> None:
        raise NotImplementedError

    def is_active(self, lights: List[Light]) -> List[bool]:
        raise NotImplementedError

    def get_turned_on_lights(
        self, light_group: LightGroup = LightGroup.NONE
    ) -> List[Light]:
        raise NotImplementedError

    def get_turned_off_lights(
        self, light_group: LightGroup = LightGroup.NONE
    ) -> List[Light]:
        raise NotImplementedError

    def set_color(self, lights: List[Light], color: Color) -> None:
        raise NotImplementedError

    def set_colors(self, lights: List[Light], colors: List[Color]) -> None:
        raise NotImplementedError

    def get_color(self, lights: List[Light]) -> List[Color]:
        raise NotImplementedError

    def set_intensity(self, lights: List[Light], intensity: float) -> None:
        raise NotImplementedError

    def set_intensities(self, lights: List[Light], intensities: List[float]) -> None:
        raise NotImplementedError

    def get_intensity(self, lights: List[Light]) -> List[float]:
        raise NotImplementedError

    def set_light_group(self, lights: List[Light], light_group: LightGroup) -> None:
        raise NotImplementedError

    def set_light_groups(
        self, lights: List[Light], light_groups: List[LightGroup]
    ) -> None:
        raise NotImplementedError

    def get_light_group(self, lights: List[Light]) -> List[LightGroup]:
        raise NotImplementedError

    def set_light_state(self, lights: List[Light], light_state: LightState) -> None:
        raise NotImplementedError

    def set_light_states(
        self, lights: List[Light], light_states: List[LightState]
    ) -> None:
        raise NotImplementedError

    def get_light_state(self, lights: List[Light]) -> List[LightState]:
        raise NotImplementedError
