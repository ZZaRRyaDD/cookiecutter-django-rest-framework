import re

from channels.db import database_sync_to_async
from channels.middleware import BaseMiddleware
from channels.sessions import CookieMiddleware, SessionMiddleware
from django.contrib.auth.models import AnonymousUser
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.exceptions import (
    AuthenticationFailed,
    InvalidToken,
    TokenError,
)

AUTH_COOKIE_KEY = "authorization"


class JWTCookieAuthMiddleware(BaseMiddleware):
    """
    Class to get user from cookie.
    rest_framework_simplejwt is required.
    """

    @staticmethod
    @database_sync_to_async
    def get_user(token):
        jwt_auth = JWTAuthentication()

        try:
            user = jwt_auth.get_user(jwt_auth.get_validated_token(token))
        except (AuthenticationFailed, InvalidToken, TokenError, KeyError):
            user = AnonymousUser()

        return user

    async def __call__(self, scope: dict, receive, send):
        scope["user"] = AnonymousUser()
        headers: dict[bytes, bytes] = dict(scope.get("headers", {}))

        if b"cookie" in headers:
            cookies = headers[b"cookie"].decode()
            if AUTH_COOKIE_KEY.encode() in headers[b"cookie"]:
                if token_key := re.search(
                    f"{AUTH_COOKIE_KEY}=(.*)(; )?", cookies
                ).group(1):
                    scope["user"] = await self.get_user(token_key)

        return await super().__call__(scope, receive, send)


def _get_token_auth_middleware_stack(inner):
    return CookieMiddleware(SessionMiddleware(JWTCookieAuthMiddleware(inner)))


JWTCookieAuthMiddlewareStack = _get_token_auth_middleware_stack
