from aiohttp import web


class ToDoListView(web.View):
    """
    ---
    tags:
    - /ToDoList
    """

    async def get(self):
        return web.json_response({"data": "ok"})

    async def post(self):
        raise NotImplementedError
