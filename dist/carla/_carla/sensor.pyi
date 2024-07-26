from .control import VehiclePhysicsControl, VehicleControl
from .geom import Transform
from .sensor_data import RssEgoDynamicsOnRoute, GBufferTextureID
from ad.rss.state import ProperResponse
from ad.rss.world import RssDynamics
from enum import IntEnum, auto
from typing import Callable

class RssLogLevel:
    """
    Enum declaration used in carla.RssSensor to set the log level.
    """
    @property
    def critical(self): ...
    @property
    def debug(self): ...
    @property
    def err(self): ...
    @property
    def info(self): ...
    @property
    def off(self): ...
    @property
    def trace(self): ...
    @property
    def warn(self): ...

class RssRestrictor:
    """
    These objects apply restrictions to a carla.VehicleControl. It is part of the CARLA implementation of the [C++ Library for Responsibility Sensitive Safety](https://github.com/intel/ad-rss-lib). This class works hand in hand with a [rss sensor](ref_sensors.md#rss-sensor), which provides the data of the restrictions to be applied.
    """
    def restrict_vehicle_control(
        self,
        vehicle_control: VehicleControl,
        proper_response: ProperResponse,
        ego_dynamics_on_route: RssEgoDynamicsOnRoute,
        vehicle_physics: VehiclePhysicsControl,
    ) -> VehicleControl:
        """
        Applies the safety restrictions given by a carla.RssSensor to a carla.VehicleControl.
        """
    def set_log_level(self, log_level: RssLogLevel):
        """
        Sets the log level.
        """

class RssRoadBoundariesMode(IntEnum):
    """
    Enum declaration used in carla.RssSensor to enable or disable the [stay on road](https://intel.github.io/ad-rss-lib/ad_rss_map_integration/HandleRoadBoundaries/) feature. In summary, this feature considers the road boundaries as virtual objects. The minimum safety distance check is applied to these virtual walls, in order to make sure the vehicle does not drive off the road.
    """

    Off = auto()
    On = auto()

class RssSensor:
    """
    This sensor works a bit differently than the rest. Take look at the [specific documentation](adv_rss.md), and the [rss sensor reference](ref_sensors.md#rss-sensor) to gain full understanding of it.

    The RSS sensor uses world information, and a [RSS library](https://github.com/intel/ad-rss-lib) to make safety checks on a vehicle. The output retrieved by the sensor is a carla.RssResponse. This will be used by a carla.RssRestrictor to modify a carla.VehicleControl before applying it to a vehicle.
    """
    def __str__(self) -> str: ...
    def append_routing_target(self, routing_target: Transform):
        """
        Appends a new target position to the current route of the vehicle.
        """
    def drop_route(self):
        """
        Discards the current route. If there are targets remaining in **<font color="#f8805a">routing_targets</font>**, creates a new route using those. Otherwise, a new route is created at random.
        """
    def register_actor_constellation_callback(self, callback):
        """
        Register a callback to customize a carla.RssActorConstellationResult. By this callback the settings of RSS parameters are done per actor constellation and the settings (ego_vehicle_dynamics, other_vehicle_dynamics and pedestrian_dynamics) have no effect.
        """
    def reset_routing_targets(self):
        """
        Erases the targets that have been appended to the route.
        """
    def set_log_level(self, log_level: RssLogLevel):
        """
        Sets the log level.
        """
    def set_map_log_level(self, log_level: RssLogLevel):
        """
        Sets the map log level.
        """
    @property
    def ego_vehicle_dynamics(self) -> RssDynamics:
        """
        States the [RSS parameters](https://intel.github.io/ad-rss-lib/ad_rss/Appendix-ParameterDiscussion/) that the sensor will consider for the ego vehicle if no actor constellation callback is registered.
        """
    @property
    def other_vehicle_dynamics(self) -> RssDynamics:
        """
        States the [RSS parameters](https://intel.github.io/ad-rss-lib/ad_rss/Appendix-ParameterDiscussion/) that the sensor will consider for the rest of vehicles if no actor constellation callback is registered.
        """
    @property
    def pedestrian_dynamics(self) -> RssDynamics:
        """
        States the [RSS parameters](https://intel.github.io/ad-rss-lib/ad_rss/Appendix-ParameterDiscussion/) that the sensor will consider for pedestrians if no actor constellation callback is registered.
        """
    @property
    def road_boundaries_mode(self) -> RssRoadBoundariesMode:
        """
        Switches the [stay on road](https://intel.github.io/ad-rss-lib/ad_rss_map_integration/HandleRoadBoundaries/) feature. By default is __Off__.
        """
    @property
    def routing_targets(self) -> list[Transform]:
        """
        The current list of targets considered to route the vehicle. If no routing targets are defined, a route is generated at random.
        """

class Sensor:
    """
    Sensors compound a specific family of actors quite diverse and unique. They are normally spawned as attachment/sons of a vehicle (take a look at carla.World to learn about actor spawning). Sensors are thoroughly designed to retrieve different types of data that they are listening to. The data they receive is shaped as different subclasses inherited from carla.SensorData (depending on the sensor).

      Most sensors can be divided in two groups: those receiving data on every tick (cameras, point clouds and some specific sensors) and those who only receive under certain circumstances (trigger detectors). CARLA provides a specific set of sensors and their blueprint can be found in carla.BlueprintLibrary. All the information on their preferences and settlement can be found [here](ref_sensors.md), but the list of those available in CARLA so far goes as follow.
      <br><b>Receive data on every tick.</b>
      - [Depth camera](ref_sensors.md#depth-camera).
      - [Gnss sensor](ref_sensors.md#gnss-sensor).
      - [IMU sensor](ref_sensors.md#imu-sensor).
      - [Lidar raycast](ref_sensors.md#lidar-raycast-sensor).
      - [SemanticLidar raycast](ref_sensors.md#semanticlidar-raycast-sensor).
      - [Radar](ref_sensors.md#radar-sensor).
      - [RGB camera](ref_sensors.md#rgb-camera).
      - [RSS sensor](ref_sensors.md#rss-sensor).
      - [Semantic Segmentation camera](ref_sensors.md#semantic-segmentation-camera).
      <br><b>Only receive data when triggered.</b>
      - [Collision detector](ref_sensors.md#collision-detector).
      - [Lane invasion detector](ref_sensors.md#lane-invasion-detector).
      - [Obstacle detector](ref_sensors.md#obstacle-detector).
    """
    def __str__(self) -> str: ...
    def is_listening(self):
        """
        Returns whether the sensor is in a listening state.
        """
    def is_listening_gbuffer(self, gbuffer_id: GBufferTextureID):
        """
        Returns whether the sensor is in a listening state for a specific GBuffer texture.
        """
    def listen(self, callback: Callable):
        """
        The function the sensor will be calling to every time a new measurement is received. This function needs for an argument containing an object type carla.SensorData to work with.
        """
    def listen_to_gbuffer(self, gbuffer_id: GBufferTextureID, callback: Callable):
        """
        The function the sensor will be calling to every time the desired GBuffer texture is received.<br> This function needs for an argument containing an object type carla.SensorData to work with.
        """
    def stop(self):
        """
        Commands the sensor to stop listening for data.
        """
    def stop_gbuffer(self, gbuffer_id: GBufferTextureID):
        """
        Commands the sensor to stop listening for the specified GBuffer texture.
        """
    @property
    def is_listening(self) -> bool:
        """
        When <b>True</b> the sensor will be waiting for data.
        """
