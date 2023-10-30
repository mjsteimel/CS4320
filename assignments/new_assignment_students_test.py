import pytest
from System import System
import json

user = "akend3"
course = "comp_sci"
assignment_name = "assignment3"
due_date = "2/10/20"

#Tests to see whether newly created assignments are added to the students in that course
def test_new_assignment_students():
    system = System()
    system.login("saab", "boomr345")
    system.usr.create_assignment(assignment_name, due_date, course)
    assert assignment_name in system.users[user]["courses"][course]