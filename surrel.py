# %%
"""Example of how to use the SurrealDB client in a notebook"""

from surrealdb import Surreal
import asyncio


async def connect_db():
    async with Surreal("http://127.0.0.1:8000") as db:
        await db.connect()
        # await db.signin({"user": "root", "pass": "root"})
        await db.use("test", "test")
        print(db)

asyncio.run(connect_db())

# # %%
# await db.create(
#     "person",
#     {
#         "user": "me",
#         "pass": "safe",
#         "marketing": True,
#         "tags": ["python", "documentation"],
#     },
# )

# # %%
# await db.select("person")

# # %%
# await db.update("person", {
#     "user":"you",
#     "pass":"very_safe",
#     "marketing": False,
#     "tags": ["Awesome"]
# })

# # %%
# await db.delete("person")
