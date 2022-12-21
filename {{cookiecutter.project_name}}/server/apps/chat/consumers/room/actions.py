from .constants import Events
from .queries import UserQueries
from .services import UserService


class RoomActionsMixin:

    async def user_list(self) -> None:
        users = await UserQueries.get_users_list(self.event_id)
        body = {"users": await UserService.get_users_list(users)}
        await self.response_to_user(Events.EVENT_USERS_RETRIEVE, body)

    async def send_message(self, body: dict) -> None:
        body = {"message": body["message"]}
        await self.response_to_group(Events.MESSAGE_NEW, body)
