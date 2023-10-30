import pytest
from Staff import Staff
from System import System
import json

assignment_name = "fight_the_professor"
due_date = "3/31/20"
course = "software_engineering"

def test_create_assignment():
    system = System()
    system.login("goggins", "augurrox")
    system.usr.create_assignment(assignment_name, due_date, course)
    assert due_date == system.courses[course]['assignments'][assignment_name]['due_date']