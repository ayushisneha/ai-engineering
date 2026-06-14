import asyncio

from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import DeclarativeBase, mapped_column, Mapped
from sqlalchemy import String, Integer, select

# SQLite async engine - no DB setup needed, will create test.db file in current directory
engine = create_async_engine(
    "sqlite+aiosqlite:///test.db",
      echo=True,
)

# Base class
class Base(DeclarativeBase):
    pass

# Table Model defined as a class inheriting from Base
class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(50))
    balance: Mapped[int] = mapped_column(Integer)

# Function to initialize the database and create tables
async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    print("Database initialized")

async def insert_users():
    async with AsyncSession(engine) as session:
        users = [
            User(name="Alice", balance=1000),
            User(name="Bob", balance=1500),
            User(name="Charlie", balance=2000),
        ]
        session.add_all(users)
        await session.commit()
        print("Users inserted")

asyncio.run(insert_users())