"""
Testes automatizados para validação de entradas
e funcionalidades do TechFlow Task Manager
"""
import pytest
from src.app import app

@pytest.fixture
def client():
    """Fixture para criar cliente de teste"""
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

# ========================================
# TESTES DE VALIDAÇÃO DE ENTRADA
# ========================================

def test_create_task_with_valid_data(client):
    """Teste: Criar tarefa com dados válidos"""
    response = client.post('/tasks', json={
        'title': 'Tarefa Teste',
        'description': 'Descrição válida',
        'priority': 'high'
    })
    assert response.status_code == 201
    data = response.get_json()
    assert data['title'] == 'Tarefa Teste'
    print("✅ Validação: Dados válidos aceitos")

def test_create_task_without_title(client):
    """Teste: VALIDAÇÃO - Rejeitar tarefa sem título"""
    response = client.post('/tasks', json={
        'description': 'Sem título'
    })
    assert response.status_code == 400
    data = response.get_json()
    assert 'error' in data
    assert 'title required' in data['error']
    print("✅ Validação: Título obrigatório funcionando")

def test_create_task_with_empty_title(client):
    """Teste: VALIDAÇÃO - Rejeitar título vazio"""
    response = client.post('/tasks', json={
        'title': '',
        'description': 'Título vazio'
    })
    assert response.status_code == 400
    print("✅ Validação: Título vazio rejeitado")

def test_priority_validation(client):
    """Teste: VALIDAÇÃO - Aceitar prioridades válidas"""
    valid_priorities = ['low', 'normal', 'high']
    
    for priority in valid_priorities:
        response = client.post('/tasks', json={
            'title': f'Task {priority}',
            'priority': priority
        })
        assert response.status_code == 201
        data = response.get_json()
        assert data['priority'] == priority
    
    print("✅ Validação: Prioridades válidas aceitas")

def test_default_priority(client):
    """Teste: VALIDAÇÃO - Prioridade padrão é 'normal'"""
    response = client.post('/tasks', json={
        'title': 'Tarefa sem prioridade'
    })
    data = response.get_json()
    assert data['priority'] == 'normal'
    print("✅ Validação: Prioridade padrão aplicada")

def test_done_default_false(client):
    """Teste: VALIDAÇÃO - Campo 'done' inicia como False"""
    response = client.post('/tasks', json={
        'title': 'Nova tarefa'
    })
    data = response.get_json()
    assert data['done'] == False
    print("✅ Validação: Status inicial correto")

# ========================================
# TESTES DE FUNCIONALIDADE
# ========================================

def test_list_tasks_returns_json(client):
    """Teste: Listar tarefas retorna JSON válido"""
    response = client.get('/tasks')
    assert response.status_code == 200
    data = response.get_json()
    assert isinstance(data, list)
    print("✅ Funcionalidade: Listagem funcionando")

def test_get_nonexistent_task(client):
    """Teste: VALIDAÇÃO - Buscar tarefa inexistente retorna 404"""
    response = client.get('/tasks/99999')
    assert response.status_code == 404
    data = response.get_json()
    assert 'error' in data
    print("✅ Validação: Erro 404 para recurso inexistente")

def test_update_task(client):
    """Teste: Atualizar tarefa existente"""
    # Criar tarefa
    create_response = client.post('/tasks', json={
        'title': 'Tarefa Original'
    })
    task_id = create_response.get_json()['id']
    
    # Atualizar
    update_response = client.patch(f'/tasks/{task_id}', json={
        'title': 'Tarefa Atualizada',
        'done': True
    })
    assert update_response.status_code == 200
    
    data = update_response.get_json()
    assert data['title'] == 'Tarefa Atualizada'
    assert data['done'] == True
    print("✅ Funcionalidade: Atualização funcionando")

def test_filter_by_status(client):
    """Teste: MUDANÇA DE ESCOPO - Filtro por status"""
    # Criar tarefa pendente
    client.post('/tasks', json={'title': 'Pendente', 'done': False})
    
    # Criar tarefa concluída
    response = client.post('/tasks', json={'title': 'Concluída'})
    task_id = response.get_json()['id']
    client.patch(f'/tasks/{task_id}', json={'done': True})
    
    # Testar filtro pending
    response = client.get('/tasks?status=pending')
    data = response.get_json()
    for task in data:
        assert task['done'] == False
    
    # Testar filtro done
    response = client.get('/tasks?status=done')
    data = response.get_json()
    for task in data:
        assert task['done'] == True
    
    print("✅ Mudança de Escopo: Filtro por status funcionando")

# ========================================
# TESTE DE INTEGRAÇÃO
# ========================================

def test_full_crud_workflow(client):
    """Teste de integração: Fluxo completo CRUD"""
    # CREATE
    create_response = client.post('/tasks', json={
        'title': 'Teste Integração',
        'priority': 'high'
    })
    assert create_response.status_code == 201
    task_id = create_response.get_json()['id']
    
    # READ
    read_response = client.get(f'/tasks/{task_id}')
    assert read_response.status_code == 200
    
    # UPDATE
    update_response = client.patch(f'/tasks/{task_id}', json={
        'done': True
    })
    assert update_response.status_code == 200
    
    # DELETE
    delete_response = client.delete(f'/tasks/{task_id}')
    assert delete_response.status_code == 200
    
    # Verificar que foi deletada
    verify_response = client.get(f'/tasks/{task_id}')
    assert verify_response.status_code == 404
    
    print("✅ Integração: Fluxo CRUD completo funcionando")