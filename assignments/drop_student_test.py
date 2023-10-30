import pytest
from System import System
import json

with open('Data/users.json') as f:
    user_data = json.load(f)

name = "akend3"
course = "databases"

def test_drop_student():
    system = System()
    system.login("goggins", "augurrox")
    system.usr.drop_student(name, course)
    assert course not in system.users[name]['courses'].keys()