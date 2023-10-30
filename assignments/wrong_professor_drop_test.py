import pytest
from System import System
import json

with open('Data/users.json') as f:
    user_data = json.load(f)

name = "hdjsr7"
course = "cloud_computing"

#Tests to make sure professors can't drop students from classes they don't teach
def test_wrong_professor_drop():
    system = System()
    system.login("goggins", "augurrox")
    system.usr.drop_student(name, course)
    assert course in system.users[name]['courses'].keys()
