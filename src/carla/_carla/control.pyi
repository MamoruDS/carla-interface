# https://github.com/carla-simulator/carla/blob/master/PythonAPI/carla/source/libcarla/Control.cpp
from ._generic import vector_of
from .geom import Location, Transform, Vector2D, Vector3D
from typing import Generic, List, TypeVar, Union
from typing_extensions import Self


class VehicleControl:
    def __init__(
        self,
        throttle: float = 0.0,
        steer: float = 0.0,
        brake: float = 0.0,
        hand_brake: bool = False,
        reverse: bool = False,
        manual_gear_shift: bool = False,
        gear: int = 0,
    ) -> None:
        raise NotImplementedError

    @property
    def throttle(self) -> float:
        raise NotImplementedError

    @throttle.setter
    def throttle(self, val: float) -> None:
        raise NotImplementedError

    @property
    def steer(self) -> float:
        raise NotImplementedError

    @steer.setter
    def steer(self, val: float) -> None:
        raise NotImplementedError

    @property
    def brake(self) -> float:
        raise NotImplementedError

    @brake.setter
    def brake(self, val: float) -> None:
        raise NotImplementedError

    @property
    def hand_brake(self) -> bool:
        raise NotImplementedError

    @hand_brake.setter
    def hand_brake(self, val: bool) -> None:
        raise NotImplementedError

    @property
    def reverse(self) -> bool:
        raise NotImplementedError

    @reverse.setter
    def reverse(self, val: bool) -> None:
        raise NotImplementedError

    @property
    def manual_gear_shift(self) -> bool:
        raise NotImplementedError

    @manual_gear_shift.setter
    def manual_gear_shift(self, val: bool) -> None:
        raise NotImplementedError

    @property
    def gear(self) -> int:
        raise NotImplementedError

    @gear.setter
    def gear(self, val: int) -> None:
        raise NotImplementedError

    def __eq__(self, __o: Self) -> bool:
        raise NotImplementedError

    def __ne__(self, __o: Self) -> bool:
        raise NotImplementedError

    def __str__(self) -> str:
        raise NotImplementedError


class WalkerControl:
    def __init__(
        self,
        direction: Vector3D = Vector3D(1.0, 0.0, 0.0),
        speed: float = 0.0,
        jump: bool = False,
    ) -> None:
        raise NotImplementedError

    @property
    def direction(self) -> Vector3D:
        raise NotImplementedError

    @direction.setter
    def direction(self, val: Vector3D) -> None:
        raise NotImplementedError

    @property
    def speed(self) -> float:
        raise NotImplementedError

    @speed.setter
    def speed(self, val: float) -> None:
        raise NotImplementedError

    @property
    def jump(self) -> bool:
        raise NotImplementedError

    @jump.setter
    def jump(self, val: bool) -> None:
        raise NotImplementedError

    def __eq__(self, __o: Self) -> bool:
        raise NotImplementedError

    def __ne__(self, __o: Self) -> bool:
        raise NotImplementedError

    def __str__(self) -> str:
        raise NotImplementedError


class bone_transform:
    def __init__(self) -> None:
        raise NotImplementedError

    @property
    def name(self) -> str:
        raise NotImplementedError

    @name.setter
    def name(self, val: str) -> None:
        raise NotImplementedError

    @property
    def transform(self) -> Transform:
        raise NotImplementedError

    @transform.setter
    def transform(self, val: Transform) -> None:
        raise NotImplementedError

    def __str__(self) -> str:
        raise NotImplementedError


class vector_of_bones(vector_of[bone_transform]):
    ...


class bone_transform_out:
    @property
    def name(self) -> str:
        raise NotImplementedError

    @name.setter
    def name(self, val: str) -> None:
        raise NotImplementedError

    @property
    def world(self) -> Transform:
        raise NotImplementedError

    @world.setter
    def world(self, val: Transform) -> None:
        raise NotImplementedError

    @property
    def component(self) -> Transform:
        raise NotImplementedError

    @component.setter
    def component(self, val: Transform) -> None:
        raise NotImplementedError

    @property
    def relative(self) -> Transform:
        raise NotImplementedError

    @relative.setter
    def relative(self, val: Transform) -> None:
        raise NotImplementedError

    def __eq__(self, __o: Self) -> bool:
        raise NotImplementedError

    def __ne__(self, __o: Self) -> bool:
        raise NotImplementedError

    def __str__(self) -> str:
        raise NotImplementedError


class vector_of_bones_out(vector_of[bone_transform_out]):
    ...


BT = TypeVar("BT", bound=Union[bone_transform, bone_transform_out])


class _WalkerBoneControl(Generic[BT]):
    def __init__(self, *args, **kwargs) -> None:  # TODO:
        raise NotImplementedError

    @property
    def bone_transforms(self) -> BT:
        raise NotImplementedError

    def __str__(self) -> str:
        raise NotImplementedError


class WalkerBoneControlIn(_WalkerBoneControl[bone_transform]):
    ...


class WalkerBoneControlOut(_WalkerBoneControl[bone_transform_out]):
    ...


class GearPhysicsControl:
    def __init__(
        self,
        ratio: float = 1.0,
        down_ratio: float = 0.5,
        up_ratio: float = 0.65,
    ) -> None:
        raise NotImplementedError

    @property
    def ratio(self) -> float:
        raise NotImplementedError

    @ratio.setter
    def ratio(self, val: float) -> None:
        raise NotImplementedError

    @property
    def down_ratio(self) -> float:
        raise NotImplementedError

    @down_ratio.setter
    def down_ratio(self, val: float) -> None:
        raise NotImplementedError

    @property
    def up_ratio(self) -> float:
        raise NotImplementedError

    @up_ratio.setter
    def up_ratio(self, val: float) -> None:
        raise NotImplementedError

    def __eq__(self, __o: Self) -> bool:
        raise NotImplementedError

    def __ne__(self, __o: Self) -> bool:
        raise NotImplementedError

    def __str__(self) -> str:
        raise NotImplementedError


class vector_of_gears(vector_of[GearPhysicsControl]):
    ...


class WheelPhysicsControl:
    def __init__(
        self,
        tire_friction: float = 2.0,
        damping_rate: float = 0.25,
        max_steer_angle: float = 70.0,
        radius: float = 30.0,
        max_brake_torque: float = 1500.0,
        max_handbrake_torque: float = 3000.0,
        lat_stiff_max_load: float = 2.0,
        lat_stiff_value: float = 17.0,
        long_stiff_value: float = 1000.0,
        position: Vector3D = Vector3D(0, 0, 0),
    ) -> None:
        raise NotImplementedError

    @property
    def tire_friction(self) -> float:
        raise NotImplementedError

    @tire_friction.setter
    def tire_friction(self, val: float) -> None:
        raise NotImplementedError

    @property
    def damping_rate(self) -> float:
        raise NotImplementedError

    @damping_rate.setter
    def damping_rate(self, val: float) -> None:
        raise NotImplementedError

    @property
    def max_steer_angle(self) -> float:
        raise NotImplementedError

    @max_steer_angle.setter
    def max_steer_angle(self, val: float) -> None:
        raise NotImplementedError

    @property
    def radius(self) -> float:
        raise NotImplementedError

    @radius.setter
    def radius(self, val: float) -> None:
        raise NotImplementedError

    @property
    def max_brake_torque(self) -> float:
        raise NotImplementedError

    @max_brake_torque.setter
    def max_brake_torque(self, val: float) -> None:
        raise NotImplementedError

    @property
    def max_handbrake_torque(self) -> float:
        raise NotImplementedError

    @max_handbrake_torque.setter
    def max_handbrake_torque(self, val: float) -> None:
        raise NotImplementedError

    @property
    def lat_stiff_max_load(self) -> float:
        raise NotImplementedError

    @lat_stiff_max_load.setter
    def lat_stiff_max_load(self, val: float) -> None:
        raise NotImplementedError

    @property
    def lat_stiff_value(self) -> float:
        raise NotImplementedError

    @lat_stiff_value.setter
    def lat_stiff_value(self, val: float) -> None:
        raise NotImplementedError

    @property
    def long_stiff_value(self) -> float:
        raise NotImplementedError

    @long_stiff_value.setter
    def long_stiff_value(self, val: float) -> None:
        raise NotImplementedError

    @property
    def position(self) -> Vector3D:
        raise NotImplementedError

    @position.setter
    def position(self, val: Vector3D) -> None:
        raise NotImplementedError

    def __eq__(self, __o: Self) -> bool:
        raise NotImplementedError

    def __ne__(self, __o: Self) -> bool:
        raise NotImplementedError

    def __str__(self) -> str:
        raise NotImplementedError


class vector_of_wheels(vector_of[WheelPhysicsControl]):
    ...


class VehiclePhysicsControl:
    # max_rpm: float = 5000.0
    # moi: float = 1.0
    # damping_rate_full_throttle: float = 0.15
    # damping_rate_zero_throttle_clutch_engaged: float = 2.0
    # damping_rate_zero_throttle_clutch_disengaged: float = 0.35
    # use_gear_autobox: bool = True
    # gear_switch_time: float = 0.5
    # clutch_strength: float = 10.0
    # final_ratio: float = 4.0
    # mass: float = 1000.0
    # drag_coefficient: float = 0.3
    # center_of_mass: Location
    # use_sweep_wheel_collision: bool = False

    def __init__(self, *args, **kwargs) -> None:  # TODO:
        raise NotImplementedError

    @property
    def torque_curve(self) -> List[Vector2D]:
        raise NotImplementedError

    @property
    def max_rpm(self) -> float:
        raise NotImplementedError

    @max_rpm.setter
    def max_rpm(self, val: float) -> None:
        raise NotImplementedError

    @property
    def moi(self) -> float:
        raise NotImplementedError

    @moi.setter
    def moi(self, val: float) -> None:
        raise NotImplementedError

    @property
    def use_gear_autobox(self) -> bool:
        raise NotImplementedError

    @use_gear_autobox.setter
    def use_gear_autobox(self, val: bool) -> None:
        raise NotImplementedError

    @property
    def gear_switch_time(self) -> float:
        raise NotImplementedError

    @gear_switch_time.setter
    def gear_switch_time(self, val: float) -> None:
        raise NotImplementedError

    @property
    def clutch_strength(self) -> float:
        raise NotImplementedError

    @clutch_strength.setter
    def clutch_strength(self, val: float) -> None:
        raise NotImplementedError

    @property
    def final_ratio(self) -> float:
        raise NotImplementedError

    @final_ratio.setter
    def final_ratio(self, val: float) -> None:
        raise NotImplementedError

    @property
    def forward_gears(self) -> List[GearPhysicsControl]:
        raise NotImplementedError

    @property
    def mass(self) -> float:
        raise NotImplementedError

    @mass.setter
    def mass(self, val: float) -> None:
        raise NotImplementedError

    @property
    def drag_coefficient(self) -> float:
        raise NotImplementedError

    @drag_coefficient.setter
    def drag_coefficient(self, val: float) -> None:
        raise NotImplementedError

    @property
    def center_of_mass(self) -> Location:
        raise NotImplementedError

    @center_of_mass.setter
    def center_of_mass(self, val: Location) -> None:
        raise NotImplementedError

    @property
    def steering_curve(self) -> List[Vector2D]:
        raise NotImplementedError

    @property
    def wheels(self) -> List[WheelPhysicsControl]:
        raise NotImplementedError

    @property
    def use_sweep_wheel_collision(self) -> bool:
        raise NotImplementedError

    @use_sweep_wheel_collision.setter
    def use_sweep_wheel_collision(self, val: bool) -> None:
        raise NotImplementedError

    def __eq__(self, __o: Self) -> bool:
        raise NotImplementedError

    def __ne__(self, __o: Self) -> bool:
        raise NotImplementedError

    def __str__(self) -> str:
        raise NotImplementedError
