import pytest
from System import System


user = "hdjsr7"
password = "pass1234"
course = "databases"
expected_assignments = [["assignment1", "1/6/20"], ["assignment2", "2/6/20"]]

def test_view_assignments():
    system = System()
    system.login(user, password)
    assignments = system.usr.view_assignments(course)
    print(assignments)
    assert expected_assignments == assignments
    