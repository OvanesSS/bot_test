from aiogram import F, Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, CallbackQuery

import app.keyboards as kb


router = Router()


@router.message(CommandStart())
async def cmd_star(message: Message):
    await message.reply(f'Привет!\nТвой ID: {message.from_user.id}.\nИмя: {message.from_user.first_name}',
                        reply_markup=kb.main)


@router.message(Command('help'))
async def get_help(message: Message):
    await message.answer('Напишите "/start"')


@router.message(F.text=='Как дела?')
async def how_are_you(message: Message):
    await message.answer('Отлично! А как твои дела?')


@router.message(F.photo)
async def get_photo(message: Message):
    await message.answer(f'ID фото: {message.photo[-1].file_id}')


@router.message(Command('get_photo'))
async def get_photo(message: Message):
    await message.answer_photo(photo='AgACAgIAAxkBAAIBmmbF2NMUwEvCAAEhT5xKS5Wd-uBmiQACNOMxG24xMEqcc34v___J9QEAAwIAA3kAAzUE',
                               caption='Это картинка))))')


@router.callback_query(F.data == 'catalog')
async def catalog(callback: CallbackQuery):
    await callback.answer('Вы выбрали каталог', show_alert=True)
    await callback.message.edit_text('Привет!', reply_markup=await kb.inline_cars())