from aiohttp import web, WSMsgType

from .models import get_todos, create_todo


class ToDoListView(web.View):
    """
    ---
    tags:
    - /ToDoList
    """

    async def get(self):
        """
        Just return texts from all todos records.
        """
        async with self.request.app["db_pool"].acquire() as conn:
            todos = await get_todos(conn)
        return web.json_response({"data": [todo[1] for todo in todos]})

    async def post(self):
        """
        Add test todo record to db.
        """
        async with self.request.app["db_pool"].acquire() as conn:
            await create_todo(conn, "test")
        return web.json_response({"data": "ok"})


class WebSocket(web.View):
    async def get(self):
        ws = web.WebSocketResponse()
        await ws.prepare(self.request)

        async for msg in ws:
            if msg.type == WSMsgType.text:
                if msg.data == "close":
                    await ws.close()
                else:
                    async with self.request.app["db_pool"].acquire() as conn:
                        await create_todo(conn, msg.data)
                        ws.send_str(msg.data)
            elif msg.type == WSMsgType.error:
                continue

        return ws
