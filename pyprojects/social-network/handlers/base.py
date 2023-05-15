from datetime import datetime
from aiohttp import web
from aiohttp_session import get_session


class Index(web.View):

    @aiohttp_jinja2.template('index.html')
    async def get(self):
        conf = self.app['config']
        return dict(conf=conf)


class Login(web.View):

    @aiohttp_jinja2.template('login.html')
    async def get(self):
        session = await get_session(self)
        session['last visit'] = str(datetime.utcnow())
        last_visit = session['last visit']
        text = 'Last visited: {}'.format(last_visit)
        return dict(text="Login Aiohttp!, {}".format(text))

    async def post(self):
        return web.Response(text="login aiohttp")


class Signup(web.View):

    async def get(self):
        return web.Response(text="signup Aiohttp!")
