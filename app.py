from flask import Flask, request
from surreal import create_todo, get_all_todos, update_todo
import asyncio


app = Flask(__name__)


@app.route('/')
def home():
    return asyncio.run(get_all_todos())


@app.post('/add')
def add_todo():
    input_json = request.get_json()
    asyncio.run(create_todo(input_json))
    return "success"


@app.put('/edit/<id>')
def update_todo_by_id(id):
    input_json = request.get_json()
    asyncio.run(update_todo(id, input_json))
    return "success"
