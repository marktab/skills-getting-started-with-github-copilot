from urllib.parse import quote


def test_unregister_from_activity_succeeds(client):
    # Arrange
    activity_name = "Chess Club"
    email = "michael@mergington.edu"
    unregister_path = f"/activities/{quote(activity_name)}/signup"

    # Act
    response = client.delete(unregister_path, params={"email": email})

    # Assert
    assert response.status_code == 200
    assert response.json() == {"message": f"Unregistered {email} from {activity_name}"}


def test_unregister_fails_for_unknown_activity(client):
    # Arrange
    activity_name = "Unknown Club"
    email = "student@mergington.edu"
    unregister_path = f"/activities/{quote(activity_name)}/signup"

    # Act
    response = client.delete(unregister_path, params={"email": email})

    # Assert
    assert response.status_code == 404
    assert response.json()["detail"] == "Activity not found"


def test_unregister_fails_for_not_enrolled_student(client):
    # Arrange
    activity_name = "Chess Club"
    email = "not_enrolled@mergington.edu"
    unregister_path = f"/activities/{quote(activity_name)}/signup"

    # Act
    response = client.delete(unregister_path, params={"email": email})

    # Assert
    assert response.status_code == 404
    assert response.json()["detail"] == "Student is not signed up for this activity"
