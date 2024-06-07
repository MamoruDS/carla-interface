from ._c.traffic_manager import Action, ActionBuffer
from .actor import Actor
from typing import List


class TrafficManager:
    def get_port(self) -> int:
        raise NotImplementedError

    def vehicle_percentage_speed_difference(
        self, _actor: Actor, _percentage: float
    ) -> None:
        """
        Set a vehicle's % decrease in velocity with respect to the speed limit.
        If less than 0, it's a % increase.
        """
        raise NotImplementedError

    def global_percentage_speed_difference(self, _percentage: float) -> None:
        """
        Set a global % decrease in velocity with respect to the speed limit.
        If less than 0, it's a % increase.
        """
        raise NotImplementedError

    def update_vehicle_lights(self, _actor: Actor, _do_update: bool) -> None:
        """
        Set the automatic management of the vehicle lights
        """
        raise NotImplementedError

    def collision_detection(
        self,
        _reference_actor: Actor,
        _other_actor: Actor,
        _detect_collision: bool,
    ) -> None:
        """
        Method to set collision detection rules between vehicles.
        """
        raise NotImplementedError

    def force_lane_change(self, _actor: Actor, _direction: bool) -> None:
        """
        Method to force lane change on a vehicle.
        Direction flag can be set to true for left and false for right.
        """
        raise NotImplementedError

    def auto_lane_change(self, _actor: Actor, _enable: bool) -> None:
        """
        Enable/disable automatic lane change on a vehicle.
        """
        raise NotImplementedError

    def distance_to_leading_vehicle(
        self, _actor: Actor, _distance: float
    ) -> None:
        """
        Method to specify how much distance a vehicle should maintain to
        the leading vehicle.
        """
        raise NotImplementedError

    def ignore_walkers_percentage(self, _actor: Actor, _perc: float) -> None:
        """
        Method to specify the % chance of ignoring collisions with any walker.
        """
        raise NotImplementedError

    def ignore_vehicles_percentage(self, _actor: Actor, _perc: float) -> None:
        """
        Method to specify the % chance of ignoring collisions with any vehicle.
        """
        raise NotImplementedError

    def ignore_lights_percentage(self, _actor: Actor, _perc: float) -> None:
        """
        Method to specify the % chance of running a light.
        """
        raise NotImplementedError

    def ignore_signs_percentage(self, _actor: Actor, _perc: float) -> None:
        """
        Method to specify the % chance of running a sign.
        """
        raise NotImplementedError

    def set_global_distance_to_leading_vehicle(self, _distance: float) -> None:
        """
        Method to Set Global distance to Leading vehicle
        """
        raise NotImplementedError

    def keep_right_rule_percentage(
        self, _actor: Actor, _precentage: float
    ) -> None:
        """
        Method to set % to keep on the right lane.
        """
        raise NotImplementedError

    def random_left_lanechange_percentage(
        self, _actor: Actor, _precentage: float
    ) -> None:
        """
        Method to set % to randomly do a left lane change.
        """
        raise NotImplementedError

    def random_right_lanechange_percentage(
        self, _actor: Actor, _precentage: float
    ) -> None:
        """
        Method to set % to randomly do a right lane change.
        """
        raise NotImplementedError

    def set_synchronous_mode(self, _mode: bool) -> None:
        """
        Method to switch traffic manager into synchronous execution.
        """
        raise NotImplementedError

    def set_hybrid_physics_mode(self, _mode_switch: bool) -> None:
        """
        This method sets the hybrid physics mode.
        """
        raise NotImplementedError

    def set_hybrid_physics_radius(self, _radius: float) -> None:
        """
        This method sets the hybrid physics radius.
        """
        raise NotImplementedError

    def set_random_device_seed(self, _seed: int) -> None:
        """
        Method to set randomization seed.
        """
        raise NotImplementedError

    def set_osm_mode(self, _mode_switch: bool) -> None:
        """
        Method to set Open Street Map mode.
        """
        raise NotImplementedError

    def set_path(self, empty_buffer: bool = True) -> None:
        """
        Method to set our own imported path.
        """
        raise NotImplementedError

    def set_route(self, empty_buffer: bool = True) -> None:
        """
        Method to set our own imported route.
        """
        raise NotImplementedError

    def set_respawn_dormant_vehicles(self, _mode_switch: bool) -> None:
        """
        Method to set if we are automatically respawning vehicles.
        """
        raise NotImplementedError

    def set_boundaries_respawn_dormant_vehicles(
        self, _lower_bound: float, _upper_bound: float
    ) -> None:
        """
        Method to set boundaries for respawning vehicles.
        """
        raise NotImplementedError

    def get_next_action(self) -> List[Action]:
        """
        Method to get the next action.
        """
        raise NotImplementedError

    def get_all_actions(self) -> ActionBuffer:
        """
        Method to get the action buffer.
        """
        raise NotImplementedError

    def shut_down(self) -> None:
        raise NotImplementedError
