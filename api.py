async def create_todo(db, todo):
    await db.create("todo", todo)


# @app.put('/edit/<id>')
# def update_todo_by_id(id):
#     input_json = request.get_json()
#     asyncio.run(update_todo(id, input_json))
#     return "success"


# async def update_todo(id, updated_todo):
#     db = connect_db()
#     await db.update("todo:{id}", updated_todo)
