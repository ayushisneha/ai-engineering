import asyncio
import time

from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import DeclarativeBase, mapped_column, Mapped
from sqlalchemy import String, Integer, select

engine = create_async_engine(
    "sqlite+aiosqlite:///dashboard.db",
      echo=True,
)

class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(50))
    balance: Mapped[int] = mapped_column(Integer)

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
            User(name="David", balance=2500),
            User(name="Eve", balance=3000),
            User(name="Frank", balance=3500),
            User(name="Grace", balance=4000),
            User(name="Heidi", balance=4500),
            User(name="Ivan", balance=5000),
            User(name="Judy", balance=5500),
        ]
        session.add_all(users)
        await session.commit()
        print("Users inserted")

asyncio.run(init_db())
asyncio.run(insert_users())