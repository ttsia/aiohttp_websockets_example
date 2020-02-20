import asyncio
import logging

from aiohttp import web
from aiohttp_swagger import setup_swagger

from api.routes import routes
from settings import CONFIG
from db import init_db


async def init_app():
    app = web.Application()
    app["config"] = CONFIG
    app.add_routes(routes)
    setup_swagger(app)

    await init_db(app)

    return app


def main():
    logging.basicConfig(level=logging.DEBUG)

    app = init_app()

    web.run_app(app)


if __name__ == "__main__":
    main()
