from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from db import User

async def get_user_by_id(session: AsyncSession, user_id: int):
    result = await session.execute(select(User).where(User.id == user_id))
    user = result.scalar_one_or_none()
    return user