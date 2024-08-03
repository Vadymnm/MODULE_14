from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.types import InputFile
import crud_functions

# *************************************************************************

api = ''
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())

but1 = KeyboardButton(text='Информация')
but2 = KeyboardButton(text='Рассчитать')
but3 = KeyboardButton(text='Купить')
markup1 = ReplyKeyboardMarkup(resize_keyboard=True).row(but2, but1).add(but3)

butt1 = InlineKeyboardButton(text='Product1', callback_data='product_buying')
butt2 = InlineKeyboardButton(text='Product2', callback_data='product_buying')
butt3 = InlineKeyboardButton(text='Product3', callback_data='product_buying')
butt4 = InlineKeyboardButton(text='Product4', callback_data='product_buying')
kb = InlineKeyboardMarkup(resize_keyboard=True).row(butt1, butt2, butt3, butt4)

# *************************************************************************
@dp.message_handler(commands=['start'])
async def starter(message):
    await message.answer('Привет ! Я бот, помогающий твоему здоровью', reply_markup=markup1)

@dp.message_handler(text=['Купить'])
async def get_buying_list(message):
    await message.answer('Список товаров и  меню  покупки:')
    users = crud_functions.get_all_products()
    for user in users:
        print(f"Название: {user[1]} |", f"Описание: {user[2]} |", f"Цена: {user[3]}")
        str_out = (f"Название: {user[1]} |", f"Описание: {user[2]} |", f"Цена: {user[3]}")
        img_name = user[1] + '.jpg'
#        print(img_name)
        photo = InputFile(img_name)
        await message.answer(str_out)
        await bot.send_photo(chat_id=message.chat.id, photo=photo)
    await message.answer('Выберите товар для  покупки:', reply_markup=kb)

    print('==============================================')

@dp.callback_query_handler(text=['product_buying'])
async def send_confirm_message(call):
    await call.message.answer('** Успешная  покупка !!! **')
    print('----------------------------')
    await call.answer()

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
