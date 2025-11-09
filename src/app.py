from flask import Flask, jsonify, request, render_template_string
import storage

app = Flask(__name__)

# Template atualizado com filtro de status
LIST_TEMPLATE = '''
<!doctype html>
<title>Task Manager — TechFlow</title>
<h1>Tasks</h1>

<!-- MUDANÇA DE ESCOPO: Filtro por status -->
<div style="margin-bottom: 20px; padding: 10px; background: #f0f0f0;">
  <strong>Filter by status:</strong>
  <a href="/">All</a> |
  <a href="/?status=pending">Pending</a> |
  <a href="/?status=done">Done</a>
</div>

<ul>
{% for t in tasks %}
  <li>
    [{{'X' if t.done else ' '}}] <strong>{{t.title}}</strong> (priority: {{t.priority}}) -
    <a href="/tasks/{{t.id}}">view</a>
  </li>
{% endfor %}
</ul>

<h2>Create</h2>
<form action="/tasks" method="post">
  <input name="title" placeholder="title" required>
  <input name="description" placeholder="description">
  <select name="priority">
    <option value="low">low</option>
    <option value="normal" selected>normal</option>
    <option value="high">high</option>
  </select>
  <button type="submit">Create</button>
</form>
'''

@app.route('/')
def index():
    # MUDANÇA DE ESCOPO: Aplicar filtro de status na página inicial
    status = request.args.get('status')
    tasks = storage.list_tasks()
    
    if status == 'done':
        tasks = [t for t in tasks if t.get('done') == True]
    elif status == 'pending':
        tasks = [t for t in tasks if t.get('done') == False]
    
    return render_template_string(LIST_TEMPLATE, tasks=tasks)

@app.route('/tasks', methods=['GET'])
def list_tasks():
    priority = request.args.get('priority')
    status = request.args.get('status')  # MUDANÇA DE ESCOPO: Novo parâmetro
    tasks = storage.list_tasks()
    
    # Filtro por prioridade (já existente)
    if priority:
        tasks = [t for t in tasks if t.get('priority') == priority]
    
    # MUDANÇA DE ESCOPO: Filtro por status de conclusão
    if status == 'done':
        tasks = [t for t in tasks if t.get('done') == True]
    elif status == 'pending':
        tasks = [t for t in tasks if t.get('done') == False]
    
    return jsonify(tasks)

@app.route('/tasks', methods=['POST'])
def create_task():
    data = request.form or request.json
    title = data.get('title')
    description = data.get('description', '')
    priority = data.get('priority', 'normal')
    if not title:
        return jsonify({'error': 'title required'}), 400
    task = storage.create_task(title, description, priority)
    return jsonify(task), 201

@app.route('/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    task = storage.get_task(task_id)
    if not task:
        return jsonify({'error': 'not found'}), 404
    return jsonify(task)

@app.route('/tasks/<int:task_id>', methods=['PUT', 'PATCH'])
def update_task(task_id):
    data = request.json or {}
    allowed = {'title','description','done','priority'}
    update = {k: data[k] for k in data.keys() & allowed}
    task = storage.update_task(task_id, **update)
    if not task:
        return jsonify({'error':'not found'}), 404
    return jsonify(task)

@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    ok = storage.delete_task(task_id)
    if not ok:
        return jsonify({'error':'not found'}), 404
    return jsonify({'deleted': True})

if __name__ == '__main__':
    app.run(debug=True)