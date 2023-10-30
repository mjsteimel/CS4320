import pytest
from System import System
import json
import Student
import TA
import Professor


with open('Data/users.json') as f:
    user_data = json.load(f)

username = "goggins"

def test_login():
    system = System()
    user_info = user_data.get(username)
    
    if user_info is None:
        pytest.skip(f"User '{username}' not found in JSON data")
    
    password = user_info["password"]
    expected_role = user_info["role"]
    
    system.login(username, password)
    
    if expected_role == 'professor':
        assert isinstance(system.usr, Professor.Professor)
    elif expected_role == 'ta':
        assert isinstance(system.usr, TA.TA)
    elif expected_role == 'student':
        assert isinstance(system.usr, Student.Student)
    

    assert system.usr.name == username
    assert system.usr.courses == user_info["courses"]