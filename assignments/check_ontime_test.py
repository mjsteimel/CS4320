import pytest
from System import System


def test_check_ontime():
    system = System()
    system.login("akend3", "123454321")
    assert system.usr.check_ontime("1/31/20", "2/2/20") == True
    assert system.usr.check_ontime("2/5/20", "2/2/20") == False