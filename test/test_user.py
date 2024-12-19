import pytest
from src import create_app
from src.database import db
from src.infrastructure.models import User

@pytest.fixture
def app():
    app = create_app("testing")
    
    with app.app_context():
        db.create_all()
        yield app
        db.drop_all()

@pytest.fixture
def client(app):
    return app.test_client()

def test_create_user(client):
    response = client.post('/user', json={
        'username': 'testuser',
        'email': 'testuser@example.com',
        'password': 'testpassword'
    })
    
    assert response.status_code == 201
    assert response.json['username'] == 'testuser'

def test_get_user(client):
    user = User(username="testuser", email="testuser@example.com")
    db.session.add(user)
    db.session.commit()
    
    response = client.get(f'/user/{user.id}')
    
    assert response.status_code == 200
    assert response.json['username'] == 'testuser'

def test_user_not_found(client):
    response = client.get('/user/9999')
    assert response.status_code == 404
