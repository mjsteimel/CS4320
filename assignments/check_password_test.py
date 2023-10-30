import pytest
from System import System  # Import the System class

# Define test cases
def test_check_password():
    system = System()
    system.load_data()  # Load data to set up the user information

    # User for testing (you can change this to an existing user from your data)
    test_user = "akend3"

    # Correct password for the user "akend3"
    correct_password = "123454321"

    # Incorrect passwords
    incorrect_password_1 = "bestTA"
    incorrect_password_2 = "pass1234"

    # Check with the correct password
    result = system.check_password(test_user, correct_password)
    assert result is True

    # Check with incorrect passwords
    result = system.check_password(test_user, incorrect_password_1)
    assert result is False

    result = system.check_password(test_user, incorrect_password_2)
    assert result is False

# Additional test cases can be added to cover different users and their passwords
