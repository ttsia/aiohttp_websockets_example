from datetime import datetime as dt

from sqlalchemy import MetaData, Table, Column, Integer, String, DateTime

metadata = MetaData()

todos = Table(
    "todos",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("text", String(140)),
    Column("timestamp", DateTime, index=True, default=dt.utcnow),
)


async def get_todos(conn):
    records = await conn.fetch(todos.select().order_by(todos.c.id))
    return records


async def create_todo(conn, text):
    stmt = todos.insert().values(text=text)
    await conn.execute(stmt)
