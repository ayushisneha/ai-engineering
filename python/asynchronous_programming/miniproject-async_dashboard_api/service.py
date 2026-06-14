import asyncio
from sqlalchemy.ext.asyncio import AsyncSession
from repository import get_user_by_id
from db import engine

async def get_user_summary(user_id: int, sem: asyncio.Semaphore):
    async with sem: # acquire the semaphore before accessing the DB
        async with AsyncSession(engine) as session:
            user = await get_user_by_id(session, user_id)
            
            if not user:
                return ValueError(f"User with id {user_id} not found")
            
            await asyncio.sleep(1) # Simulate some processing time

            return {
                "id": user.id,
                "name": user.name,
                "balance": user.balance,
                "status": "rich" if user.balance > 4500 else "normal"
            }