import pytest
from System import System
import json


name = "akend3"
course = "software_engineering"

def test_add_student():
    system = System()
    system.login("goggins", "augurrox")
    system.usr.add_student(name, course)
    assert course in system.users[name]['courses'].keys()