from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup


class CoordinatesForm(StatesGroup):
    width = State()
    longitude = State()


# """Для старта поиска необходимо написать: /start"""
async def start_user_dialog(message: types.Message):
    await CoordinatesForm.width.set()
    await message.answer("напишите широту:")
    # await CoordinatesForm.next()


async def process_width(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        # сохраяем данные о широте
        data['width'] = message.text

        await CoordinatesForm.next()
        await message.answer("напишите долготу:")


async def process_longitude(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        # сохраяем данные о долготе
        data['longitude'] = message.text

        await state.finish()
        await message.answer(data)
        print(data)
