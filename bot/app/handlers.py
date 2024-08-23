from aiogram import Router, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, CallbackQuery, FSInputFile
from aiogram.fsm.state import State, StatesGroup, default_state
from aiogram.fsm.context import FSMContext

import app.keyboard as kb


router = Router()
class Register(StatesGroup):
	name = State()
	age = State()
	number = State()


@router.message(CommandStart())
async def cmd_start(message: Message):
	await message.answer("Привет!", reply_markup=kb.main_keyboard)


@router.message(F.text == 'Каталог')
async def catalog(message: Message):
	await message.answer('Выберите категорию товара', reply_markup=kb.catalog_keyboard)


@router.callback_query(F.data == 'tshirt')
async def tshirt(callback: CallbackQuery):
	await callback.answer()
	await callback.message.answer_photo(photo = FSInputFile('bot/media/tshirt.jpg'),
	                                    caption = 'Вы выбрали категорию футболок', reply_markup=kb.main_keyboard)
	await callback.message.delete()


@router.callback_query(F.data == 'sneakers')
async def tshirt(callback: CallbackQuery):
	await callback.answer()
	await callback.message.answer_photo(photo = FSInputFile('bot/media/sneakers.png'),
	                                    caption = 'Вы выбрали категорию кроссовок', reply_markup=kb.main_keyboard)
	await callback.message.delete()


@router.callback_query(F.data == 'cap')
async def tshirt(callback: CallbackQuery):
	await callback.answer()
	await callback.message.answer_photo(photo = FSInputFile('bot/media/cap.png'),
	                                    caption = 'Вы выбрали категорию кепок', reply_markup=kb.main_keyboard)
	await callback.message.delete()

@router.message(F.text == 'Регистрация')
async def register (message: Message, state: FSMContext):
	await state.set_state(Register.name)
	await message.answer('Введите ваше имя')


@router.message(Register.name)
async def register_name(message: Message, state: FSMContext):
	await state.update_data(name = message.text)
	await state.set_state(Register.age)
	await message.answer('Введте ваш возраст')

@router.message(Register.age)
async def register_age(message: Message, state: FSMContext):
	await state.update_data(age=message.text)
	await state.set_state(Register.number)
	await message.answer('Отправьте ваш номер телефона', reply_markup=kb.get_number)

@router.message(Register.number, F.contact)
async def register_number(message: Message, state: FSMContext):
	await state.update_data(number=message.contact.phone_number)
	data = await state.get_data()
	await message.answer(f'Вас зовут: {data['name']}\nВаш возраст: {data['age']}\nВаш номер телефона: {data['number']}',
	                     reply_markup=kb.main_keyboard)
	await state.clear()
