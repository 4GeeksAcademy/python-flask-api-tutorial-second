from flask import Flask, jsonify, request


app = Flask(__name__)


@app.route("/")
def hello_world():
    # return por default si es string, devuelve HTML
    # return por default si es dict o list, devuelve json
    return "<h1>Hello, World!</h1>"


@app.route('/todos', methods=['GET'])
def handle_todos():
    response_body = todos
    return response_body


@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.json
    print("Incoming request with the following body", request_body)
    todos.append(request_body)
    response_body = todos
    return response_body


@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    print("This is the position to delete: ",position)
    del todos[position]
    response_body = todos
    return response_body


some_data = { "name": "Bobby", "lastname": "Rixer" }
todos = [
    { "label": "My first task", "done": False },
    { "label": "My second task", "done": False }
]

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)