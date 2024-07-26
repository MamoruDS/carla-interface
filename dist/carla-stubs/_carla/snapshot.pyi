from .geom import Transform, Vector3D
from .world import Timestamp
from typing_extensions import Self

class ActorSnapshot:
    """
    A class that comprises all the information for an actor at a certain moment in time. These objects are contained in a carla.WorldSnapshot and sent to the client once every tick.
    """
    def get_acceleration(self) -> Vector3D:
        """
        Returns the acceleration vector registered for an actor in that tick.
        """
    def get_angular_velocity(self) -> Vector3D:
        """
        Returns the angular velocity vector registered for an actor in that tick.
        """
    def get_transform(self) -> Transform:
        """
        Returns the actor's transform (location and rotation) for an actor in that tick.
        """
    def get_velocity(self) -> Vector3D:
        """
        Returns the velocity vector registered for an actor in that tick.
        """
    @property
    def id(self) -> int:
        """
        An identifier for the snapshot itself.
        """

class WorldSnapshot:
    """
    This snapshot comprises all the information for every actor on scene at a certain moment of time. It creates and gives acces to a data structure containing a series of carla.ActorSnapshot. The client recieves a new snapshot on every tick that cannot be stored.
    """
    def __eq__(self, other: Self) -> bool:
        """
        Returns __True__ if both **<font color="#f8805a">timestamp</font>** are the same.
        """
    def __iter__(self):
        """
        Iterate over the carla.ActorSnapshot stored in the snapshot.
        """
    def __len__(self) -> int:
        """
        Returns the amount of carla.ActorSnapshot present in this snapshot.
        """
    def __ne__(self, other: Self) -> bool:
        """
        Returns <b>True</b> if both **<font color="#f8805a">timestamp</font>** are different.
        """
    def find(self, actor_id: int) -> ActorSnapshot:
        """
        Given a certain actor ID, returns its corresponding snapshot or <b>None</b> if it is not found.
        """
    def has_actor(self, actor_id: int) -> bool:
        """
        Given a certain actor ID, checks if there is a snapshot corresponding it and so, if the actor was present at that moment.
        """
    @property
    def frame(self) -> int:
        """
        Simulation frame in which the snapshot was taken.
        """
    @property
    def id(self) -> int:
        """
        A value unique for every snapshot to differenciate them.
        """
    @property
    def timestamp(self) -> Timestamp:
        """
        Precise moment in time when snapshot was taken. This class works in seconds as given by the operative system.
        """
