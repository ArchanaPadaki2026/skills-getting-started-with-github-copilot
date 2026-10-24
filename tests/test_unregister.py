from fastapi.testclient import TestClient

from src.app import app, activities

client = TestClient(app)


def test_unregister_participant_removes_email_from_activity():
    activity_name = "Chess Club"
    email = "test.student@mergington.edu"

    activities[activity_name]["participants"].append(email)

    response = client.delete(
        f"/activities/{activity_name}/unregister",
        params={"email": email},
    )

    assert response.status_code == 200
    assert email not in activities[activity_name]["participants"]
    assert response.json()["message"] == f"Unregistered {email} from {activity_name}"


def test_unregister_missing_email_returns_404():
    response = client.delete(
        "/activities/Chess Club/unregister",
        params={"email": "missing@mergington.edu"},
    )

    assert response.status_code == 404
