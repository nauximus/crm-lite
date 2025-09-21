def test_dashboard(client):
    response = client.get("/")
    assert response.status_code == 200
    assert b"CRM" in response.data

def test_add_customer(client):
    response = client.post("/customers/add", data={
        "name": "Alice",
        "email": "alice@example.com",
        "phone": "12345"
    }, follow_redirects = True)

    assert response.status_code == 200
    assert b"Alice" in response.data