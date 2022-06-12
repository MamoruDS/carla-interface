# https://github.com/carla-simulator/carla/blob/master/PythonAPI/carla/source/libcarla/Commands.cpp
from ._c.rpc import ActorId
from .actor import Actor, VehicleLightState
from .blueprint import ActorBlueprint
from .control import (
    VehicleControl,
    VehiclePhysicsControl,
    WalkerControl,
)
from .geom import Transform, Vector3D
from typing import Literal, Union, overload
from typing_extensions import Self


TM_DEFAULT_PORT = 8000


FutureActor = 0


class _Command:
    pass


class Response:
    @property
    def actor_id(self) -> Union[ActorId, Literal[0]]:
        """
        // return self.HasError() ? 0u : self.Get();
        """
        raise NotImplementedError

    @property
    def error(self) -> str:
        """
        // return self.HasError() ? self.GetError().What() : std::string("");
        """
        raise NotImplementedError

    def has_error(self) -> bool:
        raise NotImplementedError


class SpawnActor(_Command):
    @overload
    def __init__(
        self, blueprint: ActorBlueprint, transform: Transform
    ) -> None:
        ...

    @overload
    def __init__(
        self,
        blueprint: ActorBlueprint,
        transform: Transform,
        parent_id: ActorId,
    ) -> None:
        ...

    @overload
    def __init__(
        self,
        blueprint: ActorBlueprint,
        transform: Transform,
        parent: Actor,
    ) -> None:
        ...

    def __init__(self, *args) -> None:  # type: ignore
        raise NotImplementedError

    @property
    def transform(self) -> Transform:
        raise NotImplementedError

    @transform.setter
    def transform(self, val: Transform) -> None:
        raise NotImplementedError

    @property
    def parent_id(self) -> ActorId:
        raise NotImplementedError

    @parent_id.setter
    def parent_id(self, val: ActorId) -> None:
        raise NotImplementedError

    def then(self, command: _Command) -> Self:
        raise NotImplementedError


class DestroyActor(_Command):
    @overload
    def __init__(self, actor: Actor) -> None:
        ...

    @overload
    def __init__(self, actor_id: ActorId) -> None:
        ...

    def __init__(self, *args) -> None:  # type: ignore
        raise NotImplementedError

    @property
    def actor_id(self) -> ActorId:
        raise NotImplementedError

    @actor_id.setter
    def actor_id(self, val: ActorId) -> None:
        raise NotImplementedError


class ApplyVehicleControl(_Command):
    @overload
    def __init__(self, actor: Actor, control: VehicleControl) -> None:
        ...

    @overload
    def __init__(self, actor_id: ActorId, control: VehicleControl) -> None:
        ...

    def __init__(self, *args) -> None:  # type: ignore
        raise NotImplementedError

    @property
    def actor_id(self) -> ActorId:
        raise NotImplementedError

    @actor_id.setter
    def actor_id(self, val: ActorId) -> None:
        raise NotImplementedError

    @property
    def control(self) -> VehicleControl:
        raise NotImplementedError

    @control.setter
    def control(self, val: VehicleControl) -> None:
        raise NotImplementedError


class ApplyWalkerControl(_Command):
    @overload
    def __init__(self, actor: Actor, control: WalkerControl) -> None:
        ...

    @overload
    def __init__(self, actor_id: ActorId, control: WalkerControl) -> None:
        ...

    def __init__(self, *args) -> None:  # type: ignore
        raise NotImplementedError

    @property
    def actor_id(self) -> ActorId:
        raise NotImplementedError

    @actor_id.setter
    def actor_id(self, val: ActorId) -> None:
        raise NotImplementedError

    @property
    def control(self) -> WalkerControl:
        raise NotImplementedError

    @control.setter
    def control(self, val: WalkerControl) -> None:
        raise NotImplementedError


class ApplyVehiclePhysicsControl(_Command):
    def __init__(
        self, actor: Actor, physics_control: VehiclePhysicsControl
    ) -> None:
        raise NotImplementedError

    @property
    def actor_id(self) -> ActorId:
        raise NotImplementedError

    @actor_id.setter
    def actor_id(self, val: ActorId) -> None:
        raise NotImplementedError

    @property
    def control(self) -> VehiclePhysicsControl:
        raise NotImplementedError

    @control.setter
    def control(self, val: VehiclePhysicsControl) -> None:
        raise NotImplementedError


class ApplyTransform(_Command):
    @overload
    def __init__(self, actor: Actor, transform: Transform) -> None:
        ...

    @overload
    def __init__(self, actor_id: ActorId, transform: Transform) -> None:
        ...

    def __init__(self, *args) -> None:  # type: ignore
        raise NotImplementedError

    @property
    def actor_id(self) -> ActorId:
        raise NotImplementedError

    @actor_id.setter
    def actor_id(self, val: ActorId) -> None:
        raise NotImplementedError

    @property
    def physics_control(self) -> Transform:
        raise NotImplementedError

    @physics_control.setter
    def physics_control(self, val: Transform) -> None:
        raise NotImplementedError


class ApplyWalkerState(_Command):
    @overload
    def __init__(
        self, actor: Actor, transform: Transform, speed: float
    ) -> None:
        ...

    @overload
    def __init__(
        self, actor_id: ActorId, transform: Transform, speed: float
    ) -> None:
        ...

    def __init__(self, *args) -> None:  # type: ignore
        raise NotImplementedError

    @property
    def actor_id(self) -> ActorId:
        raise NotImplementedError

    @actor_id.setter
    def actor_id(self, val: ActorId) -> None:
        raise NotImplementedError

    @property
    def transform(self) -> Transform:
        raise NotImplementedError

    @transform.setter
    def transform(self, val: Transform) -> None:
        raise NotImplementedError

    @property
    def speed(self) -> float:
        raise NotImplementedError

    @speed.setter
    def speed(self, val: float) -> None:
        raise NotImplementedError


class ApplyTargetVelocity(_Command):
    @overload
    def __init__(self, actor: Actor, velocity: Vector3D) -> None:
        ...

    @overload
    def __init__(self, actor_id: ActorId, velocity: Vector3D) -> None:
        ...

    def __init__(self, *args) -> None:  # type: ignore
        raise NotImplementedError

    @property
    def actor_id(self) -> ActorId:
        raise NotImplementedError

    @actor_id.setter
    def actor_id(self, val: ActorId) -> None:
        raise NotImplementedError

    @property
    def velocity(self) -> Vector3D:
        raise NotImplementedError

    @velocity.setter
    def velocity(self, val: Vector3D) -> None:
        raise NotImplementedError


class ApplyTargetAngularVelocity(_Command):
    @overload
    def __init__(self, actor: Actor, angular_velocity: Vector3D) -> None:
        ...

    @overload
    def __init__(self, actor_id: ActorId, angular_velocity: Vector3D) -> None:
        ...

    def __init__(self, *args) -> None:  # type: ignore
        raise NotImplementedError

    @property
    def actor_id(self) -> ActorId:
        raise NotImplementedError

    @actor_id.setter
    def actor_id(self, val: ActorId) -> None:
        raise NotImplementedError

    @property
    def angular_velocity(self) -> Vector3D:
        raise NotImplementedError

    @angular_velocity.setter
    def angular_velocity(self, val: Vector3D) -> None:
        raise NotImplementedError


class ApplyImpulse(_Command):
    @overload
    def __init__(self, actor: Actor, impulse: Vector3D) -> None:
        ...

    @overload
    def __init__(self, actor_id: ActorId, impulse: Vector3D) -> None:
        ...

    def __init__(self, *args) -> None:  # type: ignore
        raise NotImplementedError

    @property
    def actor_id(self) -> ActorId:
        raise NotImplementedError

    @actor_id.setter
    def actor_id(self, val: ActorId) -> None:
        raise NotImplementedError

    @property
    def impulse(self) -> Vector3D:
        raise NotImplementedError

    @impulse.setter
    def impulse(self, val: Vector3D) -> None:
        raise NotImplementedError


class ApplyForce(_Command):
    @overload
    def __init__(self, actor: Actor, force: Vector3D) -> None:
        ...

    @overload
    def __init__(self, actor_id: ActorId, force: Vector3D) -> None:
        ...

    def __init__(self, *args) -> None:  # type: ignore
        raise NotImplementedError

    @property
    def actor_id(self) -> ActorId:
        raise NotImplementedError

    @actor_id.setter
    def actor_id(self, val: ActorId) -> None:
        raise NotImplementedError

    @property
    def force(self) -> Vector3D:
        raise NotImplementedError

    @force.setter
    def force(self, val: Vector3D) -> None:
        raise NotImplementedError


class ApplyAngularImpulse(_Command):
    @overload
    def __init__(self, actor: Actor, impulse: Vector3D) -> None:
        ...

    @overload
    def __init__(self, actor_id: ActorId, impulse: Vector3D) -> None:
        ...

    def __init__(self, *args) -> None:  # type: ignore
        raise NotImplementedError

    @property
    def actor_id(self) -> ActorId:
        raise NotImplementedError

    @actor_id.setter
    def actor_id(self, val: ActorId) -> None:
        raise NotImplementedError

    @property
    def impulse(self) -> Vector3D:
        raise NotImplementedError

    @impulse.setter
    def impulse(self, val: Vector3D) -> None:
        raise NotImplementedError


class ApplyTorque(_Command):
    @overload
    def __init__(self, actor: Actor, torque: Vector3D) -> None:
        ...

    @overload
    def __init__(self, actor_id: ActorId, torque: Vector3D) -> None:
        ...

    def __init__(self, *args) -> None:  # type: ignore
        raise NotImplementedError

    @property
    def actor_id(self) -> ActorId:
        raise NotImplementedError

    @actor_id.setter
    def actor_id(self, val: ActorId) -> None:
        raise NotImplementedError

    @property
    def torque(self) -> Vector3D:
        raise NotImplementedError

    @torque.setter
    def torque(self, val: Vector3D) -> None:
        raise NotImplementedError


class SetSimulatePhysics(_Command):
    @overload
    def __init__(self, actor: Actor, enabled: bool) -> None:
        ...

    @overload
    def __init__(self, actor_id: ActorId, enabled: bool) -> None:
        ...

    def __init__(self, *args) -> None:  # type: ignore
        raise NotImplementedError

    @property
    def actor_id(self) -> ActorId:
        raise NotImplementedError

    @actor_id.setter
    def actor_id(self, val: ActorId) -> None:
        raise NotImplementedError

    @property
    def enabled(self) -> bool:
        raise NotImplementedError

    @enabled.setter
    def enabled(self, val: bool) -> None:
        raise NotImplementedError


class SetEnableGravity(_Command):
    @overload
    def __init__(self, actor: Actor, enabled: bool) -> None:
        ...

    @overload
    def __init__(self, actor_id: ActorId, enabled: bool) -> None:
        ...

    def __init__(self, *args) -> None:  # type: ignore
        raise NotImplementedError

    @property
    def actor_id(self) -> ActorId:
        raise NotImplementedError

    @actor_id.setter
    def actor_id(self, val: ActorId) -> None:
        raise NotImplementedError

    @property
    def enabled(self) -> bool:
        raise NotImplementedError

    @enabled.setter
    def enabled(self, val: bool) -> None:
        raise NotImplementedError


class SetAutopilot(_Command):
    @overload
    def __init__(
        self, actor: Actor, enabled: bool, tm_port: int = TM_DEFAULT_PORT
    ) -> None:
        ...

    @overload
    def __init__(
        self, actor_id: ActorId, enabled: bool, tm_port: int = TM_DEFAULT_PORT
    ) -> None:
        ...

    def __init__(self, *args) -> None:  # type: ignore
        raise NotImplementedError

    @property
    def actor_id(self) -> ActorId:
        raise NotImplementedError

    @actor_id.setter
    def actor_id(self, val: ActorId) -> None:
        raise NotImplementedError

    @property
    def tm_port(self) -> int:
        raise NotImplementedError

    @tm_port.setter
    def tm_port(self, val: int) -> None:
        raise NotImplementedError

    @property
    def enabled(self) -> bool:
        raise NotImplementedError

    @enabled.setter
    def enabled(self, val: bool) -> None:
        raise NotImplementedError


class ShowDebugTelemetry(_Command):
    @overload
    def __init__(self, actor: Actor, enabled: bool) -> None:
        ...

    @overload
    def __init__(self, actor_id: ActorId, enabled: bool) -> None:
        ...

    def __init__(self, *args) -> None:  # type: ignore
        raise NotImplementedError

    @property
    def actor_id(self) -> ActorId:
        raise NotImplementedError

    @actor_id.setter
    def actor_id(self, val: ActorId) -> None:
        raise NotImplementedError

    @property
    def enabled(self) -> bool:
        raise NotImplementedError

    @enabled.setter
    def enabled(self, val: bool) -> None:
        raise NotImplementedError


class SetVehicleLightState(_Command):
    @overload
    def __init__(self, actor: Actor, light_state: bool) -> None:
        ...

    @overload
    def __init__(self, actor_id: int, light_state: VehicleLightState) -> None:
        ...

    def __init__(self, *args) -> None:  # type: ignore
        raise NotImplementedError

    @property
    def actor_id(self) -> ActorId:
        raise NotImplementedError

    @actor_id.setter
    def actor_id(self, val: ActorId) -> None:
        raise NotImplementedError

    @property
    def light_state(self) -> VehicleLightState:
        raise NotImplementedError

    @light_state.setter
    def light_state(self, val: VehicleLightState) -> None:
        raise NotImplementedError
