from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
import weather as w

from config import BOT_TOKEN

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.reply("Привет!\n Этот бот поможет тебе узнать погоду в интересующем тебя городе")

@dp.message_handler(commands=['help'])
async def process_help_command(message: types.Message):
    await message.reply("Напиши /weather <Название города>, чтобы узнать погоду в интересущем тебя городе")

@dp.message_handler(commands=['weather'])
async def weather_message(message: types.Message):
    argument = message.get_args()
    if not argument:
        argument = 'Yekaterinburg'
    answer = "Температура на улице %s" % (w.current_weather(argument))
    await bot.send_message(message.from_user.id, answer)

if __name__ == '__main__':
    executor.start_polling(dp)