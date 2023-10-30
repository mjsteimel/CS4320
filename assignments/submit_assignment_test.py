import pytest
from System import System
import json


user = "akend3"
password = "123454321"
course = "databases"
assignment_name = "assignment1"
submission = "lorem ipsum"
submission_date = "1/31/20"

def test_submit_assignment():
    system = System()
    system.login(user, password)
    system.usr.submit_assignment(course, assignment_name, submission, submission_date)
    assert system.users[user]['courses'][course][assignment_name]['submission'] == submission
    assert system.users[user]['courses'][course][assignment_name]['submission_date'] == submission_date