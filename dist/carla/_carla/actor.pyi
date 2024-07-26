from .control import (
    WalkerBoneControlIn,
    WalkerBoneControlOut,
    VehicleControl,
    VehiclePhysicsControl,
    WalkerControl,
)
from .geom import Transform, Vector3D, BoundingBox, Location
from .map import Waypoint
from .world import World
from enum import IntEnum, auto

class Actor:
    """
    CARLA defines actors as anything that plays a role in the simulation or can be moved around. That includes: pedestrians, vehicles, sensors and traffic signs (considering traffic lights as part of these). Actors are spawned in the simulation by carla.World and they need for a carla.ActorBlueprint to be created. These blueprints belong into a library provided by CARLA, find more about them [here](bp_library.md).
    """
    def __str__(self) -> str: ...
    def add_angular_impulse(self, angular_impulse: Vector3D):
        """
        Applies an angular impulse at the center of mass of the actor. This method should be used for instantaneous torques, usually applied once. Use __<font color="#7fb800">add_torque()</font>__ to apply rotation forces over a period of time.
        """
    def add_force(self, force: Vector3D):
        """
        Applies a force at the center of mass of the actor. This method should be used for forces that are applied over a certain period of time. Use __<font color="#7fb800">add_impulse()</font>__ to apply an impulse that only lasts an instant.
        """
    def add_impulse(self, impulse: Vector3D):
        """
        Applies an impulse at the center of mass of the actor. This method should be used for instantaneous forces, usually applied once. Use __<font color="#7fb800">add_force()</font>__ to apply forces over a period of time.
        """
    def add_torque(self, torque: Vector3D):
        """
        Applies a torque at the center of mass of the actor. This method should be used for torques that are applied over a certain period of time. Use __<font color="#7fb800">add_angular_impulse()</font>__ to apply a torque that only lasts an instant.
        """
    def close_door(self, door_idx: VehicleDoor):
        """
        Close the door door_idx if the vehicle has it. Use carla.VehicleDoor.All to close all available doors.
        """
    def destroy(self) -> bool:
        """
        Tells the simulator to destroy this actor and returns <b>True</b> if it was successful. It has no effect if it was already destroyed.
        """
    def disable_constant_velocity(self):
        """
        Disables any constant velocity previously set for a carla.Vehicle actor.
        """
    def enable_chrono_physics(
        self,
        max_substeps: int,
        max_substep_delta_time: int,
        vehicle_json: str,
        powertrain_json: str,
        tire_json: str,
        base_json_path: str,
    ):
        """
        Enables Chrono physics on a spawned vehicle.
        """
    def enable_constant_velocity(self, velocity: Vector3D):
        """
        Sets a vehicle's velocity vector to a constant value over time. The resulting velocity will be approximately the `velocity` being set, as with __<font color="#7fb800">set_target_velocity()</font>__.
        """
    def get_acceleration(self) -> Vector3D:
        """
        Returns the actor's 3D acceleration vector the client recieved during last tick. The method does not call the simulator.
        """
    def get_angular_velocity(self) -> Vector3D:
        """
        Returns the actor's angular velocity vector the client recieved during last tick. The method does not call the simulator.
        """
    def get_location(self) -> Location:
        """
        Returns the actor's location the client recieved during last tick. The method does not call the simulator.
        """
    def get_transform(self) -> Transform:
        """
        Returns the actor's transform (location and rotation) the client recieved during last tick. The method does not call the simulator.
        """
    def get_velocity(self) -> Vector3D:
        """
        Returns the actor's velocity vector the client recieved during last tick. The method does not call the simulator.
        """
    def get_world(self) -> World:
        """
        Returns the world this actor belongs to.
        """
    def open_door(self, door_idx: VehicleDoor):
        """
        Open the door door_idx if the vehicle has it. Use carla.VehicleDoor.All to open all available doors.
        """
    def set_enable_gravity(self, enabled: bool):
        """
        Enables or disables gravity for the actor. __Default__ is True.
        """
    def set_location(self, location: Location):
        """
        Teleports the actor to a given location.
        """
    def set_simulate_physics(self, enabled: bool):
        """
        Enables or disables the simulation of physics on this actor.
        """
    def set_target_angular_velocity(self, angular_velocity: Vector3D):
        """
        Sets the actor's angular velocity vector. This is applied before the physics step so the resulting angular velocity will be affected by external forces such as friction.
        """
    def set_target_velocity(self, velocity: Vector3D):
        """
        Sets the actor's velocity vector. This is applied before the physics step so the resulting angular velocity will be affected by external forces such as friction.
        """
    def set_transform(self, transform: Transform):
        """
        Teleports the actor to a given transform (location and rotation).
        """
    def show_debug_telemetry(self, enabled: bool):
        """
        Enables or disables the telemetry on this vehicle. This shows information about the vehicles current state and forces applied to it in the spectator window. Only information for one vehicle can be shown so if you enable a second one, the previous will be automatically disabled.
        """
    @property
    def attributes(self) -> dict:
        """
        A dictionary containing the attributes of the blueprint this actor was based on.
        """
    @property
    def id(self) -> int:
        """
        Identifier for this actor. Unique during a given episode.
        """
    @property
    def is_alive(self) -> bool:
        """
        Returns whether this object was destroyed using this actor handle.
        """
    @property
    def parent(self) -> Actor:
        """
        Actors may be attached to a parent actor that they will follow around. This is said actor.
        """
    @property
    def semantic_tags(self) -> list[int]:
        """
        A list of semantic tags provided by the blueprint listing components for this actor. E.g. a traffic light could be tagged with `Pole` and `TrafficLight`. These tags are used by the semantic segmentation sensor. Find more about this and other sensors [here](ref_sensors.md#semantic-segmentation-camera).
        """
    @property
    def type_id(self) -> str:
        """
        The identifier of the blueprint this actor was based on, e.g. `vehicle.ford.mustang`.
        """

class TrafficLight:
    """
    A traffic light actor, considered a specific type of traffic sign. As traffic lights will mostly appear at junctions, they belong to a group which contains the different traffic lights in it. Inside the group, traffic lights are differenciated by their pole index.

      Within a group the state of traffic lights is changed in a cyclic pattern: one index is chosen and it spends a few seconds in green, yellow and eventually red. The rest of the traffic lights remain frozen in red this whole time, meaning that there is a gap in the last seconds of the cycle where all the traffic lights are red. However, the state of a traffic light can be changed manually.
    """
    def __str__(self) -> str: ...
    def freeze(self, freeze: bool):
        """
        Stops all the traffic lights in the scene at their current state.
        """
    def get_affected_lane_waypoints(self) -> list[Waypoint]:
        """
        Returns a list of waypoints indicating the positions and lanes where the traffic light is having an effect.
        """
    def get_elapsed_time(self) -> float:
        """
        The client returns the time in seconds since current light state started according to last tick. The method does not call the simulator.
        """
    def get_green_time(self) -> float:
        """
        The client returns the time set for the traffic light to be green, according to last tick. The method does not call the simulator.
        """
    def get_group_traffic_lights(self) -> list[TrafficLight]:
        """
        Returns all traffic lights in the group this one belongs to.
        """
    def get_light_boxes(self) -> list[BoundingBox]:
        """
        Returns a list of the bounding boxes encapsulating each light box of the traffic light.
        """
    def get_opendrive_id(self) -> str:
        """
        Returns the OpenDRIVE id of this traffic light.
        """
    def get_pole_index(self) -> int:
        """
        Returns the index of the pole that identifies it as part of the traffic light group of a junction.
        """
    def get_red_time(self) -> float:
        """
        The client returns the time set for the traffic light to be red, according to last tick. The method does not call the simulator.
        """
    def get_state(self) -> TrafficLightState:
        """
        The client returns the state of the traffic light according to last tick. The method does not call the simulator.
        """
    def get_stop_waypoints(self) -> list[Waypoint]:
        """
        Returns a list of waypoints indicating the stop position for the traffic light. These waypoints are computed from the trigger boxes of the traffic light that indicate where a vehicle should stop.
        """
    def get_yellow_time(self) -> float:
        """
        The client returns the time set for the traffic light to be yellow, according to last tick. The method does not call the simulator.
        """
    def is_frozen(self) -> bool:
        """
        The client returns <b>True</b> if a traffic light is frozen according to last tick. The method does not call the simulator.
        """
    def reset_group(self):
        """
        Resets the state of the traffic lights of the group to the initial state at the start of the simulation.
        """
    def set_green_time(self, green_time: float): ...
    def set_red_time(self, red_time: float):
        """
        Sets a given time for the red state to be active.
        """
    def set_state(self, state: TrafficLightState):
        """
        Sets a given state to a traffic light actor.
        """
    def set_yellow_time(self, yellow_time: float):
        """
        Sets a given time for the yellow light to be active.
        """
    @property
    def state(self) -> TrafficLightState:
        """
        Current state of the traffic light.
        """

class TrafficLightState(IntEnum):
    """
    All possible states for traffic lights. These can either change at a specific time step or be changed manually. The snipet in carla.TrafficLight.set_state changes the state of a traffic light on the fly.
    """

    Green = auto()
    Off = auto()
    Red = auto()
    Unknown = auto()
    Yellow = auto()

class TrafficSign:
    """
    Traffic signs appearing in the simulation except for traffic lights. These have their own class inherited from this in carla.TrafficLight. Right now, speed signs, stops and yields are mainly the ones implemented, but many others are borne in mind.
    """
    @property
    def trigger_volume(self):
        """
        A carla.BoundingBox situated near a traffic sign where the carla.Actor who is inside can know about it.
        """

class Vehicle:
    """
    One of the most important group of actors in CARLA. These include any type of vehicle from cars to trucks, motorbikes, vans, bycicles and also official vehicles such as police cars. A wide set of these actors is provided in carla.BlueprintLibrary to facilitate differente requirements. Vehicles can be either manually controlled or set to an autopilot mode that will be conducted client-side by the <b>traffic manager</b>.
    """
    def __str__(self) -> str: ...
    def apply_control(self, control: VehicleControl):
        """
        Applies a control object on the next tick, containing driving parameters such as throttle, steering or gear shifting.
        """
    def apply_physics_control(self, physics_control: VehiclePhysicsControl):
        """
        Applies a physics control object in the next tick containing the parameters that define the vehicle as a corporeal body. E.g.: moment of inertia, mass, drag coefficient and many more.
        """
    def enable_carsim(self, simfile_path: str):
        """
        Enables the CarSim physics solver for this particular vehicle. In order for this function to work, there needs to be a valid license manager running on the server side. The control inputs are redirected to CarSim which will provide the position and orientation of the vehicle for every frame.
        """
    def get_control(self) -> VehicleControl:
        """
        The client returns the control applied in the last tick. The method does not call the simulator.
        """
    def get_failure_state(self) -> VehicleFailureState:
        """
        Vehicle have failure states, to  indicate that it is incapable of continuing its route. This function returns the vehicle's specific failure state, or in other words, the cause that resulted in it.
        """
    def get_light_state(self) -> VehicleLightState:
        """
        Returns a flag representing the vehicle light state, this represents which lights are active or not.
        """
    def get_physics_control(self) -> VehiclePhysicsControl:
        """
        The simulator returns the last physics control applied to this vehicle.
        """
    def get_speed_limit(self) -> float:
        """
        The client returns the speed limit affecting this vehicle according to last tick (it does not call the simulator). The speed limit is updated when passing by a speed limit signal, so a vehicle might have none right after spawning.
        """
    def get_traffic_light(self) -> TrafficLight:
        """
        Retrieves the traffic light actor affecting this vehicle (if any) according to last tick. The method does not call the simulator.
        """
    def get_traffic_light_state(self) -> TrafficLightState:
        """
        The client returns the state of the traffic light affecting this vehicle according to last tick. The method does not call the simulator. If no traffic light is currently affecting the vehicle, returns <b>green</b>.
        """
    def get_wheel_steer_angle(self, wheel_location: VehicleWheelLocation) -> float:
        """
        Returns the physics angle in degrees of a vehicle's wheel.
        """
    def is_at_traffic_light(self) -> bool:
        """
        Vehicles will be affected by a traffic light when the light is red and the vehicle is inside its bounding box. The client returns whether a traffic light is affecting this vehicle according to last tick (it does not call the simulator).
        """
    def set_autopilot(self, enabled: bool, port: int):
        """
        Registers or deletes the vehicle from a Traffic Manager's list. When __True__, the Traffic Manager passed as parameter will move the vehicle around. The autopilot takes place client-side.
        """
    def set_light_state(self, light_state: VehicleLightState):
        """
        Sets the light state of a vehicle using a flag that represents the lights that are on and off.
        """
    def set_wheel_steer_direction(
        self, wheel_location: VehicleWheelLocation, angle_in_deg: float
    ):
        """
        Sets the angle of a vehicle's wheel visually.
        """
    def use_carsim_road(self, enabled: bool):
        """
        Enables or disables the usage of CarSim vs terrain file specified in the `.simfile`. By default this option is disabled and CarSim uses unreal engine methods to process the geometry of the scene.
        """
    @property
    def bounding_box(self) -> BoundingBox:
        """
        Bounding box containing the geometry of the vehicle. Its location and rotation are relative to the vehicle it is attached to.
        """

class VehicleDoor(IntEnum):
    """
    Possible index representing the possible doors that can be open. Notice that not all possible doors are able to open in some vehicles.
    """

    All = auto()
    FL = auto()
    FR = auto()
    RL = auto()
    RR = auto()

class VehicleFailureState(IntEnum):
    """
    Enum containing the different failure states of a vehicle, from which the it cannot recover. These are returned by __<font color="#7fb800">get_failure_state()</font>__ and only Rollover is currently implemented.
    """

    Engine = auto()
    NONE = auto()
    Rollover = auto()
    TirePuncture = auto()

class VehicleLightState(IntEnum):
    """
    Class that recaps the state of the lights of a vehicle, these can be used as a flags. E.g: `VehicleLightState.HighBeam & VehicleLightState.Brake` will return `True` when both are active. Lights are off by default in any situation and should be managed by the user via script. The blinkers blink automatically. _Warning: Right now, not all vehicles have been prepared to work with this functionality, this will be added to all of them in later updates_
    """

    All = auto()
    Brake = auto()
    Fog = auto()
    HighBeam = auto()
    Interior = auto()
    LeftBlinker = auto()
    LowBeam = auto()
    NONE = auto()
    Position = auto()
    Reverse = auto()
    RightBlinker = auto()
    Special1 = auto()
    Special2 = auto()

class VehicleWheelLocation(IntEnum):
    """
    `enum` representing the position of each wheel on a vehicle.  Used to identify the target wheel when setting an angle in carla.Vehicle.set_wheel_steer_direction or carla.Vehicle.get_wheel_steer_angle.
    """

    BL_Wheel = auto()
    BR_Wheel = auto()
    Back_Wheel = auto()
    FL_Wheel = auto()
    FR_Wheel = auto()
    Front_Wheel = auto()

class Walker:
    """
    This class inherits from the carla.Actor and defines pedestrians in the simulation. Walkers are a special type of actor that can be controlled either by an AI (carla.WalkerAIController) or manually via script, using a series of carla.WalkerControl to move these and their skeletons.
    """
    def __str__(self) -> str: ...
    def apply_control(self, control: WalkerControl):
        """
        On the next tick, the control will move the walker in a certain direction with a certain speed. Jumps can be commanded too.
        """
    def blend_pose(self, blend_value: float):
        """
        Set the blending value of the custom pose with the animation. The values can be:
          - 0: will show only the animation
          - 1: will show only the custom pose (set by the user with set_bones())
          - any other: will interpolate all the bone positions between animation and the custom pose
        """
    def get_bones(self) -> WalkerBoneControlOut:
        """
        Return the structure with all the bone transformations from the actor. For each bone, we get the name and its transform in three different spaces:
          - name: bone name
          - world: transform in world coordinates
          - component: transform based on the pivot of the actor
          - relative: transform based on the bone parent
        """
    def get_control(self) -> WalkerControl:
        """
        The client returns the control applied to this walker during last tick. The method does not call the simulator.
        """
    def get_pose_from_animation(self):
        """
        Make a copy of the current animation frame as the custom pose. Initially the custom pose is the neutral pedestrian pose.
        """
    def hide_pose(self):
        """
        Hide the custom pose and show the animation (same as calling blend_pose(0))
        """
    def set_bones(self, bones: WalkerBoneControlIn):
        """
        Set the bones of the actor. For each bone we want to set we use a relative transform. Only the bones in this list will be set. For each bone you need to setup this info:
          - name: bone name
          - relative: transform based on the bone parent
        """
    def show_pose(self):
        """
        Show the custom pose and hide the animation (same as calling blend_pose(1))
        """
    @property
    def bounding_box(self) -> BoundingBox:
        """
        Bounding box containing the geometry of the walker. Its location and rotation are relative to the walker it is attached to.
        """

class WalkerAIController:
    """
    Class that conducts AI control for a walker. The controllers are defined as actors, but they are quite different from the rest. They need to be attached to a parent actor during their creation, which is the walker they will be controlling (take a look at carla.World if you are yet to learn on how to spawn actors). They also need for a special blueprint (already defined in carla.BlueprintLibrary as "controller.ai.walker"). This is an empty blueprint, as the AI controller will be invisible in the simulation but will follow its parent around to dictate every step of the way.
    """
    def __str__(self) -> str: ...
    def go_to_location(self, destination: Location):
        """
        Sets the destination that the pedestrian will reach.
        """
    def set_max_speed(self, speed: float):
        """
        Sets a speed for the walker in meters per second.
        """
    def start(self):
        """
        Enables AI control for its parent walker.
        """
    def stop(self):
        """
        Disables AI control for its parent walker.
        """
