import aiohttp_jinja2
import aiohttp
from aiohttp import web
from aiohttp_session import get_session
from app.database import Database
import time, json


async def index(request):
    session = await get_session(request)
    session['last_visit'] = time.time()
    session.changed()
    print(session)
    context = {'id':session.get('id')}
    response = aiohttp_jinja2.render_template('index.html',
                                              request,
                                              context)
    response.headers['Content-Language'] = 'ru'
    return response

async def onTelegramAuth(request):
    data = await request.read()
    user = json.loads(data.decode('utf-8'))
    session = await get_session(request)
    if (session.get('id') is None):
        db = Database()
        session['id'] = user['id']
        if db.get_user(user) is None:
            db.add_user(user)
        db.close()

    id = str(session.get('id'))
    return web.Response(text=id)


from config import TOKEN
msg = 'Сходка в селе митькино, 12:00, Будем пить пиво!)'

async def notify(request):
    db = Database()
    users = db.get_users()
    for id in map(lambda x: x[0], users):
        url = "https://api.telegram.org/bot{}/sendMessage".format(TOKEN)
        params = {'chat_id':id, 'text':msg}
        async with aiohttp.ClientSession() as session:
            async with session.get(url, params=params) as resp:
                pass

    db.close()
    return web.Response(text='done')

