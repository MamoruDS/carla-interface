# https://github.com/carla-simulator/carla/blob/master/PythonAPI/carla/source/libcarla/Sensor.cpp
from .actor import Actor
from typing import Callable


class Sensor(Actor):
    @property
    def is_listening(self) -> bool:
        raise NotImplementedError

    def listen(self, callback: Callable) -> None:  # TODO: cb parameter hinting
        raise NotImplementedError

    def stop(self) -> None:
        raise NotImplementedError

    def __str__(self) -> str:
        raise NotImplementedError


class ServerSideSensor(Sensor):
    ...


class ClientSideSensor(Sensor):
    ...


class LaneInvasionSensor(Sensor):
    ...
