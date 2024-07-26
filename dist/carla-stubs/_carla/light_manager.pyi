from .blueprint import Color
from .geom import Location
from enum import IntEnum, auto

class Light:
    """
    This class exposes the lights that exist in the scene, except for vehicle lights. The properties of a light can be queried and changed at will.
    Lights are automatically turned on when the simulator enters night mode (sun altitude is below zero).
    """
    def set_color(self, color: Color):
        """
        Changes the color of the light to `color`.
        """
    def set_intensity(self, intensity: float):
        """
        Changes the intensity of the light to `intensity`.
        """
    def set_light_group(self, light_group: LightGroup):
        """
        Changes the light to the group `light_group`.
        """
    def set_light_state(self, light_state: LightState):
        """
        Changes the state of the light to `light_state`. This may change attributes, group and turn the light on/off all at once.
        """
    def turn_off(self):
        """
        Switches off the light.
        """
    def turn_on(self):
        """
        Switches on the light.
        """
    @property
    def color(self) -> Color:
        """
        Color of the light.
        """
    @property
    def id(self) -> int:
        """
        Identifier of the light.
        """
    @property
    def intensity(self) -> float:
        """
        Intensity of the light.
        """
    @property
    def is_on(self) -> bool:
        """
        Switch of the light. It is __True__ when the light is on. When the night mode starts, this is set to __True__.
        """
    @property
    def light_group(self) -> LightGroup:
        """
        Group the light belongs to.
        """
    @property
    def light_state(self) -> LightState:
        """
        State of the light. Summarizes its attributes, group, and if it is on/off.
        """
    @property
    def location(self) -> Location:
        """
        Position of the light.
        """

class LightGroup(IntEnum):
    """
    This class categorizes the lights on scene into different groups. These groups available are provided as a enum values that can be used as flags.

    __Note.__ So far, though there is a `vehicle` group, vehicle lights are not available as carla.Light objects. These have to be managed using carla.Vehicle and carla.VehicleLightState.
    """

    Building = auto()
    NONE = auto()
    Other = auto()
    Street = auto()
    Vehicle = auto()

class LightManager:
    """
    This class handles the lights in the scene. Its main use is to get and set the state of groups or lists of lights in one call. An instance of this class can be retrieved by the carla.World.get_lightmanager().

    __Note.__ So far, though there is a `vehicle` group, vehicle lights are not available as carla.Light objects. These have to be managed using carla.Vehicle and carla.VehicleLightState.
    """
    def get_all_lights(self, light_group: LightGroup) -> list[Light]:
        """
        Returns a list containing the lights in a certain group. By default, the group is `None`.
        """
    def get_color(self, lights: list[Light]) -> list[Color]:
        """
        Returns a list with the colors of every element in `lights`.
        """
    def get_intensity(self, lights: list[Light]) -> list[float]:
        """
        Returns a list with the intensity of every element in `lights`.
        """
    def get_light_group(self, lights: list[Light]) -> list[LightGroup]:
        """
        Returns a list with the group of every element in `lights`.
        """
    def get_light_state(self, lights: list[Light]) -> list[LightState]:
        """
        Returns a list with the state of all the attributes of every element in `lights`.
        """
    def get_turned_off_lights(self, light_group: LightGroup) -> list[Light]:
        """
        Returns a list containing lights switched off in the scene, filtered by group.
        """
    def get_turned_on_lights(self, light_group: LightGroup) -> list[Light]:
        """
        Returns a list containing lights switched on in the scene, filtered by group.
        """
    def is_active(self, lights: list[Light]) -> list[bool]:
        """
        Returns a list with booleans stating if the elements in `lights` are switched on/off.
        """
    def set_active(self, lights: list[Light], active: list[bool]):
        """
        Switches on/off the elements in `lights`.
        """
    def set_color(self, lights: list[Light], color: Color):
        """
        Changes the color of the elements in `lights` to `color`.
        """
    def set_colors(self, lights: list[Light], colors: list[Color]):
        """
        Changes the color of each element in `lights` to the corresponding in `colors`.
        """
    def set_day_night_cycle(self, active: bool):
        """
        All scene lights have a day-night cycle, automatically turning on and off with the altitude of the sun. This interferes in cases where full control of the scene lights is required, so setting this to __False__ deactivates it. It can reactivated by setting it to __True__.
        """
    def set_intensities(self, lights: list[Light], intensities: list[float]):
        """
        Changes the intensity of each element in `lights` to the corresponding in `intensities`.
        """
    def set_intensity(self, lights: list[Light], intensity: float):
        """
        Changes the intensity of every element in `lights` to `intensity`.
        """
    def set_light_group(self, lights: list[Light], light_group: LightGroup):
        """
        Changes the group of every element in `lights` to `light_group`.
        """
    def set_light_groups(self, lights: list[Light], light_groups: list[LightGroup]):
        """
        Changes the group of each element in `lights` to the corresponding in `light_groups`.
        """
    def set_light_state(self, lights: list[Light], light_state: LightState):
        """
        Changes the state of the attributes of every element in `lights` to `light_state`.
        """
    def set_light_states(self, lights: list[Light], light_states: list[LightState]):
        """
        Changes the state of the attributes of each element in `lights` to the corresponding in `light_states`.
        """
    def turn_off(self, lights: list[Light]):
        """
        Switches off all the lights in `lights`.
        """
    def turn_on(self, lights: list[Light]):
        """
        Switches on all the lights in `lights`.
        """

class LightState:
    """
    This class represents all the light variables except the identifier and the location, which are should to be static. Using this class allows to manage all the parametrization of the light in one call.
    """
    def __init__(
        self, intensity: float, color: Color, group: LightGroup, active: bool
    ): ...
    @property
    def active(self) -> bool:
        """
        Switch of a light. It is __True__ when the light is on.
        """
    @property
    def color(self) -> Color:
        """
        Color of a light.
        """
    @property
    def group(self) -> LightGroup:
        """
        Group a light belongs to.
        """
    @property
    def intensity(self) -> float:
        """
        Intensity of a light.
        """
