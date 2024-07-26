from enum import IntEnum, auto

class RoadOption(IntEnum):
    """
    following https://github.com/carla-simulator/carla/blob/master/LibCarla/source/carla/trafficmanager/SimpleWaypoint.h#L25
    """

    ChangeLaneLeft = auto()
    ChangeLaneRight = auto()
    LaneFollow = auto()
    Left = auto()
    Right = auto()
    RoadEnd = auto()
    Straight = auto()
    Void = auto()
