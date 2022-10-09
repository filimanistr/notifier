import aiohttp_jinja2
import aiohttp
from aiohttp import web
from aiohttp_session import get_session
import time, json

from app.tgapi import TelegramUser, send_messages
from app.database import Database
import config


async def index(request):
    session = await get_session(request)
    session['last_visit'] = time.time()

    with Database() as db:
        data = db.get_all('id', 'first_name', 'last_name')

    users = [TelegramUser(*user) for user in data]
    context = {'id':session.get('id'), 'users':users, 'YAPI':config.YANDEX_API_KEY}
    response = aiohttp_jinja2.render_template('index.html', request, context)
    response.headers['Content-Language'] = 'ru'
    return response

async def onTelegramAuth(request):
    """Добавление зарегестрированного пользователя в бд"""
    data = await request.read()
    user = json.loads(data.decode('utf-8'))
    session = await get_session(request)
    if (session.get('id') is None):
        session['id'] = user['id']
        with Database() as db:
            if db.get_user(user) is None:
                db.add_user(user)

    id = str(session.get('id'))
    return web.Response(text=id)

async def notify(request):
    """Рассылка сообщений всем юзерам из базы"""
    with Database() as db:
        data = db.get_all('id')

    users = [TelegramUser(*user).id for user in data]
    await send_messages(users, config.MESSAGE)
    return web.Response()

async def notify_certain_users(request):
    """Рассылка сообщений выбранным юзерам"""
    data = await request.read()
    users = json.loads(data.decode('utf-8'))
    msg = config.CERTAIN_MESSAGE.format(users['reason'],
                                        users['time'],
                                        users['address'])
    await send_messages(users['users'], msg)
    return web.Response()
