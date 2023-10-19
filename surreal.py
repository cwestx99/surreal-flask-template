from surrealdb import Surreal


async def create_todo(todo):
    """Example of how to use the SurrealDB client."""
    async with Surreal("ws://localhost:8000/rpc") as db:
        await db.signin({"user": "root", "pass": "root"})
        await db.use("test", "test")
        await db.create("todo", todo)


async def get_all_todos():
    async with Surreal("ws://localhost:8000/rpc") as db:
        await db.signin({"user": "root", "pass": "root"})
        await db.use("test", "test")
        response = await db.select("todo")
        return response


async def update_todo(id, updated_todo):
    async with Surreal("ws://localhost:8000/rpc") as db:
        await db.signin({"user": "root", "pass": "root"})
        await db.use("test", "test")
        await db.update(id, updated_todo)
