import pytest
from Staff import Staff
from System import System


assignment_name = "compute_a_cloud"
due_date = "3/31/20"
course = "cloud_computing"

#Tests to make sure a professor can't create an assignment in a class they don't teach
def test_wrong_professor_create():
    system = System()
    system.login("goggins", "augurrox")
    system.usr.create_assignment(assignment_name, due_date, course)
    assert assignment_name not in system.courses[course]['assignments'].keys()