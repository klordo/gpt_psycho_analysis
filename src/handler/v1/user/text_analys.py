from aiogram.fsm.context import FSMContext

import fsm
from aiogram import types, F
from handler.v1.router import user_router
from gpt import get_analys


@user_router.message(F.text.casefold() == "/analys")
async def send_welcome(message: types.Message, state: FSMContext):
    await message.reply("Пожалуйста, отправь небольшое эссе на любую тему.")
    await state.set_state(fsm.TextAnalys.wait_text)


@user_router.message(fsm.TextAnalys.wait_text)
async def analyze_text(message: types.Message, state: FSMContext):
    await state.clear()
    result_text = get_analys(message.text)
    max_length = 4096  # Максимальная длина одного сообщения в Telegram

    # Разбиваем текст на части, если он слишком большой
    for i in range(0, len(result_text), max_length):
        part_of_text = result_text[i:i+max_length]
        await message.answer(part_of_text)