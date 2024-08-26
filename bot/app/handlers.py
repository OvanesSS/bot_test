from aiogram import Router, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, CallbackQuery, FSInputFile
from aiogram.fsm.state import State, StatesGroup, default_state
from aiogram.fsm.context import FSMContext

import bot.app.keyboard as kb
import bot.app.database.requests as rq

router = Router()


@router.message(CommandStart())
async def cmd_start(message: Message):
	await rq.set_user(message.from_user.id)
	await message.answer("Добро пожаловать в магазин кроссовок!", reply_markup=kb.main_keyboard)


@router.message(F.text=='Каталог')
async def catalog(message: Message):
	await message.answer('Выберите категорию товара', reply_markup=await kb.categories())


@router.callback_query(F.data.startswith('category_'))
async def category(callback: CallbackQuery):
	await callback.answer('Вы выбрали категорию')
	await callback.message.answer('Выберите товар',
	                              reply_markup=await kb.get_category_items(callback.data.split('_')[1]))


"""@router.callback_query(F.data == 'cap')
async def tshirt(callback: CallbackQuery):
	await callback.answer()
	try:
		await callback.message.answer_photo(photo=id_files['cap'],
		                                    caption='Вы выбрали категорию кепок',
		                                    reply_markup=kb.main_keyboard)
	except KeyError:
		message_id = await callback.message.answer_photo(photo=FSInputFile('bot/media/cap.png'),
		                                                 caption='Вы выбрали категорию кепок',
		                                                 reply_markup=kb.main_keyboard)

		id_files['cap'] = message_id.photo[-1].file_id
	await callback.message.delete()
"""