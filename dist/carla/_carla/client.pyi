""" """

from .actor import Actor
from .command import Response
from .world import World, MapLayer

class Client:
    """
    The Client connects CARLA to the server which runs the simulation. Both server and client contain a CARLA library (libcarla) with some differences that allow communication between them. Many clients can be created and each of these will connect to the RPC server inside the simulation to send commands. The simulation runs server-side. Once the connection is established, the client will only receive data retrieved from the simulation. Walkers are the exception. The client is in charge of managing pedestrians so, if you are running a simulation with multiple clients, some issues may arise. For example, if you spawn walkers through different clients, collisions may happen, as each client is only aware of the ones it is in charge of.

      The client also has a recording feature that saves all the information of a simulation while running it. This allows the server to replay it at will to obtain information and experiment with it. [Here](adv_recorder.md) is some information about how to use this recorder.
    """
    def __init__(self, host: str, port: int, worker_threads: int):
        """
        Client constructor
        """
    def apply_batch(self, commands: list):
        """
        Executes a list of commands on a single simulation step and retrieves no information. If you need information about the response of each command, use the __<font color="#7fb800">apply_batch_sync()</font>__ method. [Here](https://github.com/carla-simulator/carla/blob/master/PythonAPI/examples/generate_traffic.py) is an example on how to delete the actors that appear in carla.ActorList all at once.
        """
    def apply_batch_sync(self, commands: list, due_tick_cue: bool) -> list[Response]:
        """
        Executes a list of commands on a single simulation step, blocks until the commands are linked, and returns a list of <b>command.Response</b> that can be used to determine whether a single command succeeded or not. [Here](https://github.com/carla-simulator/carla/blob/master/PythonAPI/examples/generate_traffic.py) is an example of it being used to spawn actors.
        """
    def generate_opendrive_world(
        self,
        opendrive: str,
        parameters: OpendriveGenerationParameters,
        reset_settings: bool,
    ):
        """
        Loads a new world with a basic 3D topology generated from the content of an OpenDRIVE file. This content is passed as a `string` parameter. It is similar to `client.load_world(map_name)` but allows for custom OpenDRIVE maps in server side. Cars can drive around the map, but there are no graphics besides the road and sidewalks.
        """
    def get_available_maps(self) -> list[str]:
        """
        Returns a list of strings containing the paths of the maps available on server. These paths are dynamic, they will be created during the simulation and so you will not find them when looking up in your files. One of the possible returns for this method would be:
          ['/Game/Carla/Maps/Town01',
          '/Game/Carla/Maps/Town02',
          '/Game/Carla/Maps/Town03',
          '/Game/Carla/Maps/Town04',
          '/Game/Carla/Maps/Town05',
          '/Game/Carla/Maps/Town06',
          '/Game/Carla/Maps/Town07']
        """
    def get_client_version(self) -> str:
        """
        Returns the client libcarla version by consulting it in the "Version.h" file. Both client and server can use different libcarla versions but some issues may arise regarding unexpected incompatibilities.
        """
    def get_required_files(self, folder: str, download: bool):
        """
        Asks the server which files are required by the client to use the current map. Option to download files automatically if they are not already in the cache.
        """
    def get_server_version(self) -> str:
        """
        Returns the server libcarla version by consulting it in the "Version.h" file. Both client and server should use the same libcarla version.
        """
    def get_trafficmanager(self, client_connection: int) -> TrafficManager:
        """
        Returns an instance of the traffic manager related to the specified port. If it does not exist, this will be created.
        """
    def get_world(self) -> World:
        """
        Returns the world object currently active in the simulation. This world will be later used for example to load maps.
        """
    def load_world(self, map_name: str, reset_settings: bool, map_layers: MapLayer):
        """
        Creates a new world with default settings using `map_name` map. All actors in the current world will be destroyed.
        """
    def reload_world(self, reset_settings: bool):
        """
        Reload the current world, note that a new world is created with default settings using the same map. All actors present in the world will be destroyed, __but__ traffic manager instances will stay alive.
        """
    def replay_file(
        self,
        name: str,
        start: float,
        duration: float,
        follow_id: int,
        replay_sensors: bool,
    ):
        """
        Load a new world with default settings using `map_name` map. All actors present in the current world will be destroyed, __but__ traffic manager instances will stay alive.
        """
    def request_file(self, name: str):
        """
        Requests one of the required files returned by carla.Client.get_required_files.
        """
    def set_files_base_folder(self, path: str): ...
    def set_replayer_ignore_hero(self, ignore_hero: bool): ...
    def set_replayer_time_factor(self, time_factor: float):
        """
        When used, the time speed of the reenacted simulation is modified at will. It can be used several times while a playback is in curse.
        """
    def set_timeout(self, seconds: float):
        """
        Sets the maxixum time a network call is allowed before blocking it and raising a timeout exceeded error.
        """
    def show_recorder_actors_blocked(
        self, filename: str, min_time: float, min_distance: float
    ) -> str:
        """
        The terminal will show the information registered for actors considered blocked. An actor is considered blocked when it does not move a minimum distance in a period of time, being these `min_distance` and `min_time`.
        """
    def show_recorder_collisions(
        self, filename: str, category1: str, category2: str
    ) -> str:
        """
        The terminal will show the collisions registered by the recorder. These can be filtered by specifying the type of actor involved. The categories will be specified in `category1` and `category2` as follows:
          'h' = Hero, the one vehicle that can be controlled manually or managed by the user.
          'v' = Vehicle
          'w' = Walker
          't' = Traffic light
          'o' = Other
          'a' = Any
        If you want to see only collisions between a vehicles and a walkers, use for `category1` as 'v' and `category2` as 'w' or vice versa. If you want to see all the collisions (filter off) you can use 'a' for both parameters.
        """
    def show_recorder_file_info(self, filename: str, show_all: bool) -> str:
        """
        The information saved by the recorder will be parsed and shown in your terminal as text (frames, times, events, state, positions...). The information shown can be specified by using the `show_all` parameter. [Here](ref_recorder_binary_file_format.md) is some more information about how to read the recorder file.
        """
    def start_recorder(self, filename: str, additional_data: bool):
        """
        Enables the recording feature, which will start saving every information possible needed by the server to replay the simulation.
        """
    def stop_recorder(self):
        """
        Stops the recording in progress. If you specified a path in `filename`, the recording will be there. If not, look inside `CarlaUE4/Saved/`.
        """
    def stop_replayer(self, keep_actors: bool):
        """
        Stop current replayer.
        """

class OpendriveGenerationParameters:
    """
    This class defines the parameters used when generating a world using an OpenDRIVE file.
    """
    @property
    def additional_width(self) -> float:
        """
        Additional with applied junction lanes. Complex situations tend to occur at junctions, and a little increase can prevent vehicles from falling off the road.  __Default is `0.6`__.
        """
    @property
    def enable_mesh_visibility(self) -> bool:
        """
        If __True__, the road mesh will be rendered. Setting this to __False__ should reduce the rendering overhead.  __Default is `True`__.
        """
    @property
    def enable_pedestrian_navigation(self) -> bool:
        """
        If __True__, Pedestrian navigation will be enabled using Recast tool. For very large maps it is recomended to disable this option. __Default is `True`__.
        """
    @property
    def max_road_length(self) -> float:
        """
        Max road length for a single mesh portion. The mesh of the map is divided into portions, in order to avoid propagating issues. __Default is `50.0`__.
        """
    @property
    def smooth_junctions(self) -> bool:
        """
        If __True__, the mesh at junctions will be smoothed to prevent issues where roads blocked other roads. __Default is `True`__.
        """
    @property
    def vertex_distance(self) -> float:
        """
        Distance between vertices of the mesh generated. __Default is `2.0`__.
        """
    @property
    def wall_height(self) -> float:
        """
        Height of walls created on the boundaries of the road. These prevent vehicles from falling off the road. __Default is `1.0`__.
        """

class TrafficManager:
    """
    The traffic manager is a module built on top of the CARLA API in C++. It handles any group of vehicles set to autopilot mode to populate the simulation with realistic urban traffic conditions and give the chance to user to customize some behaviours. The architecture of the traffic manager is divided in five different goal-oriented stages and a PID controller where the information flows until eventually, a carla.VehicleControl is applied to every vehicle registered in a traffic manager.
    In order to learn more, visit the [documentation](adv_traffic_manager.md) regarding this module.
    """
    def auto_lane_change(self, actor: Actor, enable: bool):
        """
        Turns on or off lane changing behaviour for a vehicle.
        """
    def collision_detection(
        self, reference_actor: Actor, other_actor: Actor, detect_collision: bool
    ):
        """
        Tunes on/off collisions between a vehicle and another specific actor. In order to ignore all other vehicles, traffic lights or walkers, use the specific __ignore__ methods described in this same section.
        """
    def distance_to_leading_vehicle(self, actor: Actor, distance: float):
        """
        Sets the minimum distance in meters that a vehicle has to keep with the others. The distance is in meters and will affect the minimum moving distance. It is computed from front to back of the vehicle objects.
        """
    def force_lane_change(self, actor: Actor, direction: bool):
        """
        Forces a vehicle to change either to the lane on its left or right, if existing, as indicated in `direction`. This method applies the lane change no matter what, disregarding possible collisions.
        """
    def get_all_actions(self, actor: Actor):
        """
        Returns all known actions (i.e. road options and waypoints) that an actor controlled by the Traffic Manager will perform in its next steps.
        """
    def get_next_action(self, actor: Actor):
        """
        Returns the next known road option and waypoint that an actor controlled by the Traffic Manager will follow.
        """
    def get_port(self) -> int:
        """
        Returns the port where the Traffic Manager is connected. If the object is a TM-Client, it will return the port of its TM-Server. Read the [documentation](#adv_traffic_manager.md#multiclient-and-multitm-management) to learn the difference.
        """
    def global_lane_offset(self, offset: float):
        """
        Sets a global lane offset displacement from the center line. Positive values imply a right offset while negative ones mean a left one.
        Default is 0. Numbers high enough to cause the vehicle to drive through other lanes might break the controller.
        """
    def global_percentage_speed_difference(self, percentage: float):
        """
        Sets the difference the vehicle's intended speed and its current speed limit. Speed limits can be exceeded by setting the `perc` to a negative value.
        Default is 30. Exceeding a speed limit can be done using negative percentages.
        """
    def ignore_lights_percentage(self, actor: Actor, perc: float):
        """
        During the traffic light stage, which runs every frame, this method sets the percent chance that traffic lights will be ignored for a vehicle.
        """
    def ignore_signs_percentage(self, actor: Actor, perc: float):
        """
        During the traffic light stage, which runs every frame, this method sets the percent chance that stop signs will be ignored for a vehicle.
        """
    def ignore_vehicles_percentage(self, actor: Actor, perc: float):
        """
        During the collision detection stage, which runs every frame, this method sets a percent chance that collisions with another vehicle will be ignored for a vehicle.
        """
    def ignore_walkers_percentage(self, actor: Actor, perc: float):
        """
        During the collision detection stage, which runs every frame, this method sets a percent chance that collisions with walkers will be ignored for a vehicle.
        """
    def keep_right_rule_percentage(self, actor: Actor, perc: float):
        """
        During the localization stage, this method sets a percent chance that vehicle will follow the *keep right* rule, and stay in the right lane.
        """
    def random_left_lanechange_percentage(self, actor: Actor, percentage: float):
        """
        Adjust probability that in each timestep the actor will perform a left lane change, dependent on lane change availability.
        """
    def random_right_lanechange_percentage(self, actor: Actor, percentage: float):
        """
        Adjust probability that in each timestep the actor will perform a right lane change, dependent on lane change availability.
        """
    def set_boundaries_respawn_dormant_vehicles(
        self, lower_bound: float, upper_bound: float
    ):
        """
        Sets the upper and lower boundaries for dormant actors to be respawned near the hero vehicle.
        """
    def set_desired_speed(self, actor: Actor, speed: float):
        """
        Sets the speed of a vehicle to the specified value.
        """
    def set_global_distance_to_leading_vehicle(self, distance: float):
        """
        Sets the minimum distance in meters that vehicles have to keep with the rest. The distance is in meters and will affect the minimum moving distance. It is computed from center to center of the vehicle objects.
        """
    def set_hybrid_physics_mode(self, enabled: bool):
        """
        Enables or disables the hybrid physics mode. In this mode, vehicle's farther than a certain radius from the ego vehicle will have their physics disabled. Computation cost will be reduced by not calculating vehicle dynamics. Vehicles will be teleported.
        """
    def set_hybrid_physics_radius(self, r: float):
        """
        With hybrid physics on, changes the radius of the area of influence where physics are enabled.
        """
    def set_osm_mode(self, mode_switch: bool):
        """
        Enables or disables the OSM mode. This mode allows the user to run TM in a map created with the [OSM feature](tuto_G_openstreetmap.md). These maps allow having dead-end streets. Normally, if vehicles cannot find the next waypoint, TM crashes. If OSM mode is enabled, it will show a warning, and destroy vehicles when necessary.
        """
    def set_path(self, actor: Actor, path: list):
        """
        Sets a list of locations for a vehicle to follow while controlled by the Traffic Manager.
        """
    def set_random_device_seed(self, value: int):
        """
        Sets a specific random seed for the Traffic Manager, thereby setting it to be deterministic.
        """
    def set_respawn_dormant_vehicles(self, mode_switch: bool):
        """
        If __True__, vehicles in large maps will respawn near the hero vehicle when they become dormant. Otherwise, they will stay dormant until they are within `actor_active_distance` of the hero vehicle again.
        """
    def set_route(self, actor: Actor, path: list):
        """
        Sets a list of route instructions for a vehicle to follow while controlled by the Traffic Manager. The possible route instructions are 'Left', 'Right', 'Straight'.
        """
    def set_synchronous_mode(self, mode_switch: bool):
        """
        Sets the Traffic Manager to [synchronous mode](adv_traffic_manager.md#synchronous-mode). In a [multiclient situation](adv_traffic_manager.md#multiclient), only the TM-Server can tick. Similarly, in a [multiTM situation](adv_traffic_manager.md#multitm), only one TM-Server must tick. Use this method in the client that does the world tick, and right after setting the world to synchronous mode, to set which TM will be the master while in sync.
        """
    def update_vehicle_lights(self, actor: Actor, do_update: bool):
        """
        Sets if the Traffic Manager is responsible of updating the vehicle lights, or not.
        Default is __False__. The traffic manager will not change the vehicle light status of a vehicle, unless its auto_update_status is st to __True__.
        """
    def vehicle_lane_offset(self, actor: Actor, offset: float):
        """
        Sets a lane offset displacement from the center line. Positive values imply a right offset while negative ones mean a left one.
        Default is 0. Numbers high enough to cause the vehicle to drive through other lanes might break the controller.
        """
    def vehicle_percentage_speed_difference(self, actor: Actor, percentage: float):
        """
        Sets the difference the vehicle's intended speed and its current speed limit. Speed limits can be exceeded by setting the `perc` to a negative value.
        Default is 30. Exceeding a speed limit can be done using negative percentages.
        """
