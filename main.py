import asyncio
import re
from aiogram import Bot, Dispatcher
from aiogram.types import Message
import time

bot = Bot(token='7721522134:AAGvZ1Ui7Zf1efHwP5yDk-PHUAiklMNTivk')
dp = Dispatcher()

current_chat_id = None
last_message_time = None

def contains_kus(text: str) -> bool:
    if text is None:
        return False

    pattern = r'[КкKk][УуYy][СсCc]'
    return re.search(pattern, text, re.IGNORECASE) is not None

@dp.message()
async def handle_message(message: Message):
    global current_chat_id, last_message_time

    if message.chat.type == 'private':
        return
    else:
        current_chat_id = message.chat.id

    if message.text and contains_kus(message.text):
        last_message_time = time.time()
        await message.answer('#сашаненародныйкрутитпроектывкрысу') # Месседж на слово "КУС" в любом контексте

async def send_message():
    global current_chat_id, last_message_time
    while True:
        if last_message_time is not None and time.time() - last_message_time > 3600: # Delay при при пустом чате 1 час
            await asyncio.sleep(3)
            continue

        if current_chat_id:
            try:
                await bot.send_message(current_chat_id, "Cherry KYC: Link (раз в 3 сек)")
            except Exception as e:
                print(f"Error sending message: {e}")

        await asyncio.sleep(3) # Отправлять меседж на сервисы раз в 3 сек

async def main():
    asyncio.create_task(send_message())
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())