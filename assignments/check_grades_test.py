import pytest
from System import System


user = "akend3"
password = "123454321"
course = "comp_sci"
expected_grades = [["assignment1", 99], ["assignment2", 66]]

def test_check_grades():
    system = System()
    system.login(user, password)
    grades = system.usr.check_grades(course)
    assert expected_grades == grades
    