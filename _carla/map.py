# https://github.com/carla-simulator/carla/blob/master/PythonAPI/carla/source/libcarla/Map.cpp
from __future__ import annotations
from ._c.road import JuncId, LaneId, RoadId, SectionId
from .geom import BoundingBox, GeoLocation, Location, Transform
from enum import Enum, IntEnum
from typing import Any, List, Optional, Tuple


# https://github.com/carla-simulator/carla/blob/master/LibCarla/source/carla/road/Lane.h#L29
class LaneType(IntEnum):
    NONE = 0x1
    Driving = 0x1 << 1
    Stop = 0x1 << 2
    Shoulder = 0x1 << 3
    Biking = 0x1 << 4
    Sidewalk = 0x1 << 5
    Border = 0x1 << 6
    Restricted = 0x1 << 7
    Parking = 0x1 << 8
    Bidirectional = 0x1 << 9
    Median = 0x1 << 10
    Special1 = 0x1 << 11
    Special2 = 0x1 << 12
    Special3 = 0x1 << 13
    RoadWorks = 0x1 << 14
    Tram = 0x1 << 15
    Rail = 0x1 << 16
    Entry = 0x1 << 17
    Exit = 0x1 << 18
    OffRamp = 0x1 << 19
    OnRamp = 0x1 << 20
    Any = -2 // 0xFFFFFFFE


# https://github.com/carla-simulator/carla/blob/master/LibCarla/source/carla/road/element/LaneMarking.h#L49
class LaneChange(IntEnum):
    NONE = 0x00
    Right = 0x01
    Left = 0x02
    Both = 0x03


# https://github.com/carla-simulator/carla/blob/master/LibCarla/source/carla/road/element/LaneMarking.h#L38
class LaneMarkingColor(IntEnum):
    Standard = 0
    Blue = 1
    Green = 2
    Red = 3
    White = Standard
    Yellow = 4
    Other = 5


class LaneMarkingType(IntEnum):
    NONE = 10
    Other = 0
    Broken = 1
    Solid = 2
    SolidSolid = 3
    SolidBroken = 4
    BrokenSolid = 5
    BrokenBroken = 6
    BottsDots = 7
    Grass = 8
    Curb = 9


class LandmarkOrientation(IntEnum):
    Positive = 0
    Negative = 1
    Both = 2


TopologyList = List[Tuple["WayPoint", "WayPoint"]]


class Map:
    def __init__(self, name: str, xodr_content: str) -> None:
        raise NotImplementedError

    @property
    def name(self) -> str:
        raise NotImplementedError

    def get_spawn_points(
        self,
    ) -> List[Transform]:
        raise NotImplementedError

    def get_waypoint(
        self,
        location: Location,
        project_to_road: bool = True,
        lane_type: LaneType = LaneType.Driving,
    ) -> WayPoint:
        raise NotImplementedError

    def get_waypoint_xodr(
        self, road_id: RoadId, lane_id: LaneId, s: float
    ) -> WayPoint:
        raise NotImplementedError

    def get_topology(self) -> TopologyList:  # TODO: verify
        raise NotImplementedError

    def generate_waypoints(self, distance: float) -> List[WayPoint]:
        raise NotImplementedError

    def transform_to_geolocation(self, location: Location) -> GeoLocation:
        raise NotImplementedError

    def to_opendrive(self) -> str:
        raise NotImplementedError

    def save_to_disk(self, path: str = "") -> None:
        raise NotImplementedError

    def get_crosswalks(self) -> List[Location]:
        """
        Returns a pair of waypoints (start and end) for each lane in the
        junction
        """
        raise NotImplementedError

    def get_all_landmarks(self) -> List[LandMark]:
        """
        Returns all the larndmarks in the map
        """
        raise NotImplementedError

    def get_all_landmarks_from_id(self, opendrive_id: str) -> List[LandMark]:
        """
        Returns all the larndmarks in the map with a specific OpenDRIVE id
        """
        raise NotImplementedError

    def get_all_landmarks_of_type(self, type: LandMarkType) -> List[LandMark]:
        """
        Returns all the landmarks in the map of a specific type
        """
        raise NotImplementedError

    def get_landmark_group(self, landmark: LandMark) -> List[LandMark]:
        """
        Returns all the landmarks in the same group including this one
        """
        raise NotImplementedError

    def cook_in_memory_map(self, path: str = "") -> None:
        """
        Cooks InMemoryMap used by the traffic manager
        """
        raise NotImplementedError

    def __str__(self) -> str:
        raise NotImplementedError


class LaneMarking:
    @property
    def type(self) -> LaneMarkingType:
        raise NotImplementedError

    @type.setter
    def type(self, val: LaneMarkingType) -> None:
        raise NotImplementedError

    @property
    def color(self) -> LaneMarkingColor:
        raise NotImplementedError

    @color.setter
    def color(self, val: LaneMarkingColor) -> None:
        raise NotImplementedError

    @property
    def lane_change(self) -> LaneChange:
        raise NotImplementedError

    @lane_change.setter
    def lane_change(self, val: LaneChange) -> None:
        raise NotImplementedError

    @property
    def width(self) -> float:
        raise NotImplementedError

    @width.setter
    def width(self, val: float) -> None:
        raise NotImplementedError


class WayPoint:
    @property
    def id(self) -> int:
        raise NotImplementedError

    @id.setter
    def id(self, val: int) -> None:
        raise NotImplementedError

    @property
    def transform(self) -> Transform:
        raise NotImplementedError

    @transform.setter
    def transform(self, val: Transform) -> None:
        raise NotImplementedError

    @property
    def is_intersection(self) -> bool:
        """deprecated; using `WayPoint.is_junction`"""
        raise NotImplementedError

    @is_intersection.setter
    def is_intersection(self, val: bool) -> None:
        """deprecated; using `WayPoint.is_junction`"""
        raise NotImplementedError

    @property
    def is_junction(self) -> bool:
        raise NotImplementedError

    @is_junction.setter
    def is_junction(self, val: bool) -> None:
        raise NotImplementedError

    @property
    def lane_width(self) -> float:
        raise NotImplementedError

    @lane_width.setter
    def lane_width(self, val: float) -> None:
        raise NotImplementedError

    @property
    def road_id(self) -> RoadId:
        raise NotImplementedError

    @road_id.setter
    def road_id(self, val: RoadId) -> None:
        raise NotImplementedError

    @property
    def section_id(self) -> SectionId:
        raise NotImplementedError

    @section_id.setter
    def section_id(self, val: SectionId) -> None:
        raise NotImplementedError

    @property
    def lane_id(self) -> LaneId:
        raise NotImplementedError

    @lane_id.setter
    def lane_id(self, val: LaneId) -> None:
        raise NotImplementedError

    @property
    def s(self) -> float:
        """distance"""
        raise NotImplementedError

    @s.setter
    def s(self, val: float) -> None:
        """distance"""
        raise NotImplementedError

    @property
    def junction_id(self) -> JuncId:
        raise NotImplementedError

    @junction_id.setter
    def junction_id(self, val: JuncId) -> None:
        raise NotImplementedError

    @property
    def lane_change(self) -> LaneChange:
        raise NotImplementedError

    @lane_change.setter
    def lane_change(self, val: LaneChange) -> None:
        raise NotImplementedError

    @property
    def lane_type(self) -> LaneType:
        raise NotImplementedError

    @lane_type.setter
    def lane_type(self, val: LaneType) -> None:
        raise NotImplementedError

    @property
    def right_lane_marking(self) -> Optional[LaneMarking]:
        raise NotImplementedError

    @right_lane_marking.setter
    def right_lane_marking(self, val: Optional[LaneMarking]) -> None:
        raise NotImplementedError

    @property
    def left_lane_marking(self) -> Optional[LaneMarking]:
        raise NotImplementedError

    @left_lane_marking.setter
    def left_lane_marking(self, val: Optional[LaneMarking]) -> None:
        raise NotImplementedError

    def next(self, distance: float) -> List[WayPoint]:
        raise NotImplementedError

    def previous(self, distance: float) -> List[WayPoint]:
        raise NotImplementedError

    def next_until_lane_end(self, distance: float) -> List[WayPoint]:
        """
        Returns a list of waypoints separated by distance from the current waypoint
        to the end of the lane
        """
        raise NotImplementedError

    def previous_until_lane_start(self, distance: float) -> List[WayPoint]:
        """
        Returns a list of waypoints separated by distance from the current waypoint
        to the start of the lane
        """
        raise NotImplementedError

    def get_right_lane(self) -> WayPoint:
        raise NotImplementedError

    def get_left_lane(self) -> WayPoint:
        raise NotImplementedError

    def get_junction(self) -> Junction:
        raise NotImplementedError

    def get_landmarks(
        self, distance: float, stop_at_junction: bool = False
    ) -> List[LandMark]:
        raise NotImplementedError

    def get_landmarks_of_type(
        self, distance: float, type: str, stop_at_junction: bool = False
    ) -> List[LandMark]:
        """
        Returns a list of landmarks from the current position to a certain distance
        Filters by specified type
        """
        raise NotImplementedError

    def __str__(self) -> str:
        raise NotImplementedError


class Junction:
    @property
    def id(self) -> JuncId:
        raise NotImplementedError

    @id.setter
    def id(self, val: JuncId) -> None:
        raise NotImplementedError

    @property
    def bounding_box(self) -> BoundingBox:
        raise NotImplementedError

    @bounding_box.setter
    def bounding_box(self, val: BoundingBox) -> None:
        raise NotImplementedError

    def get_waypoints(self) -> List[Tuple[WayPoint, WayPoint]]:
        raise NotImplementedError


# https://github.com/carla-simulator/carla/blob/master/LibCarla/source/carla/road/SignalType.h
class LandMarkType(Enum):
    Danger = "101"
    LanesMerging = "121"
    CautionPedestrian = "133"
    CautionBicycle = "138"
    LevelCrossing = "150"
    StopSign = "206"
    YieldSign = "205"
    MandatoryTurnDirection = "209"
    MandatoryLeftRightDirection = "211"
    TwoChoiceTurnDirection = "214"
    Roundabout = "215"
    PassRightLeft = "222"
    AccessForbidden = "250"
    AccessForbiddenMotorvehicles = "251"
    AccessForbiddenTrucks = "253"
    AccessForbiddenBicycle = "254"
    AccessForbiddenWeight = "263"
    AccessForbiddenWidth = "264"
    AccessForbiddenHeight = "265"
    AccessForbiddenWrongDirection = "267"
    ForbiddenUTurn = "272"
    MaximumSpeed = "274"
    ForbiddenOvertakingMotorvehicles = "276"
    ForbiddenOvertakingTrucks = "277"
    AbsoluteNoStop = "283"
    RestrictedStop = "286"
    HasWayNextIntersection = "301"
    PriorityWay = "306"
    PriorityWayEnd = "307"
    CityBegin = "310"
    CityEnd = "311"
    Highway = "330"
    DeadEnd = "357"
    RecomendedSpeed = "380"
    RecomendedSpeedEnd = "381"


class LandMark:
    @property
    def road_id(self) -> RoadId:
        raise NotImplementedError

    @road_id.setter
    def road_id(self, val: RoadId) -> None:
        raise NotImplementedError

    @property
    def distance(self) -> float:
        raise NotImplementedError

    @distance.setter
    def distance(self, val: float) -> None:
        raise NotImplementedError

    @property
    def s(self) -> float:
        raise NotImplementedError

    @s.setter
    def s(self, val: float) -> None:
        raise NotImplementedError

    @property
    def t(self) -> float:
        raise NotImplementedError

    @t.setter
    def t(self, val: float) -> None:
        raise NotImplementedError

    @property
    def id(self) -> str:
        raise NotImplementedError

    @id.setter
    def id(self, val: str) -> None:
        raise NotImplementedError

    @property
    def name(self) -> str:
        raise NotImplementedError

    @name.setter
    def name(self, val: str) -> None:
        raise NotImplementedError

    @property
    def is_dynamic(self) -> bool:
        raise NotImplementedError

    @is_dynamic.setter
    def is_dynamic(self, val: bool) -> None:
        raise NotImplementedError

    @property
    # def orientation(self) -> SignalOrientation:
    def orientation(self) -> Any:
        raise NotImplementedError

    @orientation.setter
    def orientation(self, val: Any) -> None:
        raise NotImplementedError

    @property
    def z_offset(self) -> float:
        raise NotImplementedError

    @z_offset.setter
    def z_offset(self, val: float) -> None:
        raise NotImplementedError

    @property
    def country(self) -> str:
        raise NotImplementedError

    @country.setter
    def country(self, val: str) -> None:
        raise NotImplementedError

    @property
    def type(self) -> str:
        raise NotImplementedError

    @type.setter
    def type(self, val: str) -> None:
        raise NotImplementedError

    @property
    def sub_type(self) -> str:
        raise NotImplementedError

    @sub_type.setter
    def sub_type(self, val: str) -> None:
        raise NotImplementedError

    @property
    def value(self) -> float:
        raise NotImplementedError

    @value.setter
    def value(self, val: float) -> None:
        raise NotImplementedError

    @property
    def unit(self) -> str:
        raise NotImplementedError

    @unit.setter
    def unit(self, val: str) -> None:
        raise NotImplementedError

    @property
    def height(self) -> float:
        raise NotImplementedError

    @height.setter
    def height(self, val: float) -> None:
        raise NotImplementedError

    @property
    def width(self) -> float:
        raise NotImplementedError

    @width.setter
    def width(self, val: float) -> None:
        raise NotImplementedError

    @property
    def text(self) -> str:
        raise NotImplementedError

    @text.setter
    def text(self, val: str) -> None:
        raise NotImplementedError

    @property
    def h_offset(self) -> float:
        raise NotImplementedError

    @h_offset.setter
    def h_offset(self, val: float) -> None:
        raise NotImplementedError

    @property
    def pitch(self) -> float:
        raise NotImplementedError

    @pitch.setter
    def pitch(self, val: float) -> None:
        raise NotImplementedError

    @property
    def roll(self) -> float:
        raise NotImplementedError

    @roll.setter
    def roll(self, val: float) -> None:
        raise NotImplementedError

    @property
    def waypoint(self) -> WayPoint:
        raise NotImplementedError

    @waypoint.setter
    def waypoint(self, val: WayPoint) -> None:
        raise NotImplementedError

    @property
    def transform(self) -> Transform:
        raise NotImplementedError

    @transform.setter
    def transform(self, val: Transform) -> None:
        raise NotImplementedError

    def get_lane_validities(self) -> List[Any]:  # TODO
        raise NotImplementedError
