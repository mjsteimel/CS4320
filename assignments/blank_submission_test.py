import pytest
from System import System
import json



user = "hdjsr7"
password = "pass1234"
course = "databases"
assignment_name = "assignment1"
submission = ""
submission_date = "1/31/20"

#Tests whether blank submissions are rejected
def test_blank_submission():
    system = System()
    system.login(user, password)
    system.usr.submit_assignment(course, assignment_name, submission, submission_date)
    assert assignment_name not in system.users[user]['courses'][course]
