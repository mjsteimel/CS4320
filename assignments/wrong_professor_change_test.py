import pytest
from System import System

user = "akend3"
course = "comp_sci"
assignment = "assignment2"
grade = 100

def test_wrong_professor_change():
    system = System()
    system.login("goggins", "augurrox")
    original_grade = system.users[user]['courses'][course][assignment]['grade']
    system.usr.change_grade(user, course, assignment, grade)
    assert original_grade == system.users[user]['courses'][course][assignment]['grade']
    