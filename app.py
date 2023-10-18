from flask import Flask

app = Flask(__name__)


@app.route('/')
def get_all_todo():
    return '<h1>Hello, World!</h1>'


@app.route("/<id>")
def get_todo(id):
    pass


@app.post('/add')
def add_todo():
    pass


@app.put('/edit/<id>')
def edit_todo(id):
    pass


@app.delete('/<id>')
def delete_todo(id):
    pass
