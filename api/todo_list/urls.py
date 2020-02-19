from .views import ToDoListView
from aiohttp import web


TODO_URLS = (
    web.get('/todo_list', ToDoListView),
    web.post('/todo_list', ToDoListView)
)
