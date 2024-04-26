from aiogram.filters import Command
from aiogram import Router,types

echo_router= Router()

@echo_router.message()
async def process_text(message: types.Message):
    reversed_text = reverse_text(message.text)
    await message.reply(reversed_text)

def reverse_text(text: str) -> str:
    words = text.split()
    reversed_words = reversed(words)
    reversed_text = " ".join(reversed_words)
    return reversed_text
