from typing_extensions import Self

class BoundingBox:
    """
    Bounding boxes contain the geometry of an actor or an element in the scene. They can be used by carla.DebugHelper or a carla.Client to draw their shapes for debugging. Check out the snipet in carla.DebugHelper.draw_box where a snapshot of the world is used to draw bounding boxes for traffic lights.
    """
    def __eq__(self, other: Self) -> bool:
        """
        Returns true if both location and extent are equal for this and `other`.
        """
    def __init__(self, location: Location, extent: Vector3D): ...
    def __ne__(self, other: Self) -> bool:
        """
        Returns true if either location or extent are different for this and `other`.
        """
    def __str__(self) -> str:
        """
        Parses the location and extent of the bounding box to string.
        """
    def contains(self, world_point: Location, transform: Transform) -> bool:
        """
        Returns **True** if a point passed in world space is inside this bounding box.
        """
    def get_local_vertices(self) -> list[Location]:
        """
        Returns a list containing the locations of this object's vertices in local space.
        """
    def get_world_vertices(self, transform: Transform) -> list[Location]:
        """
        Returns a list containing the locations of this object's vertices in world space.
        """
    @property
    def extent(self) -> Vector3D:
        """
        Vector from the center of the box to one vertex. The value in each axis equals half the size of the box for that axis.
        `extent.x * 2` would return the size of the box in the X-axis.
        """
    @property
    def location(self) -> Location:
        """
        The center of the bounding box.
        """
    @property
    def rotation(self) -> Rotation:
        """
        The orientation of the bounding box.
        """

class GeoLocation:
    """
    Class that contains geographical coordinates simulated data. The carla.Map can convert simulation locations by using the <b><georeference></b> tag in the OpenDRIVE file.
    """
    def __eq__(self, other: Self) -> bool: ...
    def __init__(self, latitude: float, longitude: float, altitude: float): ...
    def __ne__(self, other: Self) -> bool: ...
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

class Location:
    """
    Represents a spot in the world.
    """
    def __abs__(self) -> Location:
        """
        Returns a Location with the absolute value of the components x, y and z.
        """
    def __eq__(self, other: Self) -> bool:
        """
        Returns __True__ if both locations are the same point in space.
        """
    def __init__(self, x: float, y: float, z: float): ...
    def __ne__(self, other: Self) -> bool:
        """
        Returns __True__ if both locations are different points in space.
        """
    def __str__(self) -> str:
        """
        Parses the axis' values to string.
        """
    def distance(self, location: Location) -> float:
        """
        Returns Euclidean distance from this location to another one.
        """
    @property
    def x(self) -> float:
        """
        Distance from origin to spot on X axis.
        """
    @property
    def y(self) -> float:
        """
        Distance from origin to spot on Y axis.
        """
    @property
    def z(self) -> float:
        """
        Distance from origin to spot on Z axis.
        """

class Rotation:
    """
    Class that represents a 3D rotation and therefore, an orientation in space. CARLA uses the Unreal Engine coordinates system. This is a Z-up left-handed system.  <br>
    <br>The constructor method follows a specific order of declaration: `(pitch, yaw, roll)`, which corresponds to `(Y-rotation,Z-rotation,X-rotation)`.  <br> <br>![UE4_Rotation](https://d26ilriwvtzlb.cloudfront.net/8/83/BRMC_9.jpg) *Unreal Engine's coordinates system*
    """
    def __eq__(self, other: Self) -> bool:
        """
        Returns __True__ if both rotations represent the same orientation for every axis.
        """
    def __init__(self, pitch: float, yaw: float, roll: float): ...
    def __ne__(self, other: Self) -> bool:
        """
        Returns __True__ if both rotations represent the same orientation for every axis.
        """
    def __str__(self) -> str:
        """
        Parses the axis' orientations to string.
        """
    def get_forward_vector(self) -> Vector3D:
        """
        Computes the vector pointing forward according to the rotation of the object.
        """
    def get_right_vector(self) -> Vector3D:
        """
        Computes the vector pointing to the right according to the rotation of the object.
        """
    def get_up_vector(self) -> Vector3D:
        """
        Computes the vector pointing upwards according to the rotation of the object.
        """
    @property
    def pitch(self) -> float:
        """
        Y-axis rotation angle.
        """
    @property
    def roll(self) -> float:
        """
        X-axis rotation angle.
        """
    @property
    def yaw(self) -> float:
        """
        Z-axis rotation angle.
        """

class Transform:
    """
    Class that defines a transformation, a combination of location and rotation, without scaling.
    """
    def __eq__(self, other: Self) -> bool:
        """
        Returns __True__ if both location and rotation are equal for this and `other`.
        """
    def __init__(self, location: Location, rotation: Rotation): ...
    def __ne__(self, other: Self) -> bool:
        """
        Returns __True__ if any location and rotation are not equal for this and `other`.
        """
    def __str__(self) -> str:
        """
        Parses both location and rotation to string.
        """
    def get_forward_vector(self) -> Vector3D:
        """
        Computes a forward vector using the rotation of the object.
        """
    def get_inverse_matrix(self) -> list[list[float]]:
        """
        Computes the 4-matrix representation of the inverse transformation.
        """
    def get_matrix(self) -> list[list[float]]:
        """
        Computes the 4-matrix representation of the transformation.
        """
    def get_right_vector(self) -> Vector3D:
        """
        Computes a right vector using the rotatio of the object.
        """
    def get_up_vector(self) -> Vector3D:
        """
        Computes an up vector using the rotation of the object.
        """
    def transform(self, in_point: Location):
        """
        Translates a 3D point from local to global coordinates using the current transformation as frame of reference.
        """
    @property
    def location(self) -> Location:
        """
        Describes a point in the coordinate system.
        """
    @property
    def rotation(self) -> Rotation:
        """
        Describes a rotation for an object according to Unreal Engine's axis system.
        """

class Vector2D:
    """
    Helper class to perform 2D operations.
    """
    def __add__(self, other: Vector2D): ...
    def __eq__(self, other: Self) -> bool:
        """
        Returns __True__ if values for every axis are equal.
        """
    def __init__(self, x: float, y: float): ...
    def __mul__(self, other: Vector2D): ...
    def __ne__(self, other: Self) -> bool:
        """
        Returns __True__ if the value for any axis is different.
        """
    def __str__(self) -> str:
        """
        Returns the axis values for the vector parsed as string.
        """
    def __sub__(self, other: Vector2D): ...
    def __truediv__(self, other: Vector2D): ...
    def length(self) -> float:
        """
        Computes the length of the vector.
        """
    def make_unit_vector(self) -> Vector3D:
        """
        Returns a vector with the same direction and unitary length.
        """
    def squared_length(self) -> float:
        """
        Computes the squared length of the vector.
        """
    @property
    def x(self) -> float:
        """
        X-axis value.
        """
    @property
    def y(self) -> float:
        """
        Y-axis value.
        """

class Vector3D:
    """
    Helper class to perform 3D operations.
    """
    def __abs__(self) -> Vector3D:
        """
        Returns a Vector3D with the absolute value of the components x, y and z.
        """
    def __add__(self, other: Vector3D): ...
    def __eq__(self, other: Self) -> bool:
        """
        Returns __True__ if values for every axis are equal.
        """
    def __init__(self, x: float, y: float, z: float): ...
    def __mul__(self, other: Vector3D): ...
    def __ne__(self, other: Self) -> bool:
        """
        Returns __True__ if the value for any axis is different.
        """
    def __str__(self) -> str:
        """
        Returns the axis values for the vector parsed as string.
        """
    def __sub__(self, other: Vector3D): ...
    def __truediv__(self, other: Vector3D): ...
    def cross(self, vector: Vector3D) -> Vector3D:
        """
        Computes the cross product between two vectors.
        """
    def distance(self, vector: Vector3D) -> float:
        """
        Computes the distance between two vectors.
        """
    def distance_2d(self, vector: Vector3D) -> float:
        """
        Computes the 2-dimensional distance between two vectors.
        """
    def distance_squared(self, vector: Vector3D) -> float:
        """
        Computes the squared distance between two vectors.
        """
    def distance_squared_2d(self, vector: Vector3D) -> float:
        """
        Computes the 2-dimensional squared distance between two vectors.
        """
    def dot(self, vector: Vector3D) -> float:
        """
        Computes the dot product between two vectors.
        """
    def dot_2d(self, vector: Vector3D) -> float:
        """
        Computes the 2-dimensional dot product between two vectors.
        """
    def length(self) -> float:
        """
        Computes the length of the vector.
        """
    def make_unit_vector(self) -> Vector3D:
        """
        Returns a vector with the same direction and unitary length.
        """
    def squared_length(self) -> float:
        """
        Computes the squared length of the vector.
        """
    @property
    def x(self) -> float:
        """
        X-axis value.
        """
    @property
    def y(self) -> float:
        """
        Y-axis value.
        """
    @property
    def z(self) -> float:
        """
        Z-axis value.
        """
