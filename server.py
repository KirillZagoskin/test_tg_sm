import os

from aiogram import Bot, Dispatcher, executor, types

from service import send_message 

API_TOKEN = os.getenv('TELEGRAM_API_TOKEN')

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler()
async def send_welcome(message: types.Message):
    user_id = message.from_user.id
    username = message.from_user.username
    msg = send_message(user_id, username)

    await message.answer(text=msg)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)