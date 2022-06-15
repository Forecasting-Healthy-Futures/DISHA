"""This module is created to facilitate the use of the library. It provides ways to
perform end-to-end operation such as model training or generation.
A :class:`__call__` function is defined and used to launch the Pipeline. """


from .Weather_Forecast import WeatherForecast

__all__ = ['WeatherForecast']