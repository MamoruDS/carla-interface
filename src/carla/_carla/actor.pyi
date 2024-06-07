# https://github.com/carla-simulator/carla/blob/master/PythonAPI/carla/source/libcarla/Actor.cpp
from __future__ import annotations
from ._c.road import SignId
from ._c.rpc import ActorId
from ._c.traffic_manager import TM_DEFAULT_PORT
from ._generic import vector_of
from .control import (
    VehicleControl,
    VehiclePhysicsControl,
    WalkerBoneControlIn,
    WalkerBoneControlOut,
    WalkerControl,
)
from .geom import BoundingBox, Location, Transform, Vector3D
from .map import WayPoint
from .world import World
from enum import IntEnum
from typing import Dict, List

class ActorState(IntEnum):
    Invalid = 0
    Active = 1
    Dormant = 2

class vector_of_ints(vector_of[int]): ...

class Actor:
    @property
    def id(self) -> ActorId:
        """
        Identifier for this actor. Unique during a given episode.
        """
        raise NotImplementedError

    @property
    def type_id(self) -> str:
        """
        The identifier of the blueprint this actor was based on, e.g. `vehicle.ford.mustang`.
        """
        raise NotImplementedError

    @property
    def parent(self) -> Actor:
        """
        Actors may be attached to a parent actor that they will follow around.
        This is said actor.
        """
        raise NotImplementedError

    @property
    def semantic_tags(self) -> List[int]:
        """A list of semantic tags provided by the blueprint listing components for this actor. E.g. a traffic light could be tagged with `Pole` and `TrafficLight`. These tags are used by the semantic segmentation sensor. Find more about this and other sensors [here](ref_sensors.md#semantic-segmentation-camera)."""
        raise NotImplementedError

    @property
    def actor_state(self) -> ActorState:
        """
        Returns the `carla.ActorState`, which can identify if the actor is Active, Dormant or Invalid.
        """
        raise NotImplementedError

    @property
    def is_alive(self) -> bool:
        """
        Returns whether this object was destroyed using this actor handle.
        """
        raise NotImplementedError

    @property
    def is_dormant(self) -> bool:
        """
        Returns whether this actor is dormant (True) or not (False) - the opposite of is_active.
        """
        raise NotImplementedError

    @property
    def is_active(self) -> bool:
        """
        Returns whether this actor is active (True) or not (False).
        """
        raise NotImplementedError

    @property
    def attributes(self) -> Dict[str, str]:  # TODO: verify this
        """
        A dictionary containing the attributes of the blueprint this actor was based on.
        """
        raise NotImplementedError

    @property
    def bounding_box(self) -> BoundingBox:
        """
        Bounding box containing the geometry of the actor.
        Its location and rotation are relative to the actor it is attached to.
        """
        raise NotImplementedError

    def get_world(self) -> World:  # TODO: verify this
        raise NotImplementedError

    def get_location(self) -> Location:
        """
        Return the current location of the actor.

        @note This function does not call the simulator, it returns the location
        received in the last tick.
        """
        raise NotImplementedError

    def get_transform(self) -> Transform:
        """
        Return the current transform of the actor.

        @note This function does not call the simulator, it returns the
        transform received in the last tick.
        """
        raise NotImplementedError

    def get_velocity(self) -> Vector3D:
        """
        Return the current 3D velocity of the actor.

        @note This function does not call the simulator, it returns the
        velocity received in the last tick.
        """
        raise NotImplementedError

    def get_angular_velocity(self) -> Vector3D:
        """
        Return the current 3D angular velocity of the actor.

        @note This function does not call the simulator, it returns the
        angular velocity received in the last tick.
        """
        raise NotImplementedError

    def get_acceleration(self) -> Vector3D:
        """
        Return the current 3D acceleration of the actor.

        @note This function does not call the simulator, it returns the
        acceleration calculated after the actor's velocity.
        """
        raise NotImplementedError

    def set_location(self, location: Location) -> None:
        """
        Teleport the actor to @a location.
        """
        raise NotImplementedError

    def set_transform(self, transform: Transform) -> None:
        """
        Teleport and rotate the actor to @a transform.
        """
        raise NotImplementedError

    def set_target_velocity(self, velocity: Vector3D) -> None:
        """
        Set the actor velocity before applying physics.
        """
        raise NotImplementedError

    def set_target_angular_velocity(self, angular_velocity: Vector3D) -> None:
        """
        Set the angular velocity of the actor before applying physics.
        """
        raise NotImplementedError

    def enable_constant_velocity(self, velocity: Vector3D) -> None:
        """
        Enable a constant velocity mode
        """
        raise NotImplementedError

    def disable_constant_velocity(self) -> None:
        """
        Disable the constant velocity mode
        """
        raise NotImplementedError

    def add_impulse(self, impulse: Vector3D) -> None:
        """
        Add impulse to the actor at its center of mass.
        """
        raise NotImplementedError

    def add_force(self, force: Vector3D) -> None:
        """
        Add force to the actor at its center of mass.
        """
        raise NotImplementedError

    def add_angular_impulse(self, angular_impulse: Vector3D) -> None:
        """
        Add angular impulse to the actor.
        """
        raise NotImplementedError

    def add_torque(self, torque: Vector3D) -> None:
        """
        Add a torque to the actor.
        """
        raise NotImplementedError

    def set_simulate_physics(self, enabled: bool) -> None:
        """
        Enable or disable physics simulation on this actor.
        """
        raise NotImplementedError

    def set_enable_gravity(self, enabled: bool) -> None:
        """
        Enable or disable gravity on this actor.
        """
        raise NotImplementedError

    def destroy(self) -> bool:
        """
        Tell the simulator to destroy this Actor, and return whether the actor
        was successfully destroyed.

        @note It has no effect if the Actor was already successfully destroyed.

        @warning This function blocks until the destruction operation is
        completed by the simulator.
        """
        raise NotImplementedError

    def __str__(self) -> str:
        raise NotImplementedError

# https://github.com/carla-simulator/carla/blob/master/LibCarla/source/carla/rpc/VehicleLightState.h
class VehicleLightState(IntEnum):
    NONE = 0
    Position = 0x1
    LowBeam = 0x1 << 1
    HighBeam = 0x1 << 2
    Brake = 0x1 << 3
    RightBlinker = 0x1 << 4
    LeftBlinker = 0x1 << 5
    Reverse = 0x1 << 6
    Fog = 0x1 << 7
    Interior = 0x1 << 8
    Special1 = 0x1 << 9  # E.g: sirens
    Special2 = 0x1 << 10
    All = 0xFFFFFFFF

# https://github.com/carla-simulator/carla/blob/master/LibCarla/source/carla/rpc/VehicleWheels.h#L15
class VehicleWheelLocation(IntEnum):
    FL_Wheel = 0
    FR_Wheel = 1
    BL_Wheel = 2
    BR_Wheel = 3
    # Use for bikes and bicycles
    Front_Wheel = 0
    Back_Wheel = 1

# https://github.com/carla-simulator/carla/blob/master/LibCarla/source/carla/rpc/VehicleDoor.h#L16
class VehicleDoor:
    FL = 0
    FR = 1
    RL = 2
    RR = 3
    Hood = 4
    Trunk = 5
    All = 6

class Vehicle(Actor):
    def apply_control(self, control: VehicleControl) -> None:
        """
        Apply @a control to this vehicle.
        """
        raise NotImplementedError

    def get_control(self) -> VehicleControl:
        """
        Return the control last applied to this vehicle.

        @note This function does not call the simulator, it returns the data
        received in the last tick.
        """
        raise NotImplementedError

    def set_light_state(self, light_state: VehicleLightState) -> None:
        """
        Sets a @a LightState to this vehicle.
        """
        raise NotImplementedError

    def open_door(self, door_idx: VehicleDoor) -> None:
        """
        Open a door in this vehicle
        """
        raise NotImplementedError

    def close_door(self, door_idx: VehicleDoor) -> None:
        """
        Close a door in this vehicle
        """
        raise NotImplementedError

    def set_wheel_steer_direction(
        self, wheel_location: VehicleWheelLocation, angle_in_deg: float
    ) -> None:
        """
        Sets a @a Rotation to a wheel of the vehicle (affects the bone of the car skeleton, not the physics)
        """
        raise NotImplementedError

    def get_wheel_steer_angle(
        self, wheel_location: VehicleWheelLocation
    ) -> VehicleLightState:
        """
        Return a @a Rotation from a wheel of the vehicle

        @note The function returns the rotation of the vehicle based on the it's physics
        """
        raise NotImplementedError

    def get_light_state(self) -> VehicleLightState:
        """
        Return the current open lights (LightState) of this vehicle.

        @note This function does not call the simulator, it returns the data
        received in the last tick.
        """
        raise NotImplementedError

    def apply_physics_control(self, physics_control: VehiclePhysicsControl) -> None:
        """
        Apply physics control to this vehicle
        """
        raise NotImplementedError

    def get_physics_control(self) -> VehiclePhysicsControl:
        """
        Return the physics control last applied to this vehicle.

        @warning This function does call the simulator.
        """
        raise NotImplementedError

    def set_autopilot(
        self, enabled: bool = True, tm_port: int = TM_DEFAULT_PORT
    ) -> None:
        """
        Switch on/off this vehicle's autopilot.
        """
        raise NotImplementedError

    def show_debug_telemetry(self, enabled: bool = True) -> None:
        """
        Switch on/off this vehicle's autopilot. # FIXME:
        # https://github.com/carla-simulator/carla/blob/master/LibCarla/source/carla/client/Vehicle.h#L46
        """
        raise NotImplementedError

    def get_speed_limit(self) -> float:
        """
        Return the speed limit currently affecting this vehicle.

        @note This function does not call the simulator, it returns the data
        received in the last tick.
        """
        raise NotImplementedError

    def get_traffic_light_state(self) -> TrafficLightState:
        """
        Return the state of the traffic light currently affecting this vehicle.

        @return Green If no traffic light is affecting the vehicle.

        @note This function does not call the simulator, it returns the data
        received in the last tick.
        """
        raise NotImplementedError

    def is_at_traffic_light(self) -> bool:
        """
        Return whether a traffic light is affecting this vehicle.

        @note This function does not call the simulator, it returns the data
        received in the last tick.
        """
        raise NotImplementedError

    def get_traffic_light(self) -> TrafficLight:
        """
        Retrieve the traffic light actor currently affecting this vehicle.
        """
        raise NotImplementedError

    def enable_carsim(self, simfile_path: str = "") -> None:
        """
        Enables CarSim simulation if it is availiable
        """
        raise NotImplementedError

    def use_carsim_road(self, enabled: bool) -> None:
        """
        Enables the use of CarSim internal road definition instead of unreal's
        """
        raise NotImplementedError

    def enable_chrono_physics(
        self,
        max_substeps: int,
        max_substep_delta_time: float,
        vehicle_json: str = "",
        powetrain_json: str = "",
        tire_json: str = "",
        base_json_path: str = "",
    ) -> None:
        raise NotImplementedError

    def __str__(self) -> str:
        raise NotImplementedError

class Walker(Actor):
    def apply_control(self, control: WalkerControl) -> None:
        """
        Apply @a control to this Walker.
        """
        raise NotImplementedError

    def get_control(self) -> WalkerControl:
        """
        Return the control last applied to this Walker.

        @note This function does not call the simulator, it returns the Control
        received in the last tick.
        """
        raise NotImplementedError

    def get_bones(self) -> WalkerBoneControlOut:
        raise NotImplementedError

    def set_bones(self, bones: WalkerBoneControlIn) -> None:
        raise NotImplementedError

    def blend_pose(self, blend) -> None:
        raise NotImplementedError

    def show_pose(self) -> None:
        raise NotImplementedError

    def hide_pose(self) -> None:
        raise NotImplementedError

    def get_pose_from_animation(self) -> None:
        raise NotImplementedError

    def __str__(self) -> str:
        raise NotImplementedError

class WalkerAIController(Actor):
    def start(self) -> None:
        raise NotImplementedError

    def stop(self) -> None:
        raise NotImplementedError

    def go_to_location(self, destination: Location) -> None:
        raise NotImplementedError

    def set_max_speed(self, speed: float) -> None:
        raise NotImplementedError

    def __str__(self) -> str:
        raise NotImplementedError

class TrafficSign(Actor):
    @property
    def trigger_volume(self) -> BoundingBox:
        raise NotImplementedError

# https://github.com/carla-simulator/carla/blob/master/LibCarla/source/carla/rpc/TrafficLightState.h#L16
class TrafficLightState(IntEnum):
    Red = 0
    Yellow = 1
    Green = 2
    Off = 3
    Unknown = 4

class TrafficLight(TrafficSign):
    @property
    def state(self) -> TrafficLightState:
        """
        Return the current state of the traffic light.

        @note This function does not call the simulator, it returns the data
        received in the last tick.
        """
        raise NotImplementedError

    def set_state(self, state: TrafficLightState) -> None:
        raise NotImplementedError

    def get_state(self) -> TrafficLightState:
        """
        Return the current state of the traffic light.

        @note This function does not call the simulator, it returns the data
        received in the last tick.
        """
        raise NotImplementedError

    def set_green_time(self, green_time: float) -> None:
        raise NotImplementedError

    def get_green_time(self) -> float:
        """
        @note This function does not call the simulator, it returns the data
        received in the last tick.
        """
        raise NotImplementedError

    def set_yellow_time(self, yellow_time: float) -> None:
        raise NotImplementedError

    def get_yellow_time(self) -> float:
        """
        @note This function does not call the simulator, it returns the data
        received in the last tick.
        """
        raise NotImplementedError

    def set_red_time(self, red_time: float) -> None:
        raise NotImplementedError

    def get_red_time(self) -> float:
        """
        @note This function does not call the simulator, it returns the data
        received in the last tick.
        """
        raise NotImplementedError

    def get_elapsed_time(self) -> float:
        """
        @note This function does not call the simulator, it returns the data
        received in the last tick.
        """
        raise NotImplementedError

    def freeze(self, freeze: bool) -> None:
        raise NotImplementedError

    def is_frozen(self) -> float:
        """
        @note This function does not call the simulator, it returns the data
        received in the last tick.
        """
        raise NotImplementedError

    def get_pole_index(self) -> int:
        """
        Returns the index of the pole in the traffic light group
        """
        raise NotImplementedError

    def get_group_traffic_lights(self) -> List[TrafficLight]:
        """
        Return all traffic lights in the group this one belongs to.

        @note This function calls the simulator
        """
        raise NotImplementedError

    def reset_group(self) -> None:
        """
        resets the timers and states of all groups
        """
        raise NotImplementedError

    def get_affected_lane_waypoints(self) -> List[WayPoint]:
        raise NotImplementedError

    def get_light_boxes(self) -> List[BoundingBox]:
        raise NotImplementedError

    def get_opendrive_id(self) -> SignId:
        raise NotImplementedError

    def get_stop_waypoints(self) -> List[BoundingBox]:
        raise NotImplementedError

    def __str__(self) -> str:
        raise NotImplementedError
