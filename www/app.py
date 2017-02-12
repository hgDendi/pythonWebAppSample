import logging; logging.basicConfig(level=logging.INFO)

import asyncio, os, json, time
from datetime import datetime
from aiohttp import web

def index(request):
	return web.Response(body=b'<h1>Hello World</h1>')

@asyncio.coroutine
def init(loop,ip,port):
	app = web.Application(loop = loop)
	app.router.add_route('GET','/',index)
	srv = yield from loop.create_server(app.make_handler(),ip,port)
	logging.info('server started at http://%s:%d' % (ip,port))
	return srv

loop = asyncio.get_event_loop()
ip = '127.0.0.1'
port = 9000
loop.run_until_complete(init(loop,ip,port))
loop.run_forever()