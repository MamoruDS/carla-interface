from .actor import Actor, VehicleLightState
from .blueprint import ActorBlueprint
from .control import VehiclePhysicsControl, WalkerControl, VehicleControl
from .geom import Vector3D, Transform
from typing import Union

class ApplyAngularImpulse:
    """
    Command adaptation of __<font color="#7fb800">add_angular_impulse()</font>__ in carla.Actor. Applies an angular impulse to an actor.
    """
    def __init__(self, actor: Union[Actor, int], impulse: Vector3D): ...
    @property
    def actor_id(self) -> int:
        """
        Actor affected by the command.
        """
    @property
    def impulse(self) -> Vector3D:
        """
        Angular impulse applied to the actor.
        """

class ApplyForce:
    """
    Command adaptation of __<font color="#7fb800">add_force()</font>__ in carla.Actor. Applies a force to an actor.
    """
    def __init__(self, actor: Union[Actor, int], force: Vector3D): ...
    @property
    def actor_id(self) -> int:
        """
        Actor affected by the command.
        """
    @property
    def force(self) -> Vector3D:
        """
        Force applied to the actor over time.
        """

class ApplyImpulse:
    """
    Command adaptation of __<font color="#7fb800">add_impulse()</font>__ in carla.Actor. Applies an impulse to an actor.
    """
    def __init__(self, actor: Union[Actor, int], impulse: Vector3D): ...
    @property
    def actor_id(self) -> int:
        """
        Actor affected by the command.
        """
    @property
    def impulse(self) -> Vector3D:
        """
        Impulse applied to the actor.
        """

class ApplyTargetAngularVelocity:
    """
    Command adaptation of __<font color="#7fb800">set_target_angular_velocity()</font>__ in carla.Actor. Sets the actor's angular velocity vector.
    """
    def __init__(self, actor: Union[Actor, int], angular_velocity: Vector3D): ...
    @property
    def actor_id(self) -> int:
        """
        Actor affected by the command.
        """
    @property
    def angular_velocity(self) -> Vector3D:
        """
        The 3D angular velocity that will be applied to the actor.
        """

class ApplyTargetVelocity:
    """
    Command adaptation of __<font color="#7fb800">set_target_velocity()</font>__ in carla.Actor.
    """
    def __init__(self, actor: Union[Actor, int], velocity: Vector3D): ...
    @property
    def actor_id(self) -> int:
        """
        Actor affected by the command.
        """
    @property
    def velocity(self) -> Vector3D:
        """
        The 3D velocity applied to the actor.
        """

class ApplyTorque:
    """
    Command adaptation of __<font color="#7fb800">add_torque()</font>__ in carla.Actor. Applies a torque to an actor.
    """
    def __init__(self, actor: Union[Actor, int], torque: Vector3D): ...
    @property
    def actor_id(self) -> int:
        """
        Actor affected by the command.
        """
    @property
    def torque(self) -> Vector3D:
        """
        Torque applied to the actor over time.
        """

class ApplyTransform:
    """
    Command adaptation of __<font color="#7fb800">set_transform()</font>__ in carla.Actor. Sets a new transform to an actor.
    """
    def __init__(self, actor: Union[Actor, int], transform: Transform): ...
    @property
    def actor_id(self) -> int:
        """
        Actor affected by the command.
        """
    @property
    def transform(self) -> Transform:
        """
        Transformation to be applied.
        """

class ApplyVehicleControl:
    """
    Command adaptation of __<font color="#7fb800">apply_control()</font>__ in carla.Vehicle. Applies a certain control to a vehicle.
    """
    def __init__(self, actor: Union[Actor, int], control: VehicleControl): ...
    @property
    def actor_id(self) -> int:
        """
        Vehicle actor affected by the command.
        """
    @property
    def control(self) -> VehicleControl:
        """
        Vehicle control to be applied.
        """

class ApplyVehiclePhysicsControl:
    """
    Command adaptation of __<font color="#7fb800">apply_physics_control()</font>__ in carla.Vehicle. Applies a new physics control to a vehicle, modifying its physical parameters.
    """
    def __init__(self, actor: Union[Actor, int], control: VehiclePhysicsControl): ...
    @property
    def actor_id(self) -> int:
        """
        Vehicle actor affected by the command.
        """
    @property
    def control(self) -> VehiclePhysicsControl:
        """
        Physics control to be applied.
        """

class ApplyWalkerControl:
    """
    Command adaptation of __<font color="#7fb800">apply_control()</font>__ in carla.Walker. Applies a control to a walker.
    """
    def __init__(self, actor: Union[Actor, int], control: WalkerControl): ...
    @property
    def actor_id(self) -> int:
        """
        Walker actor affected by the command.
        """
    @property
    def control(self) -> WalkerControl:
        """
        Walker control to be applied.
        """

class ApplyWalkerState:
    """
    Apply a state to the walker actor. Specially useful to initialize an actor them with a specific location, orientation and speed.
    """
    def __init__(
        self, actor: Union[Actor, int], transform: Transform, speed: float
    ): ...
    @property
    def actor_id(self) -> int:
        """
        Walker actor affected by the command.
        """
    @property
    def speed(self) -> float:
        """
        Speed to be applied.
        """
    @property
    def transform(self) -> Transform:
        """
        Transform to be applied.
        """

class DestroyActor:
    """
    Command adaptation of __<font color="#7fb800">destroy()</font>__ in carla.Actor that tells the simulator to destroy this actor. It has no effect if the actor was already destroyed. When executed with __<font color="#7fb800">apply_batch_sync()</font>__ in carla.Client there will be a <b>command.Response</b> that will return a boolean stating whether the actor was successfully destroyed.
    """
    def __init__(self, actor: Union[Actor, int]): ...
    @property
    def actor_id(self) -> int:
        """
        Actor affected by the command
        """

class Response:
    """
    States the result of executing a command as either the ID of the actor to whom the command was applied to (when succeeded) or an error string (when failed).  actor ID, depending on whether or not the command succeeded. The method __<font color="#7fb800">apply_batch_sync()</font>__ in carla.Client returns a list of these to summarize the execution of a batch.
    """
    def has_error(self) -> bool:
        """
        Returns <b>True</b> if the command execution fails, and <b>False</b> if it was successful.
        """
    @property
    def actor_id(self) -> int:
        """
        Actor to whom the command was applied to. States that the command was successful.
        """
    @property
    def error(self) -> str:
        """
        A string stating the command has failed.
        """

class SetAutopilot:
    """
    Command adaptation of __<font color="#7fb800">set_autopilot()</font>__ in carla.Vehicle. Turns on/off the vehicle's autopilot mode.
    """
    def __init__(self, actor: Union[Actor, int], enabled: bool, port: int): ...
    @property
    def actor_id(self) -> int:
        """
        Actor that is affected by the command.
        """
    @property
    def enabled(self) -> bool:
        """
        If autopilot should be activated or not.
        """
    @property
    def port(self) -> int:
        """
        Port of the Traffic Manager where the vehicle is to be registered or unlisted.
        """

class SetEnableGravity:
    """
    Command adaptation of __<font color="#7fb800">set_enable_gravity()</font>__ in carla.Actor. Enables or disables gravity on an actor.
    """
    def __init__(self, actor: Union[Actor, int], enabled: bool): ...
    @property
    def actor_id(self) -> Union[Actor, int]:
        """
        Actor that is affected by the command.
        """
    @property
    def enabled(self) -> bool: ...

class SetSimulatePhysics:
    """
    Command adaptation of __<font color="#7fb800">set_simulate_physics()</font>__ in carla.Actor. Determines whether an actor will be affected by physics or not.
    """
    def __init__(self, actor: Union[Actor, int], enabled: bool): ...
    @property
    def actor_id(self) -> int:
        """
        Actor affected by the command.
        """
    @property
    def enabled(self) -> bool:
        """
        If physics should be activated or not.
        """

class SetVehicleLightState:
    """
    Command adaptation of __<font color="#7fb800">set_light_state()</font>__ in carla.Vehicle. Sets the light state of a vehicle.
    """
    def __init__(self, actor: Union[Actor, int], light_state: VehicleLightState): ...
    @property
    def actor_id(self) -> int:
        """
        Actor that is affected by the command.
        """
    @property
    def light_state(self) -> VehicleLightState:
        """
        Defines the light state of a vehicle.
        """

class ShowDebugTelemetry:
    """
    Command adaptation of __<font color="#7fb800">show_debug_telemetry()</font>__ in carla.Actor. Displays vehicle control telemetry data.
    """
    def __init__(self, actor: Union[Actor, int], enabled: bool): ...
    @property
    def actor_id(self) -> Union[Actor, int]:
        """
        Actor that is affected by the command.
        """
    @property
    def enabled(self) -> bool: ...

class SpawnActor:
    """
    Command adaptation of __<font color="#7fb800">spawn_actor()</font>__ in carla.World. Spawns an actor into the world based on the blueprint provided and the transform. If a parent is provided, the actor is attached to it.
    """
    def __init__(self): ...
    def __init__(self, blueprint: ActorBlueprint, transform: Transform): ...
    def __init__(
        self, blueprint: ActorBlueprint, transform: Transform, parent: Union[Actor, int]
    ): ...
    def then(self, command):
        """
        Links another command to be executed right after. It allows to ease very common flows such as spawning a set of vehicles by command and then using this method to set them to autopilot automatically.
        """
    @property
    def parent_id(self) -> int:
        """
        Identificator of the parent actor.
        """
    @property
    def transform(self) -> Transform:
        """
        Transform to be applied.
        """
