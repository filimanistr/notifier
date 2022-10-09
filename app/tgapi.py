from dataclasses import dataclass
from typing import Optional
import aiohttp
import config

@dataclass
class TelegramUser:
    """Class that contains an info about telegram user"""
    id: int
    first_name: Optional[str] = None
    last_name: Optional[str] = None

async def send_messages(ids, msg):
    """Рассылает сообщения всем id из листа ids"""
    for id in ids:
        params = {'chat_id':id, 'text':msg}
        async with aiohttp.ClientSession() as session:
            async with session.get(config.SEND_MSG_URL, params=params) as resp:
                print("I've sent message to user: ", id)
