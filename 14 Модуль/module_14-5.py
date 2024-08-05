from aiogram import Bot, Dispatcher, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import crud_functions5

# *************************************************************************
api = '7100837638:AAFH00gqytpiU6JKLVfdt6TrAAJDEg1GfI0'
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())
# *************************************************************************

kb = InlineKeyboardMarkup()
button = InlineKeyboardButton(text='Регистрация', callback_data='Регистрация')
kb.add(button)


class RegistrationState(StatesGroup):
    username = State()
    email = State()
    age = State()
    balance = 1000


@dp.message_handler(commands=['start'])
async def starter(message):
    await message.answer('Привет ! Я бот, помогающий твоему здоровью', reply_markup=kb)


@dp.callback_query_handler(text='Регистрация')
async def sign_up(call, state):
    await call.message.answer('Введите имя пользователя (только латинский алфавит):')
    data = await state.get_data()
    await RegistrationState.username.set()


@dp.message_handler(state=RegistrationState.username)
async def set_username(message, state):
    await state.update_data(first=message.text)
    data = await state.get_data()
    await message.answer('Введите свой email')
    await RegistrationState.email.set()
#    print(data)


@dp.message_handler(state=RegistrationState.email)
async def set_email(message, state):
    await state.update_data(second=message.text)
    data = await state.get_data()
    await message.answer('Введите свой возраст')
    await RegistrationState.age.set()
#    print(data)


@dp.message_handler(state=RegistrationState.age)
async def set_age(message, state):
    await state.update_data(third=message.text)
    data = await state.get_data()
    print(data)
    print('------------------------')
    new_user = crud_functions5.is_included(data['first'])
    if new_user is None:
        crud_functions5.add_user(data['first'], data['second'], data['third'])
        await message.answer('Регистрация прошла успешно! Поздравляем!')
    else:
        print('Пользователь существует, введите другое имя')
        await message.answer('Пользователь существует, введите другое имя')
    users = crud_functions5.get_all_users()
    for user in users:
        print(f"username: {user[1]} |", f"email: {user[2]} |", f"age: {user[3]}", f"balance: {user[4]}")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

