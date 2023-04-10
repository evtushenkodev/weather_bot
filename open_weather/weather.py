from config import owm


def get_weather_info(latitude, longitude):
    """
    Функция получает текущие метрики погоды на указанных координатах и
    возвращает строку с информацией о температуре в градусах Цельсия,
    влажности в процентах, скорости ветра в м/с и облачности в процентах.
    """
    try:
        mgr = owm.weather_manager()
        observation = mgr.weather_at_coords(latitude, longitude)
        weather = observation.weather
        temperature = int(weather.temperature("celsius")["temp"])
        humidity = weather.humidity
        wind_speed = weather.wind()["speed"]
        clouds = weather.clouds

        result = f"• температура - {temperature}°\n• влажность - {humidity}%\n" \
                 f"• скорость ветра - {wind_speed} м/с\n• облачность - {clouds}%"
        return result
    except ConnectionError:
        print("Could not connect to OpenWeatherMap API.")
        return None
