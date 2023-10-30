import pytest
from System import System

user = "akend3"
course = "databases"
assignment = "assignment2"
grade = 100

def test_change_grade():
    system = System()
    system.login("goggins", "augurrox")
    system.usr.change_grade(user, course, assignment, grade)
    print(system.users[user]['courses'][course][assignment]['grade'])
    assert grade == system.users[user]['courses'][course][assignment]['grade']
    