from flask import Flask, request, jsonify, render_template
from src.storage import TaskStorage

app = Flask(__name__)
storage = TaskStorage()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/tasks', methods=['GET'])
def get_tasks():
    tasks = storage.get_all()
    return jsonify([task.__dict__ for task in tasks])

@app.route('/tasks', methods=['POST'])
def create_task():
    data = request.get_json()
    task = storage.create(data['title'], data['description'])
    return jsonify(task.__dict__), 201

@app.route('/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    task = storage.get_by_id(task_id)
    if task:
        return jsonify(task.__dict__)
    return jsonify({'error': 'Task not found'}), 404

@app.route('/tasks/priority/<priority>', methods=['GET'])
def get_tasks_by_priority(priority):
    tasks = storage.get_by_priority(priority)
    return jsonify([task.__dict__ for task in tasks])

if __name__ == '__main__':
    app.run(debug=True)



