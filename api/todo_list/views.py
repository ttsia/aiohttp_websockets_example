from aiohttp import web
from .models import get_todos

class ToDoListView(web.View):
    """
    ---
    tags:
    - /ToDoList
    """

    async def get(self):
        async with self.request.app['db_pool'].acquire() as conn:
            todos = await get_todos(conn)
        return web.json_response({"data": todos})

    async def post(self):
        raise NotImplementedError
