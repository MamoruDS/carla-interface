# https://github.com/carla-simulator/carla/blob/master/PythonAPI/carla/source/libcarla/World.cpp
from __future__ import annotations
from ._c.road import JuncId, SignId
from ._c.rpc import ActorId
from .actor import Actor, VehicleLightState
from .blueprint import (
    ActorBlueprint,
    BlueprintLibrary,
    Color,
    FloatColor,
)
from .geom import (
    BoundingBox,
    Location,
    Rotation,
    Transform,
    Vector3D,
)
from .light_manager import LightManager
from .map import LandMark, Map, WayPoint
from .snapshot import WorldSnapshot
from .weather import WeatherParameters
from enum import IntEnum
from typing import Callable, Generic, List, Optional, TypeVar, Union, overload
from typing_extensions import Self


class Timestamp:
    def __init__(
        self,
        frame: int = 0,
        elapsed_seconds: float = 0.0,
        delta_seconds: float = 0.0,
        platform_timestamp: float = 0.0,
    ) -> None:
        raise NotImplementedError

    @property
    def frame(self) -> int:
        raise NotImplementedError

    @frame.setter
    def frame(self, val: int) -> None:
        raise NotImplementedError

    @property
    def frame_count(self) -> int:
        raise NotImplementedError

    @frame_count.setter
    def frame_count(self, val: int) -> None:
        raise NotImplementedError

    @property
    def elapsed_seconds(self) -> float:
        raise NotImplementedError

    @elapsed_seconds.setter
    def elapsed_seconds(self, val: float) -> None:
        raise NotImplementedError

    @property
    def delta_seconds(self) -> float:
        raise NotImplementedError

    @delta_seconds.setter
    def delta_seconds(self, val: float) -> None:
        raise NotImplementedError

    @property
    def platform_timestamp(self) -> float:
        raise NotImplementedError

    @platform_timestamp.setter
    def platform_timestamp(self, val: float) -> None:
        raise NotImplementedError

    def __eq__(self, __o: Self) -> bool:
        raise NotImplementedError

    def __ne__(self, __o: Self) -> bool:
        raise NotImplementedError

    def __str__(self) -> str:
        raise NotImplementedError


# https://github.com/carla-simulator/carla/blob/master/LibCarla/source/carla/client/ActorList.h
class ActorList:
    def find(self, actor_id: ActorId) -> Actor:
        raise NotImplementedError

    def filter(self, wildcard_pattern: str) -> ActorList:
        raise NotImplementedError

    def __getitem__(self, i: int) -> Actor:
        raise NotImplementedError

    def __len__(self) -> int:
        raise NotImplementedError

    def __str__(self) -> str:
        raise NotImplementedError


class WorldSettings:
    def __init__(
        self,
        synchronous_mode: bool = False,
        no_rendering_mode: bool = False,
        fixed_delta_seconds: float = 0.0,
        substepping: bool = True,
        max_substep_delta_time: float = 0.01,
        max_substeps: int = 10,
        max_culling_distance: float = 0.0,
        deterministic_ragdolls: bool = False,
        tile_stream_distance: float = 3000.0,
        actor_active_distance: float = 2000.0,
    ) -> None:
        raise NotImplementedError

    @property
    def synchronous_mode(self) -> bool:
        raise NotImplementedError

    @synchronous_mode.setter
    def synchronous_mode(self, val: bool) -> None:
        raise NotImplementedError

    @property
    def no_rendering_mode(self) -> bool:
        raise NotImplementedError

    @no_rendering_mode.setter
    def no_rendering_mode(self, val: bool) -> None:
        raise NotImplementedError

    @property
    def substepping(self) -> bool:
        raise NotImplementedError

    @substepping.setter
    def substepping(self, val: bool) -> None:
        raise NotImplementedError

    @property
    def max_substep_delta_time(self) -> float:
        raise NotImplementedError

    @max_substep_delta_time.setter
    def max_substep_delta_time(self, val: float) -> None:
        raise NotImplementedError

    @property
    def max_substeps(self) -> int:
        raise NotImplementedError

    @max_substeps.setter
    def max_substeps(self, val: int) -> None:
        raise NotImplementedError

    @property
    def max_culling_distance(self) -> float:
        raise NotImplementedError

    @max_culling_distance.setter
    def max_culling_distance(self, val: float) -> None:
        raise NotImplementedError

    @property
    def deterministic_ragdolls(self) -> bool:
        raise NotImplementedError

    @deterministic_ragdolls.setter
    def deterministic_ragdolls(self, val: bool) -> None:
        raise NotImplementedError

    @property
    def fixed_delta_seconds(self) -> float:
        raise NotImplementedError

    @property
    def tile_stream_distance(self) -> float:
        raise NotImplementedError

    @tile_stream_distance.setter
    def tile_stream_distance(self, val: float) -> None:
        raise NotImplementedError

    @property
    def actor_active_distance(self) -> float:
        raise NotImplementedError

    @actor_active_distance.setter
    def actor_active_distance(self, val: float) -> None:
        raise NotImplementedError

    def __eq__(self, __o: Self) -> bool:
        raise NotImplementedError

    def __ne__(self, __o: Self) -> bool:
        raise NotImplementedError

    def __str__(self) -> str:
        raise NotImplementedError


# https://github.com/carla-simulator/carla/blob/master/LibCarla/source/carla/rpc/AttachmentType.h
class AttachmentType(IntEnum):
    Rigid = 0
    SpringArm = 1


# https://github.com/carla-simulator/carla/blob/master/LibCarla/source/carla/rpc/ObjectLabel.h#L16
class CityObjectLabel(IntEnum):
    NONE = 0
    Buildings = 1
    Fences = 2
    Other = 3
    Pedestrians = 4
    Poles = 5
    RoadLines = 6
    Roads = 7
    Sidewalks = 8
    Vegetation = 9
    Vehicles = 10
    Walls = 11
    TrafficSigns = 12
    Sky = 13
    Ground = 14
    Bridge = 15
    RailTrack = 16
    GuardRail = 17
    TrafficLight = 18
    Static = 19
    Dynamic = 20
    Water = 21
    Terrain = 22
    Any = 0xFF


# https://github.com/carla-simulator/carla/blob/master/LibCarla/source/carla/rpc/EnvironmentObject.h
class EnvironmentObject:
    transform: Transform
    bounding_box: BoundingBox
    id: int = 0
    name: str
    type: CityObjectLabel = CityObjectLabel.NONE


_CT = TypeVar("_CT", bound=Union[Color, FloatColor])


class _TextureColor(Generic[_CT]):
    def __init__(self, w: int, h: int) -> None:
        pass

    @property
    def width(self) -> int:
        raise NotImplementedError

    @property
    def height(self) -> int:
        raise NotImplementedError

    def set_dimensions(self, width: int, height: int) -> None:
        raise NotImplementedError

    def get(self, x: int, y: int) -> _CT:
        raise NotImplementedError

    # TODO: will FloatColor be valid?
    def set(self, x: int, y: int, value: _CT) -> None:
        raise NotImplementedError


class TextureColor(_TextureColor[Color]):
    pass


class TextureFloatColor(_TextureColor[FloatColor]):
    pass


# https://github.com/carla-simulator/carla/blob/master/LibCarla/source/carla/rpc/LabelledPoint.h
class LabelledPoint:
    @property
    def label(self) -> CityObjectLabel:
        raise NotImplementedError

    @property
    def location(self) -> Location:
        raise NotImplementedError


# https://github.com/carla-simulator/carla/blob/master/LibCarla/source/carla/rpc/MapLayer.h
class MapLayer(IntEnum):
    NONE = 0
    Buildings = 0x1
    Decals = 0x1 << 1
    Foliage = 0x1 << 2
    Ground = 0x1 << 3
    ParkedVehicles = 0x1 << 4
    Particles = 0x1 << 5
    Props = 0x1 << 6
    StreetLights = 0x1 << 7
    Walls = 0x1 << 8
    All = 0xFFFF


class MaterialParameter(IntEnum):
    Normal = 0
    AO_Roughness_Metallic_Emissive = 1
    Diffuse = 2
    Emissive = 3


class World:
    id: int
    debug: DebugHelper

    def load_map_layer(self, map_layers: MapLayer) -> None:
        raise NotImplementedError

    def unload_map_layer(self, map_layers: MapLayer) -> None:
        raise NotImplementedError

    def get_blueprint_library(self) -> BlueprintLibrary:
        """
        Return the list of blueprints available in this world. This blueprints
        can be used to spawning actor into the world.
        """
        raise NotImplementedError

    def get_vehicles_light_states(self) -> VehicleLightState:
        """
        Returns a list of pairs where the firts element is the vehicle ID
        and the second one is the light state
        """
        raise NotImplementedError

    def get_map(self) -> Map:
        raise NotImplementedError

    def get_random_location_from_navigation(self) -> Optional[Location]:
        """
        Get a random location from the pedestrians navigation mesh
        """
        raise NotImplementedError

    def get_spectator(self) -> Actor:
        """
        Return the spectator actor. The spectator controls the view in the
        simulator window.
        """
        raise NotImplementedError

    def get_settings(self) -> WorldSettings:
        raise NotImplementedError

    def apply_settings(self, settings: WorldSettings, seconds: float = 0.0) -> int:
        """
        Return The id of the frame when the settings were applied.
        """
        raise NotImplementedError

    def get_weather(self) -> WeatherParameters:
        """
        Retrieve the weather parameters currently active in the world.
        """
        raise NotImplementedError

    def set_weather(self, weather: WeatherParameters) -> None:
        """
        Change the weather in the simulation.
        """
        raise NotImplementedError

    def get_snapshot(self) -> WorldSnapshot:
        """
        Return a snapshot of the world at this moment.
        """
        raise NotImplementedError

    def get_actor(self, actor_id: ActorId) -> Optional[Actor]:
        """
        Find actor by id, return nullptr if not found.
        """
        raise NotImplementedError

    @overload
    def get_actors(self) -> ActorList:
        """
        Return a list with all the actors currently present in the world
        """
        ...

    @overload
    def get_actors(self, actor_ids: List[ActorId]) -> ActorList:
        """
        Return a list with the actors requested by ActorId.
        """
        ...

    def get_actors(self, actor_ids: Optional[List[ActorId]] = None) -> ActorList:
        raise NotImplementedError

    def spawn_actor(
        self,
        blurprint: ActorBlueprint,
        transform: Transform,
        attach_to: Optional[Actor] = None,
        attachment_type: AttachmentType = AttachmentType.Rigid,
    ) -> Actor:
        """
        Spawn an actor into the world based on the @a blueprint provided at @a
        transform. If a @a parent is provided, the actor is attached to @a parent.
        """
        raise NotImplementedError

    def try_spawn_actor(
        self,
        blurprint: ActorBlueprint,
        transform: Transform,
        attach_to: Optional[Actor] = None,
        attachment_type: AttachmentType = AttachmentType.Rigid,
    ) -> Optional[Actor]:
        """
        Same as SpawnActor but return nullptr on failure instead of throwing an
        exception.
        """
        raise NotImplementedError

    def wait_for_tick(self, seconds: float = 0.0) -> WorldSnapshot:
        """
        Block calling thread until a world tick is received.
        """
        raise NotImplementedError

    def on_tick(self, callback: Callable) -> int:  # TODO: Callable[?,?]
        """
        Register a @a callback to be called every time a world tick is received.
        Return ID of the callback, use it to remove the callback.
        """
        raise NotImplementedError

    def remove_on_tick(self, callback_id: int) -> None:
        """
        Remove a callback registered with OnTick.
        """
        raise NotImplementedError

    def tick(self, seconds: float = 0.0) -> int:
        """
        Signal the simulator to continue to next tick (only has effect on
        synchronous mode).
        Return The id of the frame that this call started.
        """
        raise NotImplementedError

    def set_pedestrians_cross_factor(self, percentage: float) -> None:
        """
        set the probability that an agent could cross the roads in its path following\n
        percentage of 0.0f means no pedestrian can cross roads\n
        percentage of 0.5f means 50% of all pedestrians can cross roads\n
        percentage of 1.0f means all pedestrians can cross roads if needed
        """
        raise NotImplementedError

    def set_pedestrians_seed(self, seed: int) -> None:
        """
        set the seed to use with random numbers in the pedestrians module
        """
        raise NotImplementedError

    def get_traffic_sign(self, landmark: LandMark) -> Actor:  # TODO: ?
        raise NotImplementedError

    def get_traffic_light(self, landmark: LandMark) -> Actor:
        raise NotImplementedError

    def gettraffic_light_from_opendrive_id(self, trafficlight_id: SignId) -> Actor:
        raise NotImplementedError

    def get_traffic_lights_from_waypoint(
        self, waypoint: WayPoint, distance: float
    ) -> List[Actor]:
        raise NotImplementedError

    def get_traffic_lights_in_junction(self, junction_id: JuncId) -> List[Actor]:
        raise NotImplementedError

    def reset_all_traffic_lights(self) -> None:
        raise NotImplementedError

    def get_lightmanager(self) -> LightManager:
        raise NotImplementedError

    def freeze_all_traffic_lights(self, frozen: bool) -> None:
        raise NotImplementedError

    def get_level_bbs(
        self, bb_type: CityObjectLabel = CityObjectLabel.Any
    ) -> List[BoundingBox]:
        """
        Returns all the BBs of all the elements of the level
        """
        raise NotImplementedError

    def get_environment_objects(
        self, object_type: CityObjectLabel = CityObjectLabel.Any
    ) -> List[EnvironmentObject]:
        raise NotImplementedError

    def enable_environment_objects(
        self, envobjects_ids: List[int], enable: bool
    ) -> None:
        raise NotImplementedError

    def cast_ray(
        self, initial_location: Location, final_location: Location
    ) -> List[LabelledPoint]:
        raise NotImplementedError

    def project_point(
        self,
        location: Location,
        direction: Vector3D,
        search_distance: float = 10000.0,
    ) -> Optional[LabelledPoint]:
        raise NotImplementedError

    def ground_projection(
        self,
        location: Location,
        search_distance: float = 10000.0,
    ) -> Optional[LabelledPoint]:
        raise NotImplementedError

    def get_names_of_all_objects(self) -> List[str]:
        raise NotImplementedError

    def apply_color_texture_to_object(
        self,
        object_name: str,
        material_parameter: MaterialParameter,
        texture: TextureColor,
    ) -> None:
        raise NotImplementedError

    def apply_float_color_texture_to_object(
        self,
        object_name: str,
        material_parameter: MaterialParameter,
        texture: TextureColor,
    ) -> None:
        raise NotImplementedError

    def apply_textures_to_object(
        self,
        object_name: str,
        diffuse_texture: TextureColor,
        emissive_texture: TextureFloatColor,
        normal_texture: TextureFloatColor,
        ao_roughness_metallic_emissive_texture: TextureFloatColor,
    ) -> None:
        raise NotImplementedError

    def apply_color_texture_to_objects(
        self,
        objects_name_list: List[str],
        material_parameter: MaterialParameter,
        texture: TextureColor,
    ) -> None:
        raise NotImplementedError

    def apply_float_color_texture_to_objects(
        self,
        objects_name_list: List[str],
        material_parameter: MaterialParameter,
        texture: TextureColor,
    ) -> None:
        raise NotImplementedError

    def apply_textures_to_objects(
        self,
        objects_name_list: List[str],
        diffuse_texture: TextureColor,
        emissive_texture: TextureFloatColor,
        normal_texture: TextureFloatColor,
        ao_roughness_metallic_emissive_texture: TextureFloatColor,
    ) -> None:
        raise NotImplementedError


# https://github.com/carla-simulator/carla/blob/master/LibCarla/source/carla/client/DebugHelper.h
class DebugHelper:
    def draw_point(
        self,
        location: Location,
        size: float = 0.1,
        color: Color = Color(255, 0, 0),
        life_time: float = 1.0,
        persistent_lines: bool = True,
    ) -> None:
        raise NotImplementedError

    def draw_line(
        self,
        begin: Location,
        end: Location,
        thickness: float = 0.1,
        color: Color = Color(255, 0, 0),
        life_time: float = 1.0,
        persistent_lines: bool = True,
    ) -> None:
        raise NotImplementedError

    def draw_arrow(
        self,
        begin: Location,
        end: Location,
        thickness: float = 0.1,
        arrow_size: float = 0.1,
        color: Color = Color(255, 0, 0),
        life_time: float = 1.0,
        persistent_lines: bool = True,
    ) -> None:
        raise NotImplementedError

    def draw_box(
        self,
        box: BoundingBox,
        rotation: Rotation,
        thickness: float = 0.1,
        color: Color = Color(255, 0, 0),
        life_time: float = 1.0,
        persistent_lines: bool = True,
    ) -> None:
        raise NotImplementedError

    def draw_string(
        self,
        location: Location,
        text: str,
        draw_shadow: bool = False,
        color: Color = Color(255, 0, 0),
        life_time: float = 1.0,
        persistent_lines: bool = True,
    ) -> None:
        raise NotImplementedError
