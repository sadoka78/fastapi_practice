import pytest_asyncio
from httpx import AsyncClient
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker

from database import get_db
from models import Base
from main import app

DATABASE_URL = "sqlite+aiosqlite:///./test.db"

engine_test = create_async_engine(DATABASE_URL, echo=True)
TestingSessionLocal = sessionmaker(bind=engine_test, class_=AsyncSession, expire_on_commit=False)

async def override_get_db():
    async with TestingSessionLocal() as session:
        yield session

app.dependency_overrides[get_db] = override_get_db

@pytest_asyncio.fixture(scope="session", autouse=True)
async def setup_db():
    async with engine_test.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)

import pytest_asyncio
from httpx import AsyncClient
from httpx import ASGITransport
from main import app

@pytest_asyncio.fixture
async def client():
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as c:
        yield c
