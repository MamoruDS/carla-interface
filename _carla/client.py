# https://github.com/carla-simulator/carla/blob/master/PythonAPI/carla/source/libcarla/Client.cpp
from ._c.traffic_manager import TM_DEFAULT_PORT
from .traffic_manager import TrafficManager
from .world import World, MapLayer
from typing import List


class OpendriveGenerationParameters:
    def __init__(
        self,
        vertex_distance: float = 2.0,
        max_road_length: float = 50.0,
        wall_height: float = 1.0,
        additional_width: float = 0.6,
        smooth_junctions: bool = True,
        enable_mesh_visibility: bool = True,
        enable_pedestrian_navigation: bool = True,
    ) -> None:
        raise NotImplementedError

    @property
    def vertex_distance(self) -> float:
        raise NotImplementedError

    @vertex_distance.setter
    def vertex_distance(self, val: float) -> None:
        raise NotImplementedError

    @property
    def max_road_length(self) -> float:
        raise NotImplementedError

    @max_road_length.setter
    def max_road_length(self, val: float) -> None:
        raise NotImplementedError

    @property
    def wall_height(self) -> float:
        raise NotImplementedError

    @wall_height.setter
    def wall_height(self, val: float) -> None:
        raise NotImplementedError

    @property
    def additional_width(self) -> float:
        raise NotImplementedError

    @additional_width.setter
    def additional_width(self, val: float) -> None:
        raise NotImplementedError

    @property
    def smooth_junctions(self) -> bool:
        raise NotImplementedError

    @smooth_junctions.setter
    def smooth_junctions(self, val: bool) -> None:
        raise NotImplementedError

    @property
    def enable_mesh_visibility(self) -> bool:
        raise NotImplementedError

    @enable_mesh_visibility.setter
    def enable_mesh_visibility(self, val: bool) -> None:
        raise NotImplementedError

    @property
    def enable_pedestrian_navigation(self) -> bool:
        raise NotImplementedError

    @enable_pedestrian_navigation.setter
    def enable_pedestrian_navigation(self, val: bool) -> None:
        raise NotImplementedError


class Client:
    def __init__(self, host: str, port: int, worker_threads: int = 0) -> None:
        raise NotImplementedError

    def set_timeout(self, seconds: float) -> None:
        """
        Set a timeout for networking operations. If set, any networking
        operation taking longer than @a timeout throws rpc::timeout.
        """
        raise NotImplementedError

    def get_client_version(self) -> str:
        """
        Return the version string of this client API.
        """
        raise NotImplementedError

    def get_server_version(self) -> str:
        """
        Return the version string of the simulator we are connected to.
        """
        raise NotImplementedError

    def get_world(self) -> World:
        """
        Return an instance of the world currently active in the simulator.
        """
        raise NotImplementedError

    def get_available_maps(self) -> List[str]:
        raise NotImplementedError

    def set_files_base_folder(self, path: str) -> bool:
        raise NotImplementedError

    def get_required_files(
        self, folder: str = "", download: bool = True
    ) -> List[str]:
        raise NotImplementedError

    def request_file(self, name: str) -> None:
        raise NotImplementedError

    def reload_world(self, reset_settings: bool = True) -> World:
        raise NotImplementedError

    def load_world(
        self,
        map_name: str,
        reset_settings: bool = True,
        map_layers: MapLayer = MapLayer.All,
    ) -> World:
        raise NotImplementedError

    def generate_opendrive_world(
        self,
        opendrive: str,
        parameters: OpendriveGenerationParameters = OpendriveGenerationParameters(),
        reset_settings: bool = True,
    ) -> World:
        raise NotImplementedError

    def start_recorder(self, name: str, additional_data: bool = False) -> str:
        raise NotImplementedError

    def stop_recorder(self) -> None:
        raise NotImplementedError

    def show_recorder_file_info(self, name: str, show_all: bool) -> str:
        raise NotImplementedError

    def show_recorder_collisions(
        self, name: str, type1: str, type2: str
    ) -> str:
        raise NotImplementedError

    def show_recorder_actors_blocked(
        self, name: str, min_time: float, min_distance: float
    ) -> str:
        raise NotImplementedError

    def replay_file(
        self,
        name: str,
        time_start: float,
        duration: float,
        follow_id: int,
        replay_sensors: bool = False,
    ) -> str:
        raise NotImplementedError

    def stop_replayer(self, keep_actors: bool) -> None:
        raise NotImplementedError

    def set_replayer_time_factor(self, time_factor: float) -> None:
        raise NotImplementedError

    def set_replayer_ignore_hero(self, ignore_hero: bool) -> None:
        raise NotImplementedError

    # commands: `const boost::python::object &commands`
    def apply_batch(self, commands, do_tick: bool = False):
        raise NotImplementedError

    # commands: `const boost::python::object &commands`
    def apply_batch_sync(self, commands, do_tick: bool = False):
        raise NotImplementedError

    def get_trafficmanager(
        self, port: int = TM_DEFAULT_PORT
    ) -> TrafficManager:
        raise NotImplementedError
