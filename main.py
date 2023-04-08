from aiogram.utils import executor

from config import dp

from weather_handler.coordinates_fsm import (
    CoordinatesForm,
    start_user_dialog,
    process_width,
    process_longitude
)

if __name__ == '__main__':
    print(__name__)
    dp.register_message_handler(start_user_dialog, commands=["start"])
    dp.register_message_handler(process_width, state=CoordinatesForm.width)
    dp.register_message_handler(process_longitude, state=CoordinatesForm.longitude)
    executor.start_polling(dp, skip_updates=True)
