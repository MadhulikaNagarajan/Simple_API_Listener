
import pytest
from flask import Flask, render_template, request
import json
import database
from app import app

@pytest.fixture
def client():
    return app.test_client()

def test_home_route(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b'<h1> Welcome to simple API listener</h1>' in response.data

def test_home_page(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b'<p> Please login using you r credentials</p>' not in response.data

def test_save_user_route(client):
    response = client.post('/save', data={'Username': 'Admin', 'Password': 'Admin@123'})
    assert response.status_code == 200
    assert response.data == b'User data saved successfully'

    users = database.get_user_data()
    assert any(user[1] == 'Admin' and user[2] == 'Admin@123' for user in users)

def test_save_user_page(client):
    response = client.post('/save', data={'Username': '', 'Password': '123'})
    assert response.status_code == 200
    assert response.data == b'Missing input'

def test_save_user(client):
    response = client.post('/save',data={'Username': 'Madhu', 'Password': ''})
    assert response.status_code == 200
    assert response.data == b'Missing input'

def test_get_user_route(client):
    response = client.post('/get_user')
    assert response.status_code == 200
    expected_result = database.get_user_data()
    response_data = json.loads(response.data)

    # Convert the expected result to a set of tuples
    expected_result_set = set(map(tuple,expected_result))

    # Convert the response data to a set of tuples
    response_data_set = set(map(tuple, response_data))

    # Check if the parsed response data contains the same elements as the expected result
    assert expected_result_set == response_data_set

def test_delete_user_route(client):
    response = client.post('/delete', data={'Username': 'Madhul', 'Password': 'Admin@123'})
    assert response.status_code == 200
    assert b'user not found' in response.data

def test_delete_user_page(client):
    response = client.post('/delete', data={'Username': 'Admin', 'Password': 'Admin@123'})
    assert response.status_code == 200
    assert b"User data deleted successfully" in response.data

def test_update_user_route(client):
    response = client.post('/update', data={'Username': 'Madhulika', 'Password': 'Madhu@123'})
    assert response.status_code == 200
    assert b"User data updated successfully" in response.data

def test_update_user_page(client):
    response = client.post('/update', data={'Username': 'Madhu', 'Password': 'Madhu123'})
    assert response.status_code == 200
    assert b"User data updated successfully" not in response.data

def test_authorise_user_route(client):
    response = client.post('/authorise', data={'Username': 'Madhu', 'Password': 'Madhu123'})
    assert response.status_code == 200
    assert b'Invalid input' in response.data

def test_not_authorise_user(client):
    response = client.post('/authorise', data={'Username': 'Madhulika', 'Password': 'Madhu@123'})
    assert response.status_code == 200
    assert b'you are authorised' in response.data

def test_authorise_user(client):
    response = client.post('/authorise', data={'Username': 'Madhulika', 'Password': 'Madhu@1234'})
    assert response.status_code == 200
    assert b' Invalid credenatials' in response.data