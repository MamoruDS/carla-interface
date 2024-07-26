class Osm2Odr:
    """
    Class that converts an OpenStreetMap map to OpenDRIVE format, so that it can be loaded in CARLA. Find out more about this feature in the [docs](tuto_G_openstreetmap.md).
    """
    @staticmethod
    def convert(osm_file: str, settings: Osm2OdrSettings) -> str:
        """
        Takes the content of an <code>.osm</code> file (OpenStreetMap format) and returns the content of the <code>.xodr</code> (OpenDRIVE format) describing said map. Some parameterization is passed to do the conversion.
        """

class Osm2OdrSettings:
    """
    Helper class that contains the parameterization that will be used by carla.Osm2Odr to convert an OpenStreetMap map to OpenDRIVE format. Find out more about this feature in the [docs](tuto_G_openstreetmap.md).
    """
    def set_osm_way_types(self, way_types: list[str]):
        """
        Defines the OpenStreetMaps road types that will be imported to OpenDRIVE. By default the road types imported are `motorway, motorway_link, trunk, trunk_link, primary, primary_link, secondary, secondary_link, tertiary, tertiary_link, unclassified, residential`. For a full list of road types check [here](https://wiki.openstreetmap.org/wiki/Main_Page).
        """
    def set_traffic_light_excluded_way_types(self, way_types: list[str]):
        """
        Defines the OpenStreetMaps road types that will not generate traffic lights even if `generate_traffic_lights` is enabled. By default the road types excluded are `motorway_link, primary_link, secondary_link, tertiary_link`
        """
    @property
    def all_junctions_with_traffic_lights(self) -> bool:
        """
        When disabled, the converter will generate traffic light data from the OpenStreetMaps data only. When enabled, all junctions will generate traffic lights.
        """
    @property
    def center_map(self) -> bool:
        """
        When this option is enabled, the geometry of the map will be displaced so that the origin of coordinates matches the center of the bounding box of the entire road map.
        """
    @property
    def default_lane_width(self) -> float:
        """
        Width of the lanes described in the resulting XODR map. Default value is __4.0__.
        """
    @property
    def elevation_layer_height(self) -> float:
        """
        Defines the height separating two different [OpenStreetMap layers](https://wiki.openstreetmap.org/wiki/Key:layer). Default value is __0.0__.
        """
    @property
    def generate_traffic_lights(self) -> bool:
        """
        Indicates wether to generate traffic light data in the OpenDRIVE. Road types defined by `set_traffic_light_excluded_way_types(way_types)` will not generate traffic lights.
        """
    @property
    def offset_x(self) -> float:
        """
        Offset in the X axis.  Default value is __0.0__.
        """
    @property
    def offset_y(self) -> float:
        """
        Offset in the Y axis.  Default value is __0.0__.
        """
    @property
    def proj_string(self) -> str:
        """
        Defines the [proj4](https://github.com/OSGeo/proj.4) string that will be used to compute the projection from geocoordinates to cartesian coordinates. This string will be written in the resulting OpenDRIVE unless the options `use_offsets` or `center_map` are enabled as these options override some of the definitions in the string.
        """
    @property
    def use_offsets(self) -> bool:
        """
        Enables the use of offset for the conversion. The offset will move the origin position of the map. Default value is __False__.
        """
