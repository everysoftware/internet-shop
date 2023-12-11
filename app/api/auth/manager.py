from typing import AsyncGenerator

from fastapi import Depends, Request
from fastapi_users import BaseUserManager, IntegerIDMixin

from app.core.config import cfg
from app.core.models import User
from app.core.repositories import get_user_db
from app.tasks import send_email
from .email import thank_you


class UserManager(IntegerIDMixin, BaseUserManager[User, int]):
    reset_password_token_secret = cfg.api.secret_auth
    verification_token_secret = cfg.api.secret_auth

    async def on_after_register(self, user: User, request: Request | None = None):
        print(f"User {user.id} has registered.")

        send_email.delay(thank_you(user))


async def get_user_manager(
        user_db=Depends(get_user_db),
) -> AsyncGenerator[UserManager, None]:
    yield UserManager(user_db)
