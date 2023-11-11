import aiohttp_jinja2

from datetime import datetime

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

        db = self.app['db']
        user = await User.get_user(uid=1)
        document = await db.test.find_one()
        return dict(text="Login Aiohttp!, Last Visited: {}".format(last_visit))

    async def post(self):
        data = await self.post()
        login = data['login']
        password = data['password']

        session = await get_session(self)
        session['user'] = {"login": login}

        location = self.app.router['index'].url_for()
        return web.HTTPFound(location=location)


class Signup(web.View):

    @aiohttp_jinja2.template('signup.html')
    async def get(self):
        session = await get_session(self)
        session['last visit'] = str(datetime.utcnow())
        last_visit = session['last visit']

        db = self.app['db']
        user = await User.get_user(uid=1)
        document = await db.test.find_one()
        return dict(text="Login Aiohttp!, Last Visited: {}".format(last_visit))

    async def post(self):
        data = await self.post()
        login = data['login']
        password = data['password']

        session = await get_session(self)
        session['user'] = {"login": login}

        location = self.app.router['index'].url_for()
        return web.HTTPFound(location=location)
