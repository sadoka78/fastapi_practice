import pytest

@pytest.mark.asyncio
async def test_notes_crud(client):
    res = await client.post("/login", json={"username": "testuser", "password": "ffff"})
    token = res.json()["access_token"]
    headers = {"Authorization": f"Bearer {token}"}

    res = await client.post("/notes/", headers=headers, json={"text": "First note!"})
    assert res.status_code == 200
    note_id = res.json()["id"]

    res = await client.get("/notes/", headers=headers)
    assert res.status_code == 200
    assert any(n["text"] == "First note!" for n in res.json())

    res = await client.delete(f"/notes/{note_id}", headers=headers)
    assert res.status_code == 200

    res = await client.delete(f"/notes/{note_id}", headers=headers)
    assert res.status_code == 404
