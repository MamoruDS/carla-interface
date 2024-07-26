from enum import IntEnum, auto
from typing_extensions import Self

class ActorAttribute:
    """
    CARLA provides a library of blueprints for actors that can be accessed as carla.BlueprintLibrary. Each of these blueprints has a series of attributes defined internally. Some of these are modifiable, others are not. A list of recommended values is provided for those that can be set.
    """
    def __bool__(self) -> bool: ...
    def __eq__(self, other: Self) -> bool:
        """
        Returns true if this actor's attribute and `other` are the same.
        """
    def __float__(self) -> float: ...
    def __int__(self) -> int: ...
    def __ne__(self, other: Self) -> bool:
        """
        Returns true if this actor's attribute and `other` are different.
        """
    def __nonzero__(self) -> bool:
        """
        Returns true if this actor's attribute is not zero or null.
        """
    def __str__(self) -> str: ...
    def as_bool(self):
        """
        Reads the attribute as boolean value.
        """
    def as_color(self):
        """
        Reads the attribute as carla.Color.
        """
    def as_float(self):
        """
        Reads the attribute as float.
        """
    def as_int(self):
        """
        Reads the attribute as int.
        """
    def as_str(self):
        """
        Reads the attribute as string.
        """
    @property
    def id(self) -> str:
        """
        The attribute's name and identifier in the library.
        """
    @property
    def is_modifiable(self) -> bool:
        """
        It is <b>True</b> if the attribute's value can be modified.
        """
    @property
    def recommended_values(self) -> list[str]:
        """
        A list of values suggested by those who designed the blueprint.
        """
    @property
    def type(self) -> ActorAttributeType:
        """
        The attribute's parameter type.
        """

class ActorAttributeType(IntEnum):
    """
    CARLA provides a library of blueprints for actors in carla.BlueprintLibrary with different attributes each. This class defines the types those at carla.ActorAttribute can be as a series of enum. All this information is managed internally and listed here for a better comprehension of how CARLA works.
    """

    Bool = auto()
    Float = auto()
    Int = auto()
    RGBColor = auto()
    String = auto()

class ActorBlueprint:
    """
    CARLA provides a blueprint library for actors that can be consulted through carla.BlueprintLibrary. Each of these consists of an identifier for the blueprint and a series of attributes that may be modifiable or not. This class is the intermediate step between the library and the actor creation. Actors need an actor blueprint to be spawned. These store the information for said blueprint in an object with its attributes and some tags to categorize them. The user can then customize some attributes and eventually spawn the actors through carla.World.
    """
    def __iter__(self):
        """
        Iterate over the carla.ActorAttribute that this blueprint has.
        """
    def __len__(self) -> int:
        """
        Returns the amount of attributes for this blueprint.
        """
    def __str__(self) -> str: ...
    def get_attribute(self, id: str) -> ActorAttribute:
        """
        Returns the actor's attribute with `id` as identifier if existing.
        """
    def has_attribute(self, id: str) -> bool:
        """
        Returns <b>True</b> if the blueprint contains the attribute `id`.
        """
    def has_tag(self, tag: str) -> bool:
        """
        Returns <b>True</b> if the blueprint has the specified `tag` listed.
        """
    def match_tags(self, wildcard_pattern: str) -> bool:
        """
        Returns <b>True</b> if any of the tags listed for this blueprint matches `wildcard_pattern`. Matching follows [fnmatch](https://docs.python.org/2/library/fnmatch.html) standard.
        """
    def set_attribute(self, id: str, value: str):
        """
        If the `id` attribute is modifiable, changes its value to `value`.
        """
    @property
    def id(self) -> str:
        """
        The identifier of said blueprint inside the library. E.g. `walker.pedestrian.0001`.
        """
    @property
    def tags(self) -> list[str]:
        """
        A list of tags each blueprint has that helps describing them. E.g. `['0001', 'pedestrian', 'walker']`.
        """

class BlueprintLibrary:
    """
    A class that contains the blueprints provided for actor spawning. Its main application is to return carla.ActorBlueprint objects needed to spawn actors. Each blueprint has an identifier and attributes that may or may not be modifiable. The library is automatically created by the server and can be accessed through carla.World.

      [Here](bp_library.md) is a reference containing every available blueprint and its specifics.
    """
    def __getitem__(self, pos: int) -> ActorBlueprint:
        """
        Returns the blueprint stored in `pos` position inside the data structure containing them.
        """
    def __iter__(self):
        """
        Iterate over the carla.ActorBlueprint stored in the library.
        """
    def __len__(self) -> int:
        """
        Returns the amount of blueprints comprising the library.
        """
    def __str__(self) -> str:
        """
        Parses the identifiers for every blueprint to string.
        """
    def filter(self, wildcard_pattern: str) -> BlueprintLibrary:
        """
        Filters a list of blueprints matching the `wildcard_pattern` against the id and tags of every blueprint contained in this library and returns the result as a new one. Matching follows [fnmatch](https://docs.python.org/2/library/fnmatch.html) standard.
        """
    def find(self, id: str) -> ActorBlueprint:
        """
        Returns the blueprint corresponding to that identifier.
        """

class Color:
    """
    Class that defines a 32-bit RGBA color.
    """
    def __eq__(self, other: Self) -> bool: ...
    def __init__(self, r: int, g: int, b: int, a: int):
        """
        Initializes a color, black by default.
        """
    def __ne__(self, other: Self) -> bool: ...
    def __str__(self) -> str: ...
    @property
    def a(self) -> int:
        """
        Alpha channel (0-255).
        """
    @property
    def b(self) -> int:
        """
        Blue color (0-255).
        """
    @property
    def g(self) -> int:
        """
        Green color (0-255).
        """
    @property
    def r(self) -> int:
        """
        Red color (0-255).
        """

class FloatColor:
    """
    Class that defines a float RGBA color.
    """
    def __eq__(self, other: Self) -> bool: ...
    def __init__(self, r: float, g: float, b: float, a: float):
        """
        Initializes a color, black by default.
        """
    def __ne__(self, other: Self) -> bool: ...
    @property
    def a(self) -> float:
        """
        Alpha channel.
        """
    @property
    def b(self) -> float:
        """
        Blue color.
        """
    @property
    def g(self) -> float:
        """
        Green color.
        """
    @property
    def r(self) -> float:
        """
        Red color.
        """

class OpticalFlowPixel:
    """
    Class that defines a 2 dimensional vector representing an optical flow pixel.
    """
    def __eq__(self, other: Self) -> bool: ...
    def __init__(self, x: float, y: float):
        """
        Initializes the Optical Flow Pixel. Zero by default.
        """
    def __ne__(self, other: Self) -> bool: ...
    def __str__(self) -> str: ...
    @property
    def x(self) -> float:
        """
        Optical flow in the x component.
        """
    @property
    def y(self) -> float:
        """
        Optical flow in the y component.
        """
