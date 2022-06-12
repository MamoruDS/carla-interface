# https://github.com/carla-simulator/carla/tree/master/LibCarla/source/carla/trafficmanager
from ..geom import Location
from ..map import WayPoint
from enum import IntEnum
from typing import List, Tuple


TM_DEFAULT_PORT = 8000

# https://github.com/carla-simulator/carla/blob/master/LibCarla/source/carla/trafficmanager/SimpleWaypoint.h#L25
class RoadOption(IntEnum):
    Void = 0
    Left = 1
    Right = 2
    Straight = 3
    LaneFollow = 4
    ChangeLaneLeft = 5
    ChangeLaneRight = 6
    RoadEnd = 7


# https://github.com/carla-simulator/carla/blob/master/LibCarla/source/carla/trafficmanager/LocalizationStage.h
Action = Tuple[RoadOption, WayPoint]
ActionBuffer = List[Action]
Path = List[Location]
Route = List[int]
