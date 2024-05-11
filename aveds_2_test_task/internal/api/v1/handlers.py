from aiogram import Router, types, F
from aiogram.filters.command import Command

router = Router()


@router.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer(f"Hello {message.from_user.first_name}!\nSend me any text and I'll tell you it's length.")


@router.message(F.text)
async def handle_message(message: types.Message):
    await message.answer(f"Вы отправили сообщение длиной {len((message.text).replace(' ', ''))} символа(ов).")
