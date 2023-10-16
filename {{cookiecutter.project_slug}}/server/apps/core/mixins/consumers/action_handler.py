from typing import Any, Awaitable, Final

from rest_framework.exceptions import ValidationError


class ActionHandlerMixin:
    """
    Class to handle arguments that is passed through receive_json function.
    If passed arguments doesn't contain required body argument
    it will raise BODY_IS_REQUIRED ValidationError.
    If passed action argument is not provided
    it will raise ACTION_INVALID_OR_NOT_PROVIDED ValidationError.
    """

    class Errors:
        ACTION_INVALID_OR_NOT_PROVIDED: Final[str] = "Action is not provided"
        BODY_IS_REQUIRED: Final[str] = "Body argument is required"

    async def handle_action(self, content: dict) -> None:
        action = await self._get_action_from_content(content)
        content_body = await self._get_content_body_for_action(action, content)
        await action(self, **content_body)

    async def _get_action_from_content(self, content: dict) -> Awaitable:
        try:
            return self.ACTION_MAP[content["type"]]
        except KeyError:
            raise ValidationError(self.Errors.ACTION_INVALID_OR_NOT_PROVIDED)

    async def _get_content_body_for_action(
        self, action: Awaitable, content: dict
    ) -> dict:
        body: dict[str, Any] = {}

        try:
            body.update(
                {
                    param: content[param]
                    for param in await self._get_required_params(action)
                }
            )
        except KeyError:
            raise ValidationError(self.Errors.BODY_IS_REQUIRED)
        else:
            body.update(
                {
                    param: content.get(param, None)
                    for param in await self._get_optional_params(action)
                }
            )

        return body

    @staticmethod
    async def _get_required_params(method: Awaitable) -> set[str]:
        annotations: dict[str, Any] = method.__annotations__
        params = {
            key
            for key in annotations.keys()
            if "Optional" not in str(annotations[key])
        }
        params.discard("return")
        return params

    @staticmethod
    async def _get_optional_params(method: Awaitable) -> set[str]:
        annotations: dict[str, Any] = method.__annotations__
        params = {
            key
            for key in annotations.keys()
            if "Optional" in str(annotations[key])
        }
        params.discard("return")
        return params
