from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup

from open_weather.weather import get_weather_info


class CoordinatesForm(StatesGroup):
    latitude = State()
    longitude = State()


async def start_user_dialog(message: types.Message):
    """Запускает FSM для сохранения координат,
    для старта поиска необходимо написать: /start"""
    await CoordinatesForm.latitude.set()
    await message.answer("Введите широту:")


async def process_latitude(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        # сохраяем данные о широте
        try:
            latitude = float(message.text)
        except ValueError:
            await message.answer("Широта должна быть числом, попробуйте еще раз.")
            return

        data['latitude'] = latitude
        await CoordinatesForm.next()
        await message.answer("Введите долготу:")


async def process_longitude(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        # сохраяем данные о долготе
        try:
            longitude = float(message.text)
        except ValueError:
            await message.answer("Долгота должна быть числом, попробуйте еще раз.")
            return

        data['longitude'] = longitude
        await state.finish()
        weather = get_weather_info(data['latitude'], data['longitude'])
        await message.answer(weather)

        print(weather)
