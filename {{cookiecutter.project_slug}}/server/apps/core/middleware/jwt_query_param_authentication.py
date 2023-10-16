from urllib.parse import parse_qs

from channels.db import database_sync_to_async
from django.contrib.auth.models import AnonymousUser
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.exceptions import (
    AuthenticationFailed,
    InvalidToken,
    TokenError,
)

QUERY_TOKEN_KEY = "token"


class JWTQueryParamAuthMiddleware:
    """
    Class to get user from query param.
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

    def __init__(self, inner):
        self.inner = inner

    async def __call__(self, scope: dict, receive, send):
        qs = scope["query_string"].decode("utf8")
        token = parse_qs(qs).get(QUERY_TOKEN_KEY, [""])[0]

        scope["user"] = await self.get_user(token)

        return await self.inner(scope, receive, send)
