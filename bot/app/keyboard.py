from aiogram.types import (ReplyKeyboardMarkup,KeyboardButton,
                           InlineKeyboardMarkup, InlineKeyboardButton)

main_keyboard = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='Каталог')],
                                               [KeyboardButton(text='Корзина')],
                                               [KeyboardButton(text='Контакты'),
                                               KeyboardButton(text='Регистрация')]],
									resize_keyboard=True,
									input_field_placeholder='Выберите пункт меню',
                                    one_time_keyboard=True)
catalog_keyboard =InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='Футболки', callback_data='tshirt'),],
                                                        [InlineKeyboardButton(text='Кроссовки', callback_data='sneakers')],
                                                        [InlineKeyboardButton(text='Кепки', callback_data='cap')]])

get_number = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='Отправить номер', request_contact=True)]],
                                 resize_keyboard=True,
                                 one_time_keyboard=True)