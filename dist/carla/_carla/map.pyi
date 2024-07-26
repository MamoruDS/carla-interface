from .geom import Transform, GeoLocation, BoundingBox, Location
from enum import IntEnum, auto

class Junction:
    """
    Class that embodies the intersections on the road described in the OpenDRIVE file according to OpenDRIVE 1.4 standards.
    """
    def get_waypoints(self, lane_type: LaneType) -> list[tuple[Waypoint]]:
        """
        Returns a list of pairs of waypoints. Every tuple on the list contains first an initial and then a final waypoint within the intersection boundaries that describe the beginning and the end of said lane along the junction. Lanes follow their OpenDRIVE definitions so there may be many different tuples with the same starting waypoint due to possible deviations, as this are considered different lanes.
        """
    @property
    def bounding_box(self) -> BoundingBox:
        """
        Bounding box encapsulating the junction lanes.
        """
    @property
    def id(self) -> int:
        """
        Identificator found in the OpenDRIVE file.
        """

class Landmark:
    """
    Class that defines any type of traffic landmark or sign affecting a road. These class mediates between the [OpenDRIVE 1.4 standard](http://www.opendrive.org/docs/OpenDRIVEFormatSpecRev1.4H.pdf) definition of the landmarks and their representation in the simulation. This class retrieves all the information defining a landmark in OpenDRIVE and facilitates information about which lanes does it affect and when.
    Landmarks will be accessed by carla.Waypoint objects trying to retrieve the regulation of their lane. Therefore some attributes depend on the waypoint that is consulting the landmark and so, creating the object.
    """
    def get_lane_validities(self) -> list[tuple[int]]:
        """
        Returns which lanes the landmark is affecting to. As there may be specific lanes where the landmark is not effective, the return is a list of pairs containing ranges of the __lane_id__ affected:
        <small>Example: In a road with 5 lanes, being 3 not affected: [(from_lane1,to_lane2),(from_lane4,to_lane5)]</small>
        """
    @property
    def country(self) -> str:
        """
        Country code where the landmark is defined (default to OpenDRIVE is Germany 2017).
        """
    @property
    def distance(self) -> float:
        """
        Distance between the landmark and the waypoint creating the object (querying `get_landmarks` or `get_landmarks_of_type`).
        """
    @property
    def h_offset(self) -> float:
        """
        Orientation offset of the signal relative to the the definition of `road_id` at `s` in OpenDRIVE.
        """
    @property
    def height(self) -> float:
        """
        Total height of the signal.
        """
    @property
    def id(self) -> str:
        """
        Unique ID of the landmark in the OpenDRIVE file.
        """
    @property
    def is_dynamic(self) -> bool:
        """
        Indicates if the landmark has state changes over time such as traffic lights.
        """
    @property
    def name(self) -> str:
        """
        Name of the landmark in the in the OpenDRIVE file.
        """
    @property
    def orientation(self) -> LandmarkOrientation:
        """
        Indicates which lanes the landmark is facing towards to.
        """
    @property
    def pitch(self) -> float:
        """
        Pitch rotation of the signal (Y-axis in [UE coordinates system](https://carla.readthedocs.io/en/latest/python_api/#carlarotation)).
        """
    @property
    def road_id(self) -> int:
        """
        The OpenDRIVE ID of the road where this landmark is defined. Due to OpenDRIVE road definitions, this road may be different from the road the landmark is currently affecting. It is mostly the case in junctions where the road diverges in different routes.
        <small>Example: a traffic light is defined in one of the divergent roads in a junction, but it affects all the possible routes</small>
        """
    @property
    def roll(self) -> float:
        """
        Roll rotation of the signal (X-axis in [UE coordinates system](https://carla.readthedocs.io/en/latest/python_api/#carlarotation)).
        """
    @property
    def s(self) -> float:
        """
        Distance where the landmark is positioned along the geometry of the road `road_id`.
        """
    @property
    def sub_type(self) -> str:
        """
        Subtype identificator of the landmark according to the country code.
        """
    @property
    def t(self) -> float:
        """
        Lateral distance where the landmark is positioned from the edge of the road `road_id`.
        """
    @property
    def text(self) -> str:
        """
        Additional text in the signal.
        """
    @property
    def transform(self) -> Transform:
        """
        The location and orientation of the landmark in the simulation.
        """
    @property
    def type(self) -> str:
        """
        Type identificator of the landmark according to the country code.
        """
    @property
    def unit(self) -> str:
        """
        Units of measurement for the attribute `value`.
        """
    @property
    def value(self) -> float:
        """
        Value printed in the signal (e.g. speed limit, maximum weight, etc).
        """
    @property
    def waypoint(self) -> Waypoint:
        """
        A waypoint placed in the lane of the one that made the query and at the `s` of the landmark. It is the first waypoint for which the landmark will be effective.
        """
    @property
    def width(self) -> float:
        """
        Total width of the signal.
        """
    @property
    def z_offset(self) -> float:
        """
        Height where the landmark is placed.
        """

class LandmarkOrientation(IntEnum):
    """
    Helper class to define the orientation of a landmark in the road. The definition is not directly translated from OpenDRIVE but converted for the sake of understanding.
    """

    Both = auto()
    Negative = auto()
    Positive = auto()

class LandmarkType(IntEnum):
    """
    Helper class containing a set of commonly used landmark types as defined by the default country code in the [OpenDRIVE standard](http://opendrive.org/docs/OpenDRIVEFormatSpecRev1.5M.pdf) (Germany 2017).
    __carla.Landmark does not reference this class__. The landmark type is a string that varies greatly depending on the country code being used. This class only makes it easier to manage some of the most commonly used in the default set by describing them as an enum.
    """

    AbsoluteNoStop = auto()
    AccessForbidden = auto()
    AccessForbiddenBicycle = auto()
    AccessForbiddenHeight = auto()
    AccessForbiddenMotorvehicles = auto()
    AccessForbiddenTrucks = auto()
    AccessForbiddenWeight = auto()
    AccessForbiddenWidth = auto()
    AccessForbiddenWrongDirection = auto()
    CautionBicycle = auto()
    CautionPedestrian = auto()
    CityBegin = auto()
    CityEnd = auto()
    Danger = auto()
    DeadEnd = auto()
    ForbiddenOvertakingMotorvehicles = auto()
    ForbiddenOvertakingTrucks = auto()
    ForbiddenUTurn = auto()
    HasWayNextIntersection = auto()
    Highway = auto()
    LanesMerging = auto()
    LevelCrossing = auto()
    MandatoryLeftRightDirection = auto()
    MandatoryTurnDirection = auto()
    MaximumSpeed = auto()
    PassRightLeft = auto()
    PriorityWay = auto()
    PriorityWayEnd = auto()
    RecomendedSpeed = auto()
    RecomendedSpeedEnd = auto()
    RestrictedStop = auto()
    Roundabout = auto()
    StopSign = auto()
    TwoChoiceTurnDirection = auto()
    YieldSign = auto()

class LaneChange(IntEnum):
    """
    Class that defines the permission to turn either left, right, both or none (meaning only going straight is allowed). This information is stored for every carla.Waypoint according to the OpenDRIVE file. The snipet in carla.Map.get_waypoint shows how a waypoint can be used to learn which turns are permitted.
    """

    Both = auto()
    Left = auto()
    NONE = auto()
    Right = auto()

class LaneMarking:
    """
    Class that gathers all the information regarding a lane marking according to [OpenDRIVE 1.4 standard](http://www.opendrive.org/docs/OpenDRIVEFormatSpecRev1.4H.pdf) standard.
    """
    @property
    def color(self) -> LaneMarkingColor:
        """
        Actual color of the marking.
        """
    @property
    def lane_change(self) -> LaneChange:
        """
        Permissions for said lane marking to be crossed.
        """
    @property
    def type(self) -> LaneMarkingType:
        """
        Lane marking type.
        """
    @property
    def width(self) -> float:
        """
        Horizontal lane marking thickness.
        """

class LaneMarkingColor(IntEnum):
    """
    Class that defines the lane marking colors according to OpenDRIVE 1.4.
    """

    Blue = auto()
    Green = auto()
    Other = auto()
    Red = auto()
    Standard = auto()
    White = auto()
    Yellow = auto()

class LaneMarkingType(IntEnum):
    """
    Class that defines the lane marking types accepted by OpenDRIVE 1.4. The snipet in carla.Map.get_waypoint shows how a waypoint can be used to retrieve the information about adjacent lane markings.   <br><br> __Note on double types:__ Lane markings are defined under the OpenDRIVE standard that determines whereas a line will be considered "BrokenSolid" or "SolidBroken". For each road there is a center lane marking, defined from left to right regarding the lane's directions. The rest of the lane markings are defined in order from the center lane to the closest outside of the road.
    """

    BottsDots = auto()
    Broken = auto()
    BrokenBroken = auto()
    BrokenSolid = auto()
    Curb = auto()
    Grass = auto()
    NONE = auto()
    Other = auto()
    Solid = auto()
    SolidBroken = auto()
    SolidSolid = auto()

class LaneType(IntEnum):
    """
    Class that defines the possible lane types accepted by OpenDRIVE 1.4. This standards define the road information. The snipet in carla.Map.get_waypoint makes use of a waypoint to get the current and adjacent lane types.
    """

    Any = auto()
    Bidirectional = auto()
    Biking = auto()
    Border = auto()
    Driving = auto()
    Entry = auto()
    Exit = auto()
    Median = auto()
    NONE = auto()
    OffRamp = auto()
    OnRamp = auto()
    Parking = auto()
    Rail = auto()
    Restricted = auto()
    RoadWorks = auto()
    Shoulder = auto()
    Sidewalk = auto()
    Special1 = auto()
    Special2 = auto()
    Special3 = auto()
    Stop = auto()
    Tram = auto()

class Map:
    """
    Class containing the road information and waypoint managing. Data is retrieved from an OpenDRIVE file that describes the road. A query system is defined which works hand in hand with carla.Waypoint to translate geometrical information from the .xodr to natural world points. CARLA is currently working with [OpenDRIVE 1.4 standard](http://www.opendrive.org/docs/OpenDRIVEFormatSpecRev1.4H.pdf).
    """
    def __init__(self, name: str, xodr_content: str):
        """
        Constructor for this class. Though a map is automatically generated when initializing the world, using this method in no-rendering mode facilitates working with an .xodr without any CARLA server running.
        """
    def __str__(self) -> str: ...
    def generate_waypoints(self, distance: float) -> list[Waypoint]:
        """
        Returns a list of waypoints with a certain distance between them for every lane and centered inside of it. Waypoints are not listed in any particular order. Remember that waypoints closer than 2cm within the same road, section and lane will have the same identificator.
        """
    def get_all_landmarks(self) -> list[Landmark]:
        """
        Returns all the landmarks in the map. Landmarks retrieved using this method have a __null__ waypoint.
        """
    def get_all_landmarks_from_id(self, opendrive_id: str) -> list[Landmark]:
        """
        Returns the landmarks with a certain OpenDRIVE ID. Landmarks retrieved using this method have a __null__ waypoint.
        """
    def get_all_landmarks_of_type(self, type: str) -> list[Landmark]:
        """
        Returns the landmarks of a specific type. Landmarks retrieved using this method have a __null__ waypoint.
        """
    def get_crosswalks(self) -> list[Location]:
        """
        Returns a list of locations with all crosswalk zones in the form of closed polygons. The first point is repeated, symbolizing where the polygon begins and ends.
        """
    def get_landmark_group(self, landmark: Landmark) -> list[Landmark]:
        """
        Returns the landmarks in the same group as the specified landmark (including itself). Returns an empty list if the landmark does not belong to any group.
        """
    def get_spawn_points(self) -> list[Transform]:
        """
        Returns a list of recommendations made by the creators of the map to be used as spawning points for the vehicles. The list includes carla.Transform objects with certain location and orientation. Said locations are slightly on-air in order to avoid Z-collisions, so vehicles fall for a bit before starting their way.
        """
    def get_topology(self) -> list[tuple[Waypoint, Waypoint]]:
        """
        Returns a list of tuples describing a minimal graph of the topology of the OpenDRIVE file. The tuples contain pairs of waypoints located either at the point a road begins or ends. The first one is the origin and the second one represents another road end that can be reached. This graph can be loaded into [NetworkX](https://networkx.github.io/) to work with. Output could look like this: <b>[(w0, w1), (w0, w2), (w1, w3), (w2, w3), (w0, w4)]</b>.
        """
    def get_waypoint(
        self, location: Location, project_to_road: bool, lane_type: LaneType
    ) -> Waypoint:
        """
        Returns a waypoint that can be located in an exact location or translated to the center of the nearest lane. Said lane type can be defined using flags such as `LaneType.Driving & LaneType.Shoulder`.
         The method will return <b>None</b> if the waypoint is not found, which may happen only when trying to retrieve a waypoint for an exact location. That eases checking if a point is inside a certain road, as otherwise, it will return the corresponding waypoint.
        """
    def get_waypoint_xodr(self, road_id: int, lane_id: int, s: float) -> Waypoint:
        """
        Returns a waypoint if all the parameters passed are correct. Otherwise, returns __None__.
        """
    def save_to_disk(self, path):
        """
        Saves the .xodr OpenDRIVE file of the current map to disk.
        """
    def to_opendrive(self) -> str:
        """
        Returns the .xodr OpenDRIVe file of the current map as string.
        """
    def transform_to_geolocation(self, location: Location) -> GeoLocation:
        """
        Converts a given `location`, a point in the simulation, to a carla.GeoLocation, which represents world coordinates. The geographical location of the map is defined inside OpenDRIVE within the tag <b><georeference></b>.
        """
    @property
    def name(self) -> str:
        """
        The name of the map. It corresponds to the .umap from Unreal Engine that is loaded from a CARLA server, which then references to the .xodr road description.
        """

class Waypoint:
    """
    Waypoints in CARLA are described as 3D directed points. They have a carla.Transform which locates the waypoint in a road and orientates it according to the lane. They also store the road information belonging to said point regarding its lane and lane markings.   <br><br> All the information regarding waypoints and the [waypoint API](../../core_map/#navigation-in-carla) is retrieved as provided by the OpenDRIVE file. Once the client asks for the map object to the server, no longer communication will be needed.
    """
    def __str__(self) -> str: ...
    def get_junction(self) -> Junction:
        """
        If the waypoint belongs to a junction this method returns the asociated junction object. Otherwise returns null.
        """
    def get_landmarks(self, distance: float, stop_at_junction: bool) -> list[Landmark]:
        """
        Returns a list of landmarks in the road from the current waypoint until the specified distance.
        """
    def get_landmarks_of_type(
        self, distance: float, type: str, stop_at_junction: bool
    ) -> list[Landmark]:
        """
        Returns a list of landmarks in the road of a specified type from the current waypoint until the specified distance.
        """
    def get_left_lane(self) -> Waypoint:
        """
        Generates a Waypoint at the center of the left lane based on the direction of the current Waypoint, taking into account if the lane change is allowed in this location.
        Will return <b>None</b> if the lane does not exist
        """
    def get_right_lane(self) -> Waypoint:
        """
        Generates a waypoint at the center of the right lane based on the direction of the current waypoint, taking into account if the lane change is allowed in this location.
        Will return <b>None</b> if the lane does not exist.
        """
    def next(self, distance: float) -> list[Waypoint]:
        """
        Returns a list of waypoints at a certain approximate `distance` from the current one. It takes into account the road and its possible deviations without performing any lane change and returns one waypoint per option.
        The list may be empty if the lane is not connected to any other at the specified distance.
        """
    def next_until_lane_end(self, distance: float) -> list[Waypoint]:
        """
        Returns a list of waypoints from this to the end of the lane separated by a certain `distance`.
        """
    def previous(self, distance: float) -> list[Waypoint]:
        """
        This method does not return the waypoint previously visited by an actor, but a list of waypoints at an approximate `distance` but in the opposite direction of the lane. Similarly to **<font color="#7fb800">next()</font>**, it takes into account the road and its possible deviations without performing any lane change and returns one waypoint per option.
        The list may be empty if the lane is not connected to any other at the specified distance.
        """
    def previous_until_lane_start(self, distance: float) -> list[Waypoint]:
        """
        Returns a list of waypoints from this to the start of the lane separated by a certain `distance`.
        """
    @property
    def id(self) -> int:
        """
        The identificator is generated using a hash combination of the <b>road</b>, <b>section</b>, <b>lane</b> and <b>s</b> values that correspond to said point in the OpenDRIVE geometry. The <b>s</b> precision is set to 2 centimeters, so 2 waypoints closer than 2 centimeters in the same road, section and lane, will have the same identificator.
        """
    @property
    def is_junction(self) -> bool:
        """
        <b>True</b> if the current Waypoint is on a junction as defined by OpenDRIVE.
        """
    @property
    def lane_change(self) -> LaneChange:
        """
        Lane change definition of the current Waypoint's location, based on the traffic rules defined in the OpenDRIVE file. It states if a lane change can be done and in which direction.
        """
    @property
    def lane_id(self) -> int:
        """
        OpenDRIVE lane's id, this value can be positive or negative which represents the direction of the current lane with respect to the road. For more information refer to OpenDRIVE [documentation](http://www.opendrive.org/docs/OpenDRIVEFormatSpecRev1.4H.pdf#page=20)
        """
    @property
    def lane_type(self) -> LaneType:
        """
        The lane type of the current Waypoint, based on OpenDRIVE 1.4 standard.
        """
    @property
    def lane_width(self) -> float:
        """
        Horizontal size of the road at current <b>s</b>.
        """
    @property
    def left_lane_marking(self) -> LaneMarking:
        """
        The left lane marking information based on the direction of the Waypoint.
        """
    @property
    def right_lane_marking(self) -> LaneMarking:
        """
        The right lane marking information based on the direction of the Waypoint.
        """
    @property
    def road_id(self) -> int:
        """
        OpenDRIVE road's id.
        """
    @property
    def s(self) -> float:
        """
        OpenDRIVE <b>s</b> value of the current position.
        """
    @property
    def section_id(self) -> int:
        """
        OpenDRIVE section's id, based on the order that they are originally defined.
        """
    @property
    def transform(self) -> Transform:
        """
        Position and orientation of the waypoint according to the current lane information. This data is computed the first time it is accessed. It is not created right away in order to ease computing costs when lots of waypoints are created but their specific transform is not needed.
        """
