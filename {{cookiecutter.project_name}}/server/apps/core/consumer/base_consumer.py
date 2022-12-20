import json
from typing import Optional

from channels.generic.websocket import AsyncJsonWebsocketConsumer
from rest_framework.exceptions import ValidationError

from apps.core.mixins.consumers import ActionHandlerMixin


class BaseConsumer(
    AsyncJsonWebsocketConsumer,
    ActionHandlerMixin,
):

    ACTION_MAP: dict[str, str] = {}

    group_name: Optional[str] = None

    async def receive_json(self, content: dict, **kwargs) -> None:
        try:
            await self.handle_action(content=content)
        except Exception as exception:
            await self.handle_exception(exception)

    async def receive(self, *args, **kwargs) -> None:
        try:
            await super().receive(*args, **kwargs)
        except json.JSONDecodeError as exception:
            await self.handle_exception(exception)

    async def response_to_user(self, event: str, body: dict) -> None:
        await self.channel_layer.send(
            self.channel_name,
            {"type": event, "body": body}
        )

    async def response_to_group(self, event: str, body: dict) -> None:
        if self.group_name:
            await self.channel_layer.group_send(
                self.group_name, {"type": event, "body": body}
            )

    async def send_error(self, message: str) -> None:
        message = self._clean_rest_framework_validation_error(message)
        await super().send_json({"type": "error", "detail": message})

    async def send_event_response(self, event: dict) -> None:
        await self.send_json(await self._compose_response(event))

    @staticmethod
    async def _compose_response(event: dict) -> dict:
        response = {"type": event["type"]}

        if event.get("body"):
            response["body"] = event["body"]

        return response

    @staticmethod
    def _clean_rest_framework_validation_error(message) -> str:
        return (
            message[0]
            if isinstance(message, list) and len(message) == 1
            else message
        )

    async def handle_exception(self, exception) -> None:
        response: Optional[str] = None

        if isinstance(exception, ValidationError):
            response = exception.detail
        elif isinstance(exception, json.JSONDecodeError):
            response = str(exception)

        if response:
            await self.send_error(response)
        else:
            raise exception
