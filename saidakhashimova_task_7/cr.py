import asyncio
from models import Base
from database import engine  # у тебя он называется просто `engine`

async def create_all():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
        print("✅ Таблицы успешно созданы")

if __name__ == "__main__":
    asyncio.run(create_all())
