import asyncio
from logging.config import fileConfig
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy import pool
from alembic import context
import os
import sys

# Подключаем пути
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from models import Base

# Alembic конфиг
config = context.config

# Подключаем логгирование
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# Метаданные моделей
target_metadata = Base.metadata

# URL из переменной окружения или напрямую
def get_url():
    return os.getenv("DATABASE_URL", "postgresql+asyncpg://postgres:saida0512@localhost/notes")

def run_migrations_offline():
    """Оффлайн миграции"""
    url = get_url()
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
        compare_type=True,
    )

    with context.begin_transaction():
        context.run_migrations()

def do_run_migrations(connection):
    context.configure(
        connection=connection,
        target_metadata=target_metadata,
        compare_type=True,
    )

    with context.begin_transaction():
        context.run_migrations()

async def run_migrations_online():
    """Онлайн миграции с async движком"""
    connectable = create_async_engine(
        get_url(),
        poolclass=pool.NullPool,
    )

    async with connectable.connect() as connection:
        await connection.run_sync(do_run_migrations)

    await connectable.dispose()

if context.is_offline_mode():
    run_migrations_offline()
else:
    asyncio.run(run_migrations_online())
