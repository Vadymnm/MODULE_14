from aiogram import Bot, Dispatcher, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
import crud_functions5

# *************************************************************************
api = ''
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())
# *************************************************************************

but = KeyboardButton(text='Регистрация')
kb = ReplyKeyboardMarkup(resize_keyboard=True)
kb.add(but)


class RegistrationState(StatesGroup):
    username = State()
    email = State()
    age = State()
    balance = 1000


@dp.message_handler(commands=['start'])
async def starter(message):
    await message.answer('Привет ! Я бот, помогающий твоему здоровью', reply_markup=kb)


@dp.message_handler(text='Регистрация')
async def sign_up(message):
    await message.answer('Введите имя пользователя (только латинский алфавит):')
    print('Введите имя пользователя (только латинский алфавит):')
    await RegistrationState.username.set()


@dp.message_handler(state=RegistrationState.username)
async def set_username(message, state):
    await state.update_data(first=message.text)
    data = await state.get_data()
    new_user = crud_functions5.is_included(data['first'])
    if new_user is not None:
        print('Пользователь существует, введите другое имя')
        await message.answer('Пользователь существует, введите другое имя')
        await message.reply()
    await state.update_data(first=message.text)
    data = await state.get_data()

    await message.answer('Введите свой email')
    await RegistrationState.email.set()
    print(data)


@dp.message_handler(state=RegistrationState.email)
async def set_email(message, state):
    await state.update_data(second=message.text)
    data = await state.get_data()
    await message.answer('Введите свой возраст')
    await RegistrationState.age.set()
    print(data)


@dp.message_handler(state=RegistrationState.age)
async def set_age(message, state):
    await state.update_data(third=message.text)
    data = await state.get_data()
    print(data)
    print('------------------------')
    crud_functions5.add_user(data['first'], data['second'], data['third'])
    await message.answer('Регистрация прошла успешно! Поздравляем!')
    users = crud_functions5.get_all_users()
    for user in users:
        print(f"username: {user[1]} |", f"email: {user[2]} |", f"age: {user[3]}", f"balance: {user[4]}")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
