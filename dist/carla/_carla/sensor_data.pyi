from .actor import Actor
from .blueprint import Color
from .geom import Transform, Vector3D, Location
from .map import LaneMarking
from ad.map.match import Object
from ad.map.point import ENUHeading, ENUPoint
from ad.map.route import FullRoute
from ad.physics import Distance, Acceleration, Speed
from ad.rss.map import RestrictSpeedLimitMode, RssMode
from ad.rss.situation import SituationSnapshot
from ad.rss.state import RssStateSnapshot, ProperResponse
from ad.rss.world import ObjectType, WorldModel, RssDynamics
from enum import IntEnum, auto

class CityObjectLabel(IntEnum):
    """
    Enum declaration that contains the different tags available to filter the bounding boxes returned by carla.World.get_level_bbs(). These values correspond to the [semantic tag](ref_sensors.md#semantic-segmentation-camera) that the elements in the scene have.
    """

    Any = auto()
    Bridge = auto()
    Buildings = auto()
    Dynamic = auto()
    Fences = auto()
    Ground = auto()
    GuardRail = auto()
    NONE = auto()
    Other = auto()
    Pedestrians = auto()
    Poles = auto()
    RailTrack = auto()
    RoadLines = auto()
    Roads = auto()
    Sidewalks = auto()
    Sky = auto()
    Static = auto()
    Terrain = auto()
    TrafficLight = auto()
    TrafficSigns = auto()
    Vegetation = auto()
    Vehicles = auto()
    Walls = auto()
    Water = auto()

class CollisionEvent:
    """
    Class that defines a collision data for <b>sensor.other.collision</b>. The sensor creates one of this for every collision detected which may be many for one simulation step. Learn more about this [here](ref_sensors.md#collision-detector).
    """
    @property
    def actor(self) -> Actor:
        """
        The actor the sensor is attached to, the one that measured the collision.
        """
    @property
    def normal_impulse(self) -> Vector3D:
        """
        Normal impulse resulting of the collision.
        """
    @property
    def other_actor(self) -> Actor:
        """
        The second actor involved in the collision.
        """

class ColorConverter(IntEnum):
    """
    Class that defines conversion patterns that can be applied to a carla.Image in order to show information provided by carla.Sensor. Depth conversions cause a loss of accuracy, as sensors detect depth as <b>float</b> that is then converted to a grayscale value between 0 and 255. Take a look at the snipet in carla.Sensor.listen to see an example of how to create and save image data for <b>sensor.camera.semantic_segmentation</b>.
    """

    CityScapesPalette = auto()
    Depth = auto()
    LogarithmicDepth = auto()
    Raw = auto()

class DVSEvent:
    """
    Class that defines a DVS event. An event is a quadruple, so a tuple of 4 elements, with `x`, `y` pixel coordinate location, timestamp `t` and polarity `pol` of the event. Learn more about them [here](ref_sensors.md).
    """
    def __str__(self) -> str: ...
    @property
    def pol(self) -> bool:
        """
        Polarity of the event. __True__ for positive and __False__ for negative.
        """
    @property
    def t(self) -> int:
        """
        Timestamp of the moment the event happened.
        """
    @property
    def x(self) -> int:
        """
        X pixel coordinate.
        """
    @property
    def y(self) -> int:
        """
        Y pixel coordinate.
        """

class DVSEventArray:
    """
    Class that defines a stream of events in carla.DVSEvent. Such stream is an array of arbitrary size depending on the number of events. This class also stores the field of view, the height and width of the image and the timestamp from convenience. Learn more about them [here](ref_sensors.md).
    """
    def __getitem__(self, pos: int): ...
    def __iter__(self):
        """
        Iterate over the carla.DVSEvent retrieved as data.
        """
    def __len__(self) -> int: ...
    def __setitem__(self, pos: int, color: Color): ...
    def __str__(self) -> str: ...
    def to_array(self):
        """
        Converts the stream of events to an array of int values in the following order <code>[x, y, t, pol]</code>.
        """
    def to_array_pol(self):
        """
        Returns an array with the polarity of all the events in the stream.
        """
    def to_array_t(self):
        """
        Returns an array with the timestamp of all the events in the stream.
        """
    def to_array_x(self):
        """
        Returns an array with X pixel coordinate of all the events in the stream.
        """
    def to_array_y(self):
        """
        Returns an array with Y pixel coordinate of all the events in the stream.
        """
    def to_image(self):
        """
        Converts the image following this pattern: blue indicates positive events, red indicates negative events.
        """
    @property
    def fov(self) -> float:
        """
        Horizontal field of view of the image.
        """
    @property
    def height(self) -> int:
        """
        Image height in pixels.
        """
    @property
    def raw_data(self) -> bytes: ...
    @property
    def width(self) -> int:
        """
        Image width in pixels.
        """

class GBufferTextureID(IntEnum):
    """
    Defines the identifiers of each GBuffer texture (See the method `carla.Sensor.listen_to_gbuffer`).
    """

    CustomDepth = auto()
    CustomStencil = auto()
    GBufferA = auto()
    GBufferB = auto()
    GBufferC = auto()
    GBufferD = auto()
    GBufferE = auto()
    GBufferF = auto()
    SSAO = auto()
    SceneColor = auto()
    SceneDepth = auto()
    SceneStencil = auto()
    Velocity = auto()

class GnssMeasurement:
    """
    Class that defines the Gnss data registered by a <b>sensor.other.gnss</b>. It essentially reports its position with the position of the sensor and an OpenDRIVE geo-reference.
    """
    def __str__(self) -> str: ...
    @property
    def altitude(self) -> float:
        """
        Height regarding ground level.
        """
    @property
    def latitude(self) -> float:
        """
        North/South value of a point on the map.
        """
    @property
    def longitude(self) -> float:
        """
        West/East value of a point on the map.
        """

class IMUMeasurement:
    """
    Class that defines the data registered by a <b>sensor.other.imu</b>, regarding the sensor's transformation according to the current carla.World. It essentially acts as accelerometer, gyroscope and compass.
    """
    def __str__(self) -> str: ...
    @property
    def accelerometer(self) -> Vector3D:
        """
        Linear acceleration.
        """
    @property
    def compass(self) -> float:
        """
        Orientation with regard to the North ([0.0, -1.0, 0.0] in Unreal Engine).
        """
    @property
    def gyroscope(self) -> Vector3D:
        """
        Angular velocity.
        """

class Image:
    """
    Class that defines an image of 32-bit BGRA colors that will be used as initial data retrieved by camera sensors. There are different camera sensors (currently three, RGB, depth and semantic segmentation) and each of these makes different use for the images. Learn more about them [here](ref_sensors.md).
    """
    def __getitem__(self, pos: int): ...
    def __iter__(self):
        """
        Iterate over the carla.Color that form the image.
        """
    def __len__(self) -> int: ...
    def __setitem__(self, pos: int, color: Color): ...
    def __str__(self) -> str: ...
    def convert(self, color_converter: ColorConverter):
        """
        Converts the image following the `color_converter` pattern.
        """
    def save_to_disk(self, path: str, color_converter: ColorConverter):
        """
        Saves the image to disk using a converter pattern stated as `color_converter`. The default conversion pattern is <b>Raw</b> that will make no changes to the image.
        """
    @property
    def fov(self) -> float:
        """
        Horizontal field of view of the image.
        """
    @property
    def height(self) -> int:
        """
        Image height in pixels.
        """
    @property
    def raw_data(self) -> bytes: ...
    @property
    def width(self) -> int:
        """
        Image width in pixels.
        """

class LaneInvasionEvent:
    """
    Class that defines lanes invasion for <b>sensor.other.lane_invasion</b>. It works only client-side and is dependant on OpenDRIVE to provide reliable information. The sensor creates one of this every time there is a lane invasion, which may be more than once per simulation step. Learn more about this [here](ref_sensors.md#lane-invasion-detector).
    """
    def __str__(self) -> str: ...
    @property
    def actor(self) -> Actor:
        """
        Gets the actor the sensor is attached to, the one that invaded another lane.
        """
    @property
    def crossed_lane_markings(self) -> list[LaneMarking]:
        """
        List of lane markings that have been crossed and detected by the sensor.
        """

class LidarDetection:
    """
    Data contained inside a carla.LidarMeasurement. Each of these represents one of the points in the cloud with its location and its asociated intensity.
    """
    def __str__(self) -> str: ...
    @property
    def intensity(self) -> float:
        """
        Computed intensity for this point as a scalar value between [0.0 , 1.0].
        """
    @property
    def point(self) -> Location:
        """
        Point in xyz coordinates.
        """

class LidarMeasurement:
    """
    Class that defines the LIDAR data retrieved by a <b>sensor.lidar.ray_cast</b>. This essentially simulates a rotating LIDAR using ray-casting. Learn more about this [here](ref_sensors.md#lidar-raycast-sensor).
    """
    def __getitem__(self, pos: int): ...
    def __iter__(self):
        """
        Iterate over the carla.LidarDetection retrieved as data.
        """
    def __len__(self) -> int: ...
    def __setitem__(self, pos: int, detection: LidarDetection): ...
    def __str__(self) -> str: ...
    def get_point_count(self, channel: int):
        """
        Retrieves the number of points sorted by channel that are generated by this measure. Sorting by channel allows to identify the original channel for every point.
        """
    def save_to_disk(self, path: str):
        """
        Saves the point cloud to disk as a <b>.ply</b> file describing data from 3D scanners. The files generated are ready to be used within [MeshLab](http://www.meshlab.net/), an open source system for processing said files. Just take into account that axis may differ from Unreal Engine and so, need to be reallocated.
        """
    @property
    def channels(self) -> int:
        """
        Number of lasers shot.
        """
    @property
    def horizontal_angle(self) -> float:
        """
        Horizontal angle the LIDAR is rotated at the time of the measurement.
        """
    @property
    def raw_data(self) -> bytes:
        """
        Received list of 4D points. Each point consists of [x,y,z] coordiantes plus the intensity computed for that point.
        """

class ObstacleDetectionEvent:
    """
    Class that defines the obstacle data for <b>sensor.other.obstacle</b>. Learn more about this [here](ref_sensors.md#obstacle-detector).
    """
    def __str__(self) -> str: ...
    @property
    def actor(self) -> Actor:
        """
        The actor the sensor is attached to.
        """
    @property
    def distance(self) -> float:
        """
        Distance between `actor` and `other`.
        """
    @property
    def other_actor(self) -> Actor:
        """
        The actor or object considered to be an obstacle.
        """

class OpticalFlowImage:
    """
    Class that defines an optical flow image of 2-Dimension float (32-bit) vectors representing the optical flow detected in the field of view. The components of the vector represents the displacement of an object in the image plane. Each component outputs values in the normalized range [-2,2] which scales to [-2 size, 2 size] with size being the total resolution in the corresponding component.
    """
    def __getitem__(self, pos: int): ...
    def __iter__(self):
        """
        Iterate over the carla.OpticalFlowPixel that form the image.
        """
    def __len__(self) -> int: ...
    def __setitem__(self, pos: int, color: Color): ...
    def __str__(self) -> str: ...
    def get_color_coded_flow(self) -> Image:
        """
        Visualization helper. Converts the optical flow image to an RGB image.
        """
    @property
    def fov(self) -> float:
        """
        Horizontal field of view of the image.
        """
    @property
    def height(self) -> int:
        """
        Image height in pixels.
        """
    @property
    def raw_data(self) -> bytes: ...
    @property
    def width(self) -> int:
        """
        Image width in pixels.
        """

class RadarDetection:
    """
    Data contained inside a carla.RadarMeasurement. Each of these represents one of the points in the cloud that a <b>sensor.other.radar</b> registers and contains the distance, angle and velocity in relation to the radar.
    """
    def __str__(self) -> str: ...
    @property
    def altitude(self) -> float:
        """
        Altitude angle of the detection.
        """
    @property
    def azimuth(self) -> float:
        """
        Azimuth angle of the detection.
        """
    @property
    def depth(self) -> float:
        """
        Distance from the sensor to the detection position.
        """
    @property
    def velocity(self) -> float:
        """
        The velocity of the detected object towards the sensor.
        """

class RadarMeasurement:
    """
    Class that defines and gathers the measures registered by a <b>sensor.other.radar</b>, representing a wall of points in front of the sensor with a distance, angle and velocity in relation to it. The data consists of a carla.RadarDetection array. Learn more about this [here](ref_sensors.md#radar-sensor).
    """
    def __getitem__(self, pos: int): ...
    def __iter__(self):
        """
        Iterate over the carla.RadarDetection retrieved as data.
        """
    def __len__(self) -> int: ...
    def __setitem__(self, pos: int, detection: RadarDetection): ...
    def __str__(self) -> str: ...
    def get_detection_count(self):
        """
        Retrieves the number of entries generated, same as **<font color="#7fb800">\\__str__()</font>**.
        """
    @property
    def raw_data(self) -> bytes:
        """
        The complete information of the carla.RadarDetection the radar has registered.
        """

class RssActorConstellationData:
    """
    Data structure that is provided within the callback registered by RssSensor.register_actor_constellation_callback().
    """
    def __str__(self) -> str: ...
    @property
    def ego_dynamics_on_route(self) -> RssEgoDynamicsOnRoute:
        """
        Current ego vehicle dynamics regarding the route.
        """
    @property
    def ego_match_object(self) -> Object:
        """
        The ego map matched information.
        """
    @property
    def ego_route(self) -> FullRoute:
        """
        The ego route.
        """
    @property
    def other_actor(self) -> Actor:
        """
        The other actor. This is 'None' in case of query of default parameters or articial objects of kind <a href="https://intel.github.io/ad-rss-lib/doxygen/ad_rss/namespacead_1_1rss_1_1world.html#a6432f1ef8d0657b4f21ed5966aca1625">ad.rss.world.ObjectType.ArtificialObject</a> with no dedicated 'carla.Actor' (as e.g. for the [road boundaries](ref_sensors.md#rss-sensor) at the moment)
        """
    @property
    def other_match_object(self) -> Object:
        """
        The other object's map matched information. This is only valid if 'other_actor' is not 'None'.
        """

class RssActorConstellationResult:
    """
    Data structure that should be returned by the callback registered by RssSensor.register_actor_constellation_callback().
    """
    def __str__(self) -> str: ...
    @property
    def actor_dynamics(self) -> RssDynamics:
        """
        The RSS dynamics to be applied for the actor.
        """
    @property
    def actor_object_type(self) -> ObjectType:
        """
        The RSS object type to be used for the actor.
        """
    @property
    def ego_vehicle_dynamics(self) -> RssDynamics:
        """
        The RSS dynamics to be applied for the ego vehicle.
        """
    @property
    def restrict_speed_limit_mode(self) -> RestrictSpeedLimitMode:
        """
        The mode for restricting speed limit.
        """
    @property
    def rss_calculation_mode(self) -> RssMode:
        """
        The calculation mode to be applied with the actor.
        """

class RssEgoDynamicsOnRoute:
    """
    Part of the data contained inside a carla.RssResponse describing the state of the vehicle. The parameters include its current dynamics, and how it is heading regarding the target route.
    """
    def __str__(self) -> str: ...
    @property
    def avg_route_accel_lat(self) -> Acceleration:
        """
        The ego vehicle's acceleration component _lat_ regarding the route smoothened by an average filter.
        """
    @property
    def avg_route_accel_lon(self) -> Acceleration:
        """
        The ego acceleration component _lon_ regarding the route smoothened by an average filter.
        """
    @property
    def crossing_border(self) -> bool:
        """
        States if the vehicle is already crossing one of the lane borders.
        """
    @property
    def ego_center(self) -> ENUPoint:
        """
        The considered enu position of the ego vehicle.
        """
    @property
    def ego_center_within_route(self) -> bool:
        """
        States if the ego vehicle's center is within the route.
        """
    @property
    def ego_heading(self) -> ENUHeading:
        """
        The considered heading of the ego vehicle.
        """
    @property
    def ego_speed(self) -> Speed:
        """
        The ego vehicle's speed.
        """
    @property
    def heading_diff(self) -> ENUHeading:
        """
        The considered heading diff towards the route.
        """
    @property
    def min_stopping_distance(self) -> Distance:
        """
        The current minimum stopping distance.
        """
    @property
    def route_accel_lat(self) -> Acceleration:
        """
        The ego vehicle's acceleration component _lat_ regarding the route.
        """
    @property
    def route_accel_lon(self) -> Acceleration:
        """
        The ego vehicle's acceleration component _lon_ regarding the route.
        """
    @property
    def route_heading(self) -> ENUHeading:
        """
        The considered heading of the route.
        """
    @property
    def route_nominal_center(self) -> ENUPoint:
        """
        The considered nominal center of the current route.
        """
    @property
    def route_speed_lat(self) -> Speed:
        """
        The ego vehicle's speed component _lat_ regarding the route.
        """
    @property
    def route_speed_lon(self) -> Speed:
        """
        The ego vehicle's speed component _lon_ regarding the route.
        """

class RssResponse:
    """
    Class that contains the output of a carla.RssSensor. This is the result of the RSS calculations performed for the parent vehicle of the sensor.

    A carla.RssRestrictor will use the data to modify the carla.VehicleControl of the vehicle.
    """
    def __str__(self) -> str: ...
    @property
    def ego_dynamics_on_route(self) -> RssEgoDynamicsOnRoute:
        """
        Current ego vehicle dynamics regarding the route.
        """
    @property
    def proper_response(self) -> ProperResponse:
        """
        The proper response that the RSS calculated for the vehicle.
        """
    @property
    def response_valid(self) -> bool:
        """
        States if the response is valid. It is __False__ if calculations failed or an exception occured.
        """
    @property
    def rss_state_snapshot(self) -> RssStateSnapshot:
        """
        Detailed RSS states at the current moment in time.
        """
    @property
    def situation_snapshot(self) -> SituationSnapshot:
        """
        Detailed RSS situations extracted from the world model.
        """
    @property
    def world_model(self) -> WorldModel:
        """
        World model used for calculations.
        """

class SemanticLidarDetection:
    """
    Data contained inside a carla.SemanticLidarMeasurement. Each of these represents one of the points in the cloud with its location, the cosine of the incident angle, index of the object hit, and its semantic tag.
    """
    def __str__(self) -> str: ...
    @property
    def cos_inc_angle(self) -> float:
        """
        Cosine of the incident angle between the ray, and the normal of the hit object.
        """
    @property
    def object_idx(self) -> int:
        """
        ID of the actor hit by the ray.
        """
    @property
    def object_tag(self) -> int:
        """
        [Semantic tag](https://carla.readthedocs.io/en/latest/ref_sensors/#semantic-segmentation-camera) of the component hit by the ray.
        """
    @property
    def point(self) -> Location:
        """
        [x,y,z] coordinates of the point.
        """

class SemanticLidarMeasurement:
    """
    Class that defines the semantic LIDAR data retrieved by a <b>sensor.lidar.ray_cast_semantic</b>. This essentially simulates a rotating LIDAR using ray-casting. Learn more about this [here](ref_sensors.md#semanticlidar-raycast-sensor).
    """
    def __getitem__(self, pos: int): ...
    def __iter__(self):
        """
        Iterate over the carla.SemanticLidarDetection retrieved as data.
        """
    def __len__(self) -> int: ...
    def __setitem__(self, pos: int, detection: SemanticLidarDetection): ...
    def __str__(self) -> str: ...
    def get_point_count(self, channel: int):
        """
        Retrieves the number of points sorted by channel that are generated by this measure. Sorting by channel allows to identify the original channel for every point.
        """
    def save_to_disk(self, path: str):
        """
        Saves the point cloud to disk as a <b>.ply</b> file describing data from 3D scanners. The files generated are ready to be used within [MeshLab](http://www.meshlab.net/), an open-source system for processing said files. Just take into account that axis may differ from Unreal Engine and so, need to be reallocated.
        """
    @property
    def channels(self) -> int:
        """
        Number of lasers shot.
        """
    @property
    def horizontal_angle(self) -> float:
        """
        Horizontal angle the LIDAR is rotated at the time of the measurement.
        """
    @property
    def raw_data(self) -> bytes:
        """
        Received list of raw detection points. Each point consists of [x,y,z] coordinates plus the cosine of the incident angle, the index of the hit actor, and its semantic tag.
        """

class SensorData:
    """
    Base class for all the objects containing data generated by a carla.Sensor. This objects should be the argument of the function said sensor is listening to, in order to work with them. Each of these sensors needs for a specific type of sensor data. Hereunder is a list of the sensors and their corresponding data.<br>
      - Cameras (RGB, depth and semantic segmentation): carla.Image.<br>
      - Collision detector: carla.CollisionEvent.<br>
      - GNSS sensor: carla.GnssMeasurement.<br>
      - IMU sensor: carla.IMUMeasurement.<br>
      - Lane invasion detector: carla.LaneInvasionEvent.<br>
      - LIDAR sensor: carla.LidarMeasurement.<br>
      - Obstacle detector: carla.ObstacleDetectionEvent.<br>
      - Radar sensor: carla.RadarMeasurement.<br>
      - RSS sensor: carla.RssResponse.<br>
      - Semantic LIDAR sensor: carla.SemanticLidarMeasurement.
    """
    @property
    def frame(self) -> int:
        """
        Frame count when the data was generated.
        """
    @property
    def timestamp(self) -> float:
        """
        Simulation-time when the data was generated.
        """
    @property
    def transform(self) -> Transform:
        """
        Sensor's transform when the data was generated.
        """
