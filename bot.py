from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
import weather as weather
import log

from config import BOT_TOKEN

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.reply("Привет!\n Этот бот поможет тебе узнать текущую погоду или прогноз погоды в интересующем тебя городе")
    log.write(message.from_user, 'bot is started')

@dp.message_handler(commands=['help'])
async def process_help_command(message: types.Message):
    await message.reply("Напиши /temperature <Название города>, чтобы узнать погоду в интересущем тебя городе\n Напиши /tomorrow <Название города>, чтобы узнать прогноз погоды на завтра в интересущем тебя городе")
    log.write(message.from_user, 'ask for help')

@dp.message_handler(commands=['temperature'])
async def weather_message(message: types.Message):
    argument = message.get_args()
    if not argument:
        argument = 'Yekaterinburg'
    answer = "Температура на улице %s" % (weather.current_temperature(argument))
    await bot.send_message(message.from_user.id, answer)
    log.write(message.from_user, 'ask for temperature')

@dp.message_handler(commands=['tomorrow'])
async def weather_message(message: types.Message):
    argument = message.get_args()
    if not argument:
        argument = 'Yekaterinburg'
    answer = "Температура на завтра в это же время %s" % (weather.tomorrow_temperature(argument))
    await bot.send_message(message.from_user.id, answer)
    log.write(message.from_user, 'ask for tomorrow temperature')

if __name__ == '__main__':
    executor.start_polling(dp)