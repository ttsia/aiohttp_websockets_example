import asyncpgsa


async def init_db(app):
    dsn = construct_db_url(app["config"]["DB"])
    pool = await asyncpgsa.create_pool(dsn=dsn)
    app["db_pool"] = pool


def construct_db_url(config):
    DSN = "postgresql://{user}:{password}@{host}:{port}/{database}"
    return DSN.format(
        user=config["username"],
        password=config["password"],
        database=config["database"],
        host=config["host"],
        port=config["port"],
    )
