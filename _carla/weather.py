# https://github.com/carla-simulator/carla/blob/master/PythonAPI/carla/source/libcarla/Weather.cpp
from __future__ import annotations
from typing_extensions import Self


# https://github.com/carla-simulator/carla/blob/master/LibCarla/source/carla/rpc/WeatherParameters.h
class WeatherParameters:
    def __init__(
        self,
        cloudiness: float = 0.0,
        precipitation: float = 0.0,
        precipitation_deposits: float = 0.0,
        wind_intensity: float = 0.0,
        sun_azimuth_angle: float = 0.0,
        sun_altitude_angle: float = 0.0,
        fog_density: float = 0.0,
        fog_distance: float = 0.0,
        fog_falloff: float = 0.0,
        wetness: float = 0.0,
        scattering_intensity: float = 0.0,
        mie_scattering_scale: float = 0.0,
        rayleigh_scattering_scale: float = 0.0331,
    ) -> None:
        raise NotImplementedError

    @property
    def cloudiness(self) -> float:
        raise NotImplementedError

    @cloudiness.setter
    def cloudiness(self, val: float) -> None:
        raise NotImplementedError

    @property
    def precipitation(self) -> float:
        raise NotImplementedError

    @precipitation.setter
    def precipitation(self, val: float) -> None:
        raise NotImplementedError

    @property
    def precipitation_deposits(self) -> float:
        raise NotImplementedError

    @precipitation_deposits.setter
    def precipitation_deposits(self, val: float) -> None:
        raise NotImplementedError

    @property
    def wind_intensity(self) -> float:
        raise NotImplementedError

    @wind_intensity.setter
    def wind_intensity(self, val: float) -> None:
        raise NotImplementedError

    @property
    def sun_azimuth_angle(self) -> float:
        raise NotImplementedError

    @sun_azimuth_angle.setter
    def sun_azimuth_angle(self, val: float) -> None:
        raise NotImplementedError

    @property
    def sun_altitude_angle(self) -> float:
        raise NotImplementedError

    @sun_altitude_angle.setter
    def sun_altitude_angle(self, val: float) -> None:
        raise NotImplementedError

    @property
    def fog_density(self) -> float:
        raise NotImplementedError

    @fog_density.setter
    def fog_density(self, val: float) -> None:
        raise NotImplementedError

    @property
    def fog_distance(self) -> float:
        raise NotImplementedError

    @fog_distance.setter
    def fog_distance(self, val: float) -> None:
        raise NotImplementedError

    @property
    def fog_falloff(self) -> float:
        raise NotImplementedError

    @fog_falloff.setter
    def fog_falloff(self, val: float) -> None:
        raise NotImplementedError

    @property
    def wetness(self) -> float:
        raise NotImplementedError

    @wetness.setter
    def wetness(self, val: float) -> None:
        raise NotImplementedError

    @property
    def scattering_intensity(self) -> float:
        raise NotImplementedError

    @scattering_intensity.setter
    def scattering_intensity(self, val: float) -> None:
        raise NotImplementedError

    @property
    def mie_scattering_scale(self) -> float:
        raise NotImplementedError

    @mie_scattering_scale.setter
    def mie_scattering_scale(self, val: float) -> None:
        raise NotImplementedError

    @property
    def rayleigh_scattering_scale(self) -> float:
        raise NotImplementedError

    @rayleigh_scattering_scale.setter
    def rayleigh_scattering_scale(self, val: float) -> None:
        raise NotImplementedError

    def __eq__(self, __o: Self) -> bool:
        raise NotImplementedError

    def __ne__(self, __o: Self) -> bool:
        raise NotImplementedError

    def __str__(self) -> str:
        raise NotImplementedError

    Default: WeatherParameters
    ClearNoon: WeatherParameters
    CloudyNoon: WeatherParameters
    WetNoon: WeatherParameters
    WetCloudyNoon: WeatherParameters
    MidRainyNoon: WeatherParameters
    HardRainNoon: WeatherParameters
    SoftRainNoon: WeatherParameters
    ClearSunset: WeatherParameters
    CloudySunset: WeatherParameters
    WetSunset: WeatherParameters
    WetCloudySunset: WeatherParameters
    MidRainSunset: WeatherParameters
    HardRainSunset: WeatherParameters
    SoftRainSunset: WeatherParameters
    ClearNight: WeatherParameters
    CloudyNight: WeatherParameters
    WetNight: WeatherParameters
    WetCloudyNight: WeatherParameters
    SoftRainNight: WeatherParameters
    MidRainyNight: WeatherParameters
    HardRainNight: WeatherParameters
