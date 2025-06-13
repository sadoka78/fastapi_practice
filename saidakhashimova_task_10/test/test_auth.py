import pytest
@pytest.mark.asyncio
async def test_register_and_login(client):
    res = await client.post("/register", json={"username":"testuser", "password":"ffff"})
    assert res.status_code == 200
    res = await client.post("/register", json={"username": "testuser", "password": "ffff"})
    assert res.status_code == 400
    res = await client.post("/login", json={"username": "testuser", "password": "ffff"})
    assert res.status_code == 200
    assert "access_token" in res.json()
    res = await client.post("/login",json={"username": "testuser", "password": "wwrong"})
    assert res.status_code == 401


@pytest.mark.asyncio
async def test_users_me(client):
    res = await client.post("/login", json={"username": "testuser", "password": "ffff"})
    token = res.json()["access_token"]
    headers = {"Authorization": f"Bearer {token}"}
    res = await client.get("/users/me", headers=headers)
    assert res.status_code == 200
    res = await client.get("/users/me")
    assert res.status_code == 401