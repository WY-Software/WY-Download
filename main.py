import asyncio
import os

from aiogram import Bot, Dispatcher, F
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message, FSInputFile
from aiogram.client.default import DefaultBotProperties

from download import download

bot = Bot(token='', default=DefaultBotProperties(parse_mode=ParseMode.HTML))
dp = Dispatcher()

@dp.message(CommandStart())
async def start(message: Message):
    await message.answer(f'Привет, {message.from_user.full_name}\n'
                         f'Пришли мне ссылку на видео, а я скачаю его и пришлю сюда')


@dp.message(F.text.startswith('https'))
async def on_link(message: Message):
    await download(message.from_user.id, message.text)
    video = FSInputFile(f'{message.from_user.id}.mp4')
    await message.answer_video(video)
    os.remove(f'{message.from_user.id}.mp4')


async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
