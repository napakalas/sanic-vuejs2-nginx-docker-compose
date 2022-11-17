import os

from sanic import Sanic
from sanic.response import json

from app.utils.helper import hello_world

SANIC_PREFIX = "SANIC_"

app = Sanic(name='NGINX_SANIC_VUE')


@app.route("/hello-world")
async def moon(request):
    return json(hello_world())


@app.route("/teaching")
async def teaching(request):
    return json({'a': 100})


# while in docker files from static will be served by ngnix
app.static('/static', './static')
if __name__ == "__main__":
    for k, v in os.environ.items():
        if k.startswith(SANIC_PREFIX):
            _, config_key = k.split(SANIC_PREFIX, 1)
            app.config[config_key] = v
    app.run(
        host="0.0.0.0",
        port=8000,
        workers=1,
        auto_reload=True,
        access_log=False,
    )
