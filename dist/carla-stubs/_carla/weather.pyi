from typing_extensions import Self

class WeatherParameters:
    """
    This class defines objects containing lighting and weather specifications that can later be applied in carla.World. So far, these conditions only intervene with [sensor.camera.rgb](ref_sensors.md#rgb-camera). They neither affect the actor's physics nor other sensors.
      Each of these parameters acts indepently from the rest. Increasing the rainfall will not automatically create puddles nor change the road's humidity. That makes for a better customization but means that realistic conditions need to be scripted. However an example of dynamic weather conditions working realistically can be found [here](https://github.com/carla-simulator/carla/blob/master/PythonAPI/examples/dynamic_weather.py).
    """
    def __eq__(self, other: Self) -> bool:
        """
        Returns <b>True</b> if both objects' variables are the same.
        """
    def __init__(
        self,
        cloudiness: float,
        precipitation: float,
        precipitation_deposits: float,
        wind_intensity: float,
        sun_azimuth_angle: float,
        sun_altitude_angle: float,
        fog_density: float,
        fog_distance: float,
        wetness: float,
        fog_falloff: float,
        scattering_intensity: float,
        mie_scattering_scale: float,
        rayleigh_scattering_scale: float,
    ):
        """
        Method to initialize an object defining weather conditions. This class has some presets for different noon and sunset conditions listed in a note below.
        """
    def __ne__(self, other: Self) -> bool:
        """
        Returns <b>True</b> if both objects' variables are different.
        """
    def __str__(self) -> str: ...
    @property
    def cloudiness(self) -> float:
        """
        Values range from 0 to 100, being 0 a clear sky and 100 one completely covered with clouds.
        """
    @property
    def dust_storm(self) -> float:
        """
        Determines the strength of the dust storm weather. Values range from 0 to 100.
        """
    @property
    def fog_density(self) -> float:
        """
        Fog concentration or thickness. It only affects the RGB camera sensor. Values range from 0 to 100.
        """
    @property
    def fog_distance(self) -> float:
        """
        Fog start distance. Values range from 0 to infinite.
        """
    @property
    def fog_falloff(self) -> float:
        """
        Density of the fog (as in specific mass) from 0 to infinity. The bigger the value, the more dense and heavy it will be, and the fog will reach smaller heights. Corresponds to <a href="https://docs.unrealengine.com/en-US/Engine/Actors/FogEffects/HeightFog/index.html#:~:text=Using%20Exponential%20Height%20Fog%20Features,-The%20sections%20below&text=Add%20a%20second%20fog%20layer,height%20falloff%2C%20and%20height%20offset">Fog Height Falloff</a> in the UE docs. <br> If the value is 0, the fog will be lighter than air, and will cover the whole scene. <br> A value of 1 is approximately as dense as the air, and reaches normal-sized buildings. <br> For values greater than 5, the air will be so dense that it will be compressed on ground level.
        """
    @property
    def mie_scattering_scale(self) -> float:
        """
        Controls interaction of light with large particles like pollen or air pollution resulting in a hazy sky with halos around the light sources. When set to 0, there is no contribution.
        """
    @property
    def precipitation(self) -> float:
        """
        Rain intensity values range from 0 to 100, being 0 none at all and 100 a heavy rain.
        """
    @property
    def precipitation_deposits(self) -> float:
        """
        Determines the creation of puddles. Values range from 0 to 100, being 0 none at all and 100 a road completely capped with water. Puddles are created with static noise, meaning that they will always appear at the same locations.
        """
    @property
    def rayleigh_scattering_scale(self) -> float:
        """
        Controls interaction of light with small particles like air molecules. Dependent on light wavelength, resulting in a blue sky in the day or red sky in the evening.
        """
    @property
    def scattering_intensity(self) -> float:
        """
        Controls how much the light will contribute to volumetric fog. When set to 0, there is no contribution.
        """
    @property
    def sun_altitude_angle(self) -> float:
        """
        Altitude angle of the sun. Values range from -90 to 90 corresponding to midnight and midday each.
        """
    @property
    def sun_azimuth_angle(self) -> float:
        """
        The azimuth angle of the sun. Values range from 0 to 360. Zero is an origin point in a sphere determined by Unreal Engine.
        """
    @property
    def wetness(self) -> float:
        """
        Wetness intensity. It only affects the RGB camera sensor. Values range from 0 to 100.
        """
    @property
    def wind_intensity(self) -> float:
        """
        Controls the strenght of the wind with values from 0, no wind at all, to 100, a strong wind. The wind does affect rain direction and leaves from trees, so this value is restricted to avoid animation issues.
        """
