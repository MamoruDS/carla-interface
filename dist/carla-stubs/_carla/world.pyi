from .actor import Actor, TrafficLight, TrafficSign
from .blueprint import ActorBlueprint, BlueprintLibrary, Color, FloatColor
from .geom import BoundingBox, Location, Rotation, Transform, Vector3D
from .light_manager import LightManager
from .map import Landmark, Map, Waypoint
from .sensor_data import CityObjectLabel
from .snapshot import WorldSnapshot
from .weather import WeatherParameters
from enum import IntEnum, auto
from typing import Callable
from typing_extensions import Self

class ActorList:
    """
    A class that contains every actor present on the scene and provides access to them. The list is automatically created and updated by the server and it can be returned using carla.World.
    """
    def __getitem__(self, pos: int) -> Actor:
        """
        Returns the actor corresponding to `pos` position in the list.
        """
    def __iter__(self):
        """
        Iterate over the carla.Actor contained in the list.
        """
    def __len__(self) -> int:
        """
        Returns the amount of actors listed.
        """
    def __str__(self) -> str:
        """
        Parses to the ID for every actor listed.
        """
    def filter(self, wildcard_pattern: str) -> list:
        """
        Filters a list of Actors matching `wildcard_pattern` against their variable __<font color="#f8805a">type_id</font>__ (which identifies the blueprint used to spawn them). Matching follows [fnmatch](https://docs.python.org/2/library/fnmatch.html) standard.
        """
    def find(self, actor_id: int) -> Actor:
        """
        Finds an actor using its identifier and returns it or <b>None</b> if it is not present.
        """

class AttachmentType(IntEnum):
    """
    Class that defines attachment options between an actor and its parent. When spawning actors, these can be attached to another actor so their position changes accordingly. This is specially useful for sensors. The snipet in carla.World.spawn_actor shows some sensors being attached to a car when spawned. Note that the attachment type is declared as an enum within the class.
    """

    Rigid = auto()
    SpringArm = auto()
    SpringArmGhost = auto()

class DebugHelper:
    """
    Helper class part of carla.World that defines methods for creating debug shapes. By default, shapes last one second. They can be permanent, but take into account the resources needed to do so. Take a look at the snipets available for this class to learn how to debug easily in CARLA.
    """
    def draw_arrow(
        self,
        begin: Location,
        end: Location,
        thickness: float,
        arrow_size: float,
        color: Color,
        life_time: float,
    ):
        """
        Draws an arrow from `begin` to `end` pointing in that direction.
        """
    def draw_box(
        self,
        box: BoundingBox,
        rotation: Rotation,
        thickness: float,
        color: Color,
        life_time: float,
    ):
        """
        Draws a box, ussually to act for object colliders.
        """
    def draw_line(
        self,
        begin: Location,
        end: Location,
        thickness: float,
        color: Color,
        life_time: float,
    ):
        """
        Draws a line in between `begin` and `end`.
        """
    def draw_point(
        self, location: Location, size: float, color: Color, life_time: float
    ):
        """
        Draws a point `location`.
        """
    def draw_string(
        self,
        location: Location,
        text: str,
        draw_shadow: bool,
        color: Color,
        life_time: float,
    ):
        """
        Draws a string in a given location of the simulation which can only be seen server-side.
        """

class EnvironmentObject:
    """
    Class that represents a geometry in the level, this geometry could be part of an actor formed with other EnvironmentObjects (ie: buildings).
    """
    def __str__(self) -> str:
        """
        Parses the EnvironmentObject to a string and shows them in command line.
        """
    @property
    def bounding_box(self) -> BoundingBox:
        """
        Object containing a location, rotation and the length of a box for every axis in world space.
        """
    @property
    def id(self) -> int:
        """
        Unique ID to identify the object in the level.
        """
    @property
    def name(self) -> str:
        """
        Name of the EnvironmentObject.
        """
    @property
    def transform(self) -> Transform:
        """
        Contains the location and orientation of the EnvironmentObject in world space.
        """
    @property
    def type(self) -> CityObjectLabel:
        """
        Semantic tag.
        """

class LabelledPoint:
    """
    Class that represent a position in space with a semantic label.
    """
    @property
    def label(self):
        """
        Semantic tag of the point.
        """
    @property
    def location(self):
        """
        Position in 3D space.
        """

class MapLayer(IntEnum):
    """
    Class that represents each manageable layer of the map. Can be used as flags. __WARNING: Only "Opt" maps are able to work with map layers.__
    """

    All = auto()
    Buildings = auto()
    Decals = auto()
    Foliage = auto()
    Ground = auto()
    NONE = auto()
    ParkedVehicles = auto()
    Particles = auto()
    Props = auto()
    StreetLights = auto()
    Walls = auto()

class MaterialParameter(IntEnum):
    """
    Class that represents material parameters. Not all objects in the scene contain all parameters.
    """

    AO_Roughness_Metallic_Emissive = auto()
    Diffuse = auto()
    Emissive = auto()
    Normal = auto()

class TextureColor:
    """
    Class representing a texture object to be uploaded to the server. Pixel format is RGBA, uint8 per channel.
    """
    def __init__(self, width: int, height: int):
        """
        Initializes a the texture with a (`width`, `height`) size.
        """
    def get(self, x: int, y: int) -> Color:
        """
        Get the (x,y) pixel data.
        """
    def set(self, x: int, y: int, value: Color):
        """
        Sets the (x,y) pixel data with `value`.
        """
    def set_dimensions(self, width: int, height: int):
        """
        Resizes the texture to te specified dimensions.
        """
    @property
    def height(self) -> int:
        """
        Y-coordinate size of the texture.
        """
    @property
    def width(self) -> int:
        """
        X-coordinate size of the texture.
        """

class TextureFloatColor:
    """
    Class representing a texture object to be uploaded to the server. Pixel format is RGBA, float per channel.
    """
    def __init__(self, width: int, height: int):
        """
        Initializes a the texture with a (`width`, `height`) size.
        """
    def get(self, x: int, y: int) -> FloatColor:
        """
        Get the (x,y) pixel data.
        """
    def set(self, x: int, y: int, value: FloatColor):
        """
        Sets the (x,y) pixel data with `value`.
        """
    def set_dimensions(self, width: int, height: int):
        """
        Resizes the texture to te specified dimensions.
        """
    @property
    def height(self) -> int:
        """
        Y-coordinate size of the texture.
        """
    @property
    def width(self) -> int:
        """
        X-coordinate size of the texture.
        """

class Timestamp:
    """
    Class that contains time information for simulated data. This information is automatically retrieved as part of the carla.WorldSnapshot the client gets on every frame, but might also be used in many other situations such as a carla.Sensor retrieveing data.
    """
    def __eq__(self, other: Self) -> bool: ...
    def __init__(
        self,
        frame: int,
        elapsed_seconds: float,
        delta_seconds: float,
        platform_timestamp: float,
    ): ...
    def __ne__(self, other: Self) -> bool: ...
    def __str__(self) -> str: ...
    @property
    def delta_seconds(self) -> float:
        """
        Simulated seconds elapsed since the previous frame.
        """
    @property
    def elapsed_seconds(self) -> float:
        """
        Simulated seconds elapsed since the beginning of the current episode.
        """
    @property
    def frame(self) -> int:
        """
        The number of frames elapsed since the simulator was launched.
        """
    @property
    def platform_timestamp(self) -> float:
        """
        Time register of the frame at which this measurement was taken given by the OS in seconds.
        """

class World:
    """
    World objects are created by the client to have a place for the simulation to happen. The world contains the map we can see, meaning the asset, not the navigation map. Navigation maps are part of the carla.Map class. It also manages the weather and actors present in it. There can only be one world per simulation, but it can be changed anytime.
    """
    def __str__(self) -> str:
        """
        The content of the world is parsed and printed as a brief report of its current state.
        """
    def apply_color_texture_to_object(
        self,
        object_name: str,
        material_parameter: MaterialParameter,
        texture: TextureColor,
    ):
        """
        Applies a `texture` object in the field corresponfing to `material_parameter` (normal, diffuse, etc) to the object in the scene corresponding to `object_name`.
        """
    def apply_color_texture_to_objects(
        self,
        objects_name_list: list[str],
        material_parameter: MaterialParameter,
        texture: TextureColor,
    ):
        """
        Applies a `texture` object in the field corresponfing to `material_parameter` (normal, diffuse, etc) to the object in the scene corresponding to all objects in `objects_name_list`.
        """
    def apply_float_color_texture_to_object(
        self,
        object_name: str,
        material_parameter: MaterialParameter,
        texture: TextureFloatColor,
    ):
        """
        Applies a `texture` object in the field corresponfing to `material_parameter` (normal, diffuse, etc) to the object in the scene corresponding to `object_name`.
        """
    def apply_float_color_texture_to_objects(
        self,
        objects_name_list: list[str],
        material_parameter: MaterialParameter,
        texture: TextureFloatColor,
    ):
        """
        Applies a `texture` object in the field corresponfing to `material_parameter` (normal, diffuse, etc) to the object in the scene corresponding to all objects in `objects_name_list`.
        """
    def apply_settings(self, world_settings: WorldSettings) -> int:
        """
        This method applies settings contained in an object to the simulation running and returns the ID of the frame they were implemented.
        """
    def apply_textures_to_object(
        self,
        object_name: str,
        diffuse_texture: TextureColor,
        emissive_texture: TextureFloatColor,
        normal_texture: TextureFloatColor,
        ao_roughness_metallic_emissive_texture: TextureFloatColor,
    ):
        """
        Applies all texture fields in carla.MaterialParameter to the object `object_name`. Empty textures here will not be applied.
        """
    def apply_textures_to_objects(
        self,
        objects_name_list: list[str],
        diffuse_texture: TextureColor,
        emissive_texture: TextureFloatColor,
        normal_texture: TextureFloatColor,
        ao_roughness_metallic_emissive_texture: TextureFloatColor,
    ):
        """
        Applies all texture fields in carla.MaterialParameter to all objects in `objects_name_list`. Empty textures here will not be applied.
        """
    def cast_ray(
        self, initial_location: Location, final_location: Location
    ) -> list[LabelledPoint]:
        """
        Casts a ray from the specified initial_location to final_location. The function then detects all geometries intersecting the ray and returns a list of carla.LabelledPoint in order.
        """
    def enable_environment_objects(self, env_objects_ids: set[int], enable: bool):
        """
        Enable or disable a set of EnvironmentObject identified by their id. These objects will appear or disappear from the level.
        """
    def freeze_all_traffic_lights(self, frozen: bool):
        """
        Freezes or unfreezes all traffic lights in the scene. Frozen traffic lights can be modified by the user but the time will not update them until unfrozen.
        """
    def get_actor(self, actor_id: int) -> Actor:
        """
        Looks up for an actor by ID and returns <b>None</b> if not found.
        """
    def get_actors(self, actor_ids: list) -> ActorList:
        """
        Retrieves a list of carla.Actor elements, either using a list of IDs provided or just listing everyone on stage. If an ID does not correspond with any actor, it will be excluded from the list returned, meaning that both the list of IDs and the list of actors may have different lengths.
        """
    def get_blueprint_library(self) -> BlueprintLibrary:
        """
        Returns a list of actor blueprints available to ease the spawn of these into the world.
        """
    def get_environment_objects(
        self, object_type: CityObjectLabel
    ) -> list[EnvironmentObject]:
        """
        Returns a list of EnvironmentObject with the requested semantic tag.  The method returns all the EnvironmentObjects in the level by default, but the query can be filtered by semantic tags with the argument `object_type`.
        """
    def get_level_bbs(self, actor_type: CityObjectLabel) -> list[BoundingBox]:
        """
        Returns an array of bounding boxes with location and rotation in world space. The method returns all the bounding boxes in the level by default, but the query can be filtered by semantic tags with the argument `actor_type`.
        """
    def get_lightmanager(self) -> LightManager:
        """
        Returns an instance of carla.LightManager that can be used to handle the lights in the scene.
        """
    def get_map(self) -> Map:
        """
        Asks the server for the XODR containing the map file, and returns this parsed as a carla.Map.
        """
    def get_names_of_all_objects(self) -> list[str]:
        """
        Returns a list of the names of all objects in the scene that can be painted with the apply texture functions.
        """
    def get_random_location_from_navigation(self) -> Location:
        """
        This can only be used with walkers. It retrieves a random location to be used as a destination using the __<font color="#7fb800">go_to_location()</font>__ method in carla.WalkerAIController. This location will be part of a sidewalk. Roads, crosswalks and grass zones are excluded. The method does not take into consideration locations of existing actors so if a collision happens when trying to spawn an actor, it will return an error. Take a look at [`generate_traffic.py`](https://github.com/carla-simulator/carla/blob/master/PythonAPI/examples/generate_traffic.py) for an example.
        """
    def get_settings(self) -> WorldSettings:
        """
        Returns an object containing some data about the simulation such as synchrony between client and server or rendering mode.
        """
    def get_snapshot(self) -> WorldSnapshot:
        """
        Returns a snapshot of the world at a certain moment comprising all the information about the actors.
        """
    def get_spectator(self) -> Actor:
        """
        Returns the spectator actor. The spectator is a special type of actor created by Unreal Engine, usually with ID=0, that acts as a camera and controls the view in the simulator window.
        """
    def get_traffic_light(self, landmark: Landmark) -> TrafficLight:
        """
        Provided a landmark, returns the traffic light object it describes.
        """
    def get_traffic_light_from_opendrive_id(
        self, traffic_light_id: str
    ) -> TrafficLight:
        """
        Returns the traffic light actor corresponding to the indicated OpenDRIVE id.
        """
    def get_traffic_lights_from_waypoint(
        self, waypoint: Waypoint, distance: float
    ) -> list[TrafficLight]:
        """
        This function performs a search along the road in front of the specified waypoint and returns a list of traffic light actors found in the specified search distance.
        """
    def get_traffic_lights_in_junction(self, junction_id: int) -> list[TrafficLight]:
        """
        Returns the list of traffic light actors affecting the junction indicated in `junction_id`.
        """
    def get_traffic_sign(self, landmark: Landmark) -> TrafficSign:
        """
        Provided a landmark, returns the traffic sign object it describes.
        """
    def get_vehicles_light_states(self) -> dict:
        """
        Returns a dict where the keys are carla.Actor IDs and the values are carla.VehicleLightState of that vehicle.
        """
    def get_weather(self) -> WeatherParameters:
        """
        Retrieves an object containing weather parameters currently active in the simulation, mainly cloudiness, precipitation, wind and sun position.
        """
    def ground_projection(
        self, location: Location, search_distance: float
    ) -> LabelledPoint:
        """
        Projects the specified point downwards in the scene. The functions casts a ray from location in the direction (0,0,-1) (downwards) and returns a carla.Labelled object with the first geometry this ray intersects (usually the ground). If no geometry is found in the search_distance range the function returns `None`.
        """
    def load_map_layer(self, map_layers: MapLayer):
        """
        Loads the selected layers to the level. If the layer is already loaded the call has no effect.
        """
    def on_tick(self, callback: WorldSnapshot) -> int:
        """
        This method is used in [__asynchronous__ mode](https://carla.readthedocs.io/en/latest/adv_synchrony_timestep/). It starts callbacks from the client for the function defined as `callback`, and returns the ID of the callback. The function will be called everytime the server ticks. It requires a carla.WorldSnapshot as argument, which can be retrieved from __<font color="#7fb800">wait_for_tick()</font>__. Use __<font color="#7fb800">remove_on_tick()</font>__ to stop the callbacks.
        """
    def project_point(
        self, location: Location, direction: Vector3D, search_distance: float
    ) -> LabelledPoint:
        """
        Projects the specified point to the desired direction in the scene. The functions casts a ray from location in a direction and returns a carla.Labelled object with the first geometry this ray intersects. If no geometry is found in the search_distance range the function returns `None`.
        """
    def remove_on_tick(self, callback_id: Callable):
        """
        Stops the callback for `callback_id` started with __<font color="#7fb800">on_tick()</font>__.
        """
    def reset_all_traffic_lights(self):
        """
        Resets the cycle of all traffic lights in the map to the initial state.
        """
    def set_pedestrians_cross_factor(self, percentage: float): ...
    def set_pedestrians_seed(self, seed: int): ...
    def set_weather(self, weather: WeatherParameters):
        """
        Changes the weather parameteres ruling the simulation to another ones defined in an object.
        """
    def spawn_actor(
        self,
        blueprint: ActorBlueprint,
        transform: Transform,
        attach_to: Actor,
        attachment: AttachmentType,
    ) -> Actor:
        """
        The method will create, return and spawn an actor into the world. The actor will need an available blueprint to be created and a transform (location and rotation). It can also be attached to a parent with a certain attachment type.
        """
    def tick(self, seconds: float) -> int:
        """
        This method is used in [__synchronous__ mode](https://carla.readthedocs.io/en/latest/adv_synchrony_timestep/), when the server waits for a client tick before computing the next frame. This method will send the tick, and give way to the server. It returns the ID of the new frame computed by the server.
        """
    def try_spawn_actor(
        self,
        blueprint: ActorBlueprint,
        transform: Transform,
        attach_to: Actor,
        attachment: AttachmentType,
    ) -> Actor:
        """
        Same as __<font color="#7fb800">spawn_actor()</font>__ but returns <b>None</b> on failure instead of throwing an exception.
        """
    def unload_map_layer(self, map_layers: MapLayer):
        """
        Unloads the selected layers to the level. If the layer is already unloaded the call has no effect.
        """
    def wait_for_tick(self, seconds: float) -> WorldSnapshot:
        """
        This method is used in [__asynchronous__ mode](https://carla.readthedocs.io/en/latest/adv_synchrony_timestep/). It makes the client wait for a server tick. When the next frame is computed, the server will tick and return a snapshot describing the new state of the world.
        """
    @property
    def debug(self) -> DebugHelper:
        """
        Responsible for creating different shapes for debugging. Take a look at its class to learn more about it.
        """
    @property
    def id(self) -> int:
        """
        The ID of the episode associated with this world. Episodes are different sessions of a simulation. These change everytime a world is disabled or reloaded. Keeping track is useful to avoid possible issues.
        """

class WorldSettings:
    """
    The simulation has some advanced configuration options that are contained in this class and can be managed using carla.World and its methods. These allow the user to choose between client-server synchrony/asynchrony, activation of "no rendering mode" and either if the simulation should run with a fixed or variable time-step. Check [this](adv_synchrony_timestep.md) out if you want to learn about it.
    """
    def __eq__(self, other: Self) -> bool:
        """
        Returns <b>True</b> if both objects' variables are the same.
        """
    def __init__(
        self,
        synchronous_mode: bool,
        no_rendering_mode: bool,
        fixed_delta_seconds: float,
    ):
        """
        Creates an object containing desired settings that could later be applied through carla.World and its method __<font color="#7fb800">apply_settings()</font>__.
        """
    def __ne__(self, other: Self) -> bool:
        """
        Returns <b>True</b> if both objects' variables are different.
        """
    def __str__(self) -> str:
        """
        Parses the established settings to a string and shows them in command line.
        """
    @property
    def actor_active_distance(self) -> float:
        """
        Used for large maps only. Configures the distance from the hero vehicle to convert actors to dormant. Actors within this range will be active, and actors outside will become dormant.
        """
    @property
    def deterministic_ragdolls(self) -> bool:
        """
        Defines wether to use deterministic physics for pedestrian death animations or physical ragdoll simulation.  When enabled, pedestrians have less realistic death animation but ensures determinism.  When disabled, pedestrians are simulated as ragdolls with more realistic simulation and collision but no determinsm can be ensured.
        """
    @property
    def fixed_delta_seconds(self) -> float:
        """
        Ensures that the time elapsed between two steps of the simulation is fixed. Set this to <b>0.0</b> to work with a variable time-step, as happens by default.
        """
    @property
    def max_culling_distance(self) -> float:
        """
        Configure the max draw distance for each mesh of the level.
        """
    @property
    def max_substep_delta_time(self) -> float:
        """
        Maximum delta time of the substeps. If the carla.WorldSettingsmax_substep is high enough, the substep delta time would be always below or equal to this value. By default, the value is set to 0.01.
        """
    @property
    def max_substeps(self) -> int:
        """
        The maximum number of physics substepping that are allowed. By default, the value is set to 10.
        """
    @property
    def no_rendering_mode(self) -> bool:
        """
        When enabled, the simulation will run no rendering at all. This is mainly used to avoid overhead during heavy traffic simulations. It is false by default.
        """
    @property
    def substepping(self) -> bool:
        """
        Enable the physics substepping. This option allows computing some physics substeps between two render frames. If synchronous mode is set, the number of substeps and its time interval are fixed and computed are so they fulfilled the requirements of carla.WorldSettings.max_substep and carla.WorldSettings.max_substep_delta_time. These last two parameters need to be compatible with carla.WorldSettings.fixed_delta_seconds. Enabled by default.
        """
    @property
    def synchronous_mode(self) -> bool:
        """
        States the synchrony between client and server. When set to true, the server will wait for a client tick in order to move forward. It is false by default.
        """
    @property
    def tile_stream_distance(self) -> float:
        """
        Used for large maps only. Configures the maximum distance from the hero vehicle to stream tiled maps. Regions of the map within this range will be visible (and capable of simulating physics). Regions outside this region will not be loaded.
        """
