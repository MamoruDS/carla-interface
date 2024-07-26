from .geom import Transform, Vector2D, Vector3D
from typing_extensions import Self

class GearPhysicsControl:
    """
    Class that provides access to vehicle transmission details by defining a gear and when to run on it. This will be later used by carla.VehiclePhysicsControl to help simulate physics.
    """
    def __eq__(self, other: Self) -> bool: ...
    def __init__(self, ratio: float, down_ratio: float, up_ratio: float): ...
    def __ne__(self, other: Self) -> bool: ...
    def __str__(self) -> str: ...
    @property
    def down_ratio(self) -> float:
        """
        Quotient between current RPM and MaxRPM where the autonomous gear box should shift down.
        """
    @property
    def ratio(self) -> float:
        """
        The transmission ratio of the gear.
        """
    @property
    def up_ratio(self) -> float:
        """
        Quotient between current RPM and MaxRPM where the autonomous gear box should shift up.
        """

class VehicleControl:
    """
    Manages the basic movement of a vehicle using typical driving controls.
    """
    def __eq__(self, other: Self) -> bool: ...
    def __init__(
        self,
        throttle: float,
        steer: float,
        brake: float,
        hand_brake: bool,
        reverse: bool,
        manual_gear_shift: bool,
        gear: int,
    ): ...
    def __ne__(self, other: Self) -> bool: ...
    def __str__(self) -> str: ...
    @property
    def brake(self) -> float:
        """
        A scalar value to control the vehicle brake [0.0, 1.0]. Default is 0.0.
        """
    @property
    def gear(self) -> int:
        """
        States which gear is the vehicle running on.
        """
    @property
    def hand_brake(self) -> bool:
        """
        Determines whether hand brake will be used. Default is <b>False</b>.
        """
    @property
    def manual_gear_shift(self) -> bool:
        """
        Determines whether the vehicle will be controlled by changing gears manually. Default is <b>False</b>.
        """
    @property
    def reverse(self) -> bool:
        """
        Determines whether the vehicle will move backwards. Default is <b>False</b>.
        """
    @property
    def steer(self) -> float:
        """
        A scalar value to control the vehicle steering [-1.0, 1.0]. Default is 0.0.
        """
    @property
    def throttle(self) -> float:
        """
        A scalar value to control the vehicle throttle [0.0, 1.0]. Default is 0.0.
        """

class VehiclePhysicsControl:
    """
    Summarizes the parameters that will be used to simulate a carla.Vehicle as a physical object. The specific settings for the wheels though are stipulated using carla.WheelPhysicsControl.
    """
    def __eq__(self, other: Self) -> bool: ...
    def __init__(
        self,
        torque_curve: list[Vector2D],
        max_rpm: float,
        moi: float,
        damping_rate_full_throttle: float,
        damping_rate_zero_throttle_clutch_engaged: float,
        damping_rate_zero_throttle_clutch_disengaged: float,
        use_gear_autobox: bool,
        gear_switch_time: float,
        clutch_strength: float,
        final_ratio: float,
        forward_gears: list[GearPhysicsControl],
        drag_coefficient: float,
        center_of_mass: Vector3D,
        steering_curve: Vector2D,
        wheels: list[WheelPhysicsControl],
        use_sweep_wheel_collision: bool,
        mass: float,
    ):
        """
        VehiclePhysicsControl constructor
        """
    def __ne__(self, other: Self) -> bool: ...
    def __str__(self) -> str: ...
    @property
    def center_of_mass(self) -> Vector3D:
        """
        Center of mass of the vehicle.
        """
    @property
    def clutch_strength(self) -> float:
        """
        Clutch strength of the vehicle.
        """
    @property
    def damping_rate_full_throttle(self) -> float:
        """
        Damping ratio when the throttle is maximum.
        """
    @property
    def damping_rate_zero_throttle_clutch_disengaged(self) -> float:
        """
        Damping ratio when the throttle is zero with clutch disengaged.
        """
    @property
    def damping_rate_zero_throttle_clutch_engaged(self) -> float:
        """
        Damping ratio when the throttle is zero with clutch engaged.
        """
    @property
    def drag_coefficient(self) -> float:
        """
        Drag coefficient of the vehicle's chassis.
        """
    @property
    def final_ratio(self) -> float:
        """
        Fixed ratio from transmission to wheels.
        """
    @property
    def forward_gears(self) -> list[GearPhysicsControl]:
        """
        List of objects defining the vehicle's gears.
        """
    @property
    def gear_switch_time(self) -> float:
        """
        Switching time between gears.
        """
    @property
    def mass(self) -> float:
        """
        Mass of the vehicle.
        """
    @property
    def max_rpm(self) -> float:
        """
        The maximum RPM of the vehicle's engine.
        """
    @property
    def moi(self) -> float:
        """
        The moment of inertia of the vehicle's engine.
        """
    @property
    def steering_curve(self) -> list[Vector2D]:
        """
        Curve that indicates the maximum steering for a specific forward speed.
        """
    @property
    def torque_curve(self) -> list[Vector2D]:
        """
        Curve that indicates the torque measured in Nm for a specific RPM of the vehicle's engine.
        """
    @property
    def use_gear_autobox(self) -> bool:
        """
        If <b>True</b>, the vehicle will have an automatic transmission.
        """
    @property
    def use_sweep_wheel_collision(self) -> bool:
        """
        Enable the use of sweep for wheel collision. By default, it is disabled and it uses a simple raycast from the axis to the floor for each wheel. This option provides a better collision model in which the full volume of the wheel is checked against collisions.
        """
    @property
    def wheels(self) -> list[WheelPhysicsControl]:
        """
        List of wheel physics objects. This list should have 4 elements, where index 0 corresponds to the front left wheel, index 1 corresponds to the front right wheel, index 2 corresponds to the back left wheel and index 3 corresponds to the back right wheel. For 2 wheeled vehicles, set the same values for both front and back wheels.
        """

class WalkerBoneControlIn:
    """
    This class grants bone specific manipulation for walker. The skeletons of walkers have been unified for clarity and the transform applied to each bone are always relative to its parent. Take a look [here](tuto_G_control_walker_skeletons.md) to learn more on how to create a walker and define its movement.
    """
    def __init__(self, *arg: tuple[str, Transform]):
        """
        Initializes an object containing moves to be applied on tick. These are listed with the name of the bone and the transform that will be applied to it.
        """
    def __str__(self) -> str: ...
    @property
    def bone_transforms(self) -> list[tuple[str, Transform]]:
        """
        List with the data for each bone we want to set:
          - name: bone name
          - relative: transform based on the bone parent
        """

class WalkerBoneControlOut:
    """
    This class is used to return all bone positions of a pedestrian. For each bone we get its _name_ and its transform in three different spaces (world, actor and relative).
    """
    def __str__(self) -> str: ...
    @property
    def bone_transforms(self):
        """
        List of one entry per bone with this information:
          - name: bone name
          - world: transform in world coordinates
          - component: transform based on the pivot of the actor
          - relative: transform based on the bone parent
        """

class WalkerControl:
    """
    This class defines specific directions that can be commanded to a carla.Walker to control it via script.

      AI control can be settled for walkers, but the control used to do so is carla.WalkerAIController.
    """
    def __eq__(self, other: Self) -> bool:
        """
        Compares every variable with `other` and returns <b>True</b> if these are all the same.
        """
    def __init__(self, direction: Vector3D, speed: float, jump: bool): ...
    def __ne__(self, other: Self) -> bool:
        """
        Compares every variable with `other` and returns <b>True</b> if any of these differ.
        """
    def __str__(self) -> str: ...
    @property
    def direction(self) -> Vector3D:
        """
        Vector using global coordinates that will correspond to the direction of the walker.
        """
    @property
    def jump(self) -> bool:
        """
        If <b>True</b>, the walker will perform a jump.
        """
    @property
    def speed(self) -> float:
        """
        A scalar value to control the walker's speed.
        """

class WheelPhysicsControl:
    """
    Class that defines specific physical parameters for wheel objects that will be part of a carla.VehiclePhysicsControl to simulate vehicle it as a material object.
    """
    def __eq__(self, other: Self) -> bool: ...
    def __init__(
        self,
        tire_friction: float,
        damping_rate: float,
        max_steer_angle: float,
        radius: float,
        max_brake_torque: float,
        max_handbrake_torque: float,
        position: Vector3D,
    ): ...
    def __ne__(self, other: Self) -> bool: ...
    def __str__(self) -> str: ...
    @property
    def damping_rate(self) -> float:
        """
        Damping rate of the wheel.
        """
    @property
    def lat_stiff_max_load(self) -> float:
        """
        Maximum normalized tire load at which the tire can deliver no more lateral stiffness no matter how much extra load is applied to the tire. Each vehicle has a custom value.
        """
    @property
    def lat_stiff_value(self) -> float:
        """
        Maximum stiffness per unit of lateral slip. Each vehicle has a custom value.
        """
    @property
    def long_stiff_value(self) -> float:
        """
        Tire longitudinal stiffness per unit gravitational acceleration. Each vehicle has a custom value.
        """
    @property
    def max_brake_torque(self) -> float:
        """
        Maximum brake torque.
        """
    @property
    def max_handbrake_torque(self) -> float:
        """
        Maximum handbrake torque.
        """
    @property
    def max_steer_angle(self) -> float:
        """
        Maximum angle that the wheel can steer.
        """
    @property
    def position(self) -> Vector3D:
        """
        World position of the wheel. This is a read-only parameter.
        """
    @property
    def radius(self) -> float:
        """
        Radius of the wheel.
        """
    @property
    def tire_friction(self) -> float:
        """
        A scalar value that indicates the friction of the wheel.
        """
