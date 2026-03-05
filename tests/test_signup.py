from urllib.parse import quote


def test_signup_for_activity_succeeds(client):
    # Arrange
    activity_name = "Chess Club"
    email = "new_student@mergington.edu"
    signup_path = f"/activities/{quote(activity_name)}/signup"

    # Act
    response = client.post(signup_path, params={"email": email})

    # Assert
    assert response.status_code == 200
    assert response.json() == {"message": f"Signed up {email} for {activity_name}"}


def test_signup_fails_for_unknown_activity(client):
    # Arrange
    activity_name = "Unknown Club"
    email = "new_student@mergington.edu"
    signup_path = f"/activities/{quote(activity_name)}/signup"

    # Act
    response = client.post(signup_path, params={"email": email})

    # Assert
    assert response.status_code == 404
    assert response.json()["detail"] == "Activity not found"


def test_signup_fails_for_duplicate_registration(client):
    # Arrange
    activity_name = "Chess Club"
    email = "michael@mergington.edu"
    signup_path = f"/activities/{quote(activity_name)}/signup"

    # Act
    response = client.post(signup_path, params={"email": email})

    # Assert
    assert response.status_code == 400
    assert response.json()["detail"] == "Student already signed up"
