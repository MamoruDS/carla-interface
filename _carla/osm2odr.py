# https://github.com/carla-simulator/carla/blob/master/PythonAPI/carla/source/libcarla/OSM2ODR.cpp
from typing import List

Meters = float


class Osm2OdrSettings:
    """
    Helper class that contains the parameterization that will be used by carla.Osm2Odr to convert an OpenStreetMap map to OpenDRIVE format. Find out more about this feature in the [docs](tuto_G_openstreetmap.md).
    """

    def __init__(self) -> None:
        raise NotImplementedError

    @property
    def use_offsets(self) -> bool:
        """
        Enables the use of offset for the conversion. The offset will move the origin position of the map. Default value is __False__.
        """
        raise NotImplementedError

    @property
    def offset_x(self) -> Meters:
        """
        Offset in the X axis.  Default value is 0.0.
        """
        raise NotImplementedError

    @property
    def offset_y(self) -> Meters:
        """
        Offset in the Y axis.  Default value is 0.0.
        """
        raise NotImplementedError

    @property
    def default_lane_width(self) -> Meters:
        """
        Width of the lanes described in the resulting XODR map. Default value is 4.0.
        """
        raise NotImplementedError

    @property
    def elevation_layer_height(self) -> Meters:
        """
        Defines the height separating two different [OpenStreetMap layers](https://wiki.openstreetmap.org/wiki/Key:layer). Default value is 0.0.
        """
        raise NotImplementedError

    @property
    def proj_string(self) -> str:
        """
        Defines the [proj4](https://github.com/OSGeo/proj.4) string that will be used to compute the projection from geocoordinates to cartesian coordinates. This string will be written in the resulting OpenDRIVE unless the options `use_offsets` or `center_map` are enabled as these options override some of the definitions in the string.
        """
        raise NotImplementedError

    @property
    def center_map(self) -> bool:
        """
        When this option is enabled, the geometry of the map will be displaced so that the origin of coordinates matches the center of the bounding box of the entire road map.
        """
        raise NotImplementedError

    @property
    def generate_traffic_lights(self) -> bool:
        raise NotImplementedError

    @property
    def all_junctions_with_traffic_lights(self) -> bool:
        raise NotImplementedError

    def set_osm_way_types(self, way_types: List[str]) -> None:
        """
        Defines the OpenStreetMaps road types that will be imported to OpenDRIVE. By default the road types imported are `motorway, motorway_link, trunk, trunk_link, primary, primary_link, secondary, secondary_link, tertiary, tertiary_link, unclassified, residential`. For a full list of road types check [here](https://wiki.openstreetmap.org/wiki/Main_Page).
        """
        raise NotImplementedError

    def set_traffic_light_excluded_way_types(
        self, way_types: List[str]
    ) -> None:
        """
        Defines the OpenStreetMaps road types that will not generate traffic lights even if `generate_traffic_lights` is enabled. By default the road types excluded are `motorway_link, primary_link, secondary_link, tertiary_link`
        """
        raise NotImplementedError

    def __str__(self) -> str:
        raise NotImplementedError


class Osm2Odr:
    """
    Class that converts an OpenStreetMap map to OpenDRIVE format, so that it can be loaded in CARLA. Find out more about this feature in the [docs](tuto_G_openstreetmap.md).
    """

    @staticmethod
    def convert(
        osm_file: str, settings: Osm2OdrSettings = Osm2OdrSettings()
    ) -> str:
        """
        The converted OpenDRIVE xml data.
        Takes the content of an <code>.osm</code> file (OpenStreetMap format) and returns the content of the <code>.xodr</code> (OpenDRIVE format) describing said map. Some parameterization is passed to do the conversion.
        """
        raise NotImplementedError
