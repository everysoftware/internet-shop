from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.engine import async_session_factory
from .repositories import UserRepo


class Database:
    session: AsyncSession
    user: UserRepo

    def __init__(
            self,
            session: AsyncSession,
            user: UserRepo | None = None,

    ):
        self.session = session
        self.user = user or UserRepo(session=session)


async def get_database(
        session: AsyncSession = Depends(async_session_factory),
) -> Database:
    return Database(session=session)
