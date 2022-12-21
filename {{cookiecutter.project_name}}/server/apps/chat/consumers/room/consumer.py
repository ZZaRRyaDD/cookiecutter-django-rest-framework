from channels.exceptions import DenyConnection

from apps.core.consumer import BaseConsumer

from .actions import RoomActionsMixin
from .constants import Actions
from .events import RoomEventsMixin
from .validators import ConnectValidation


class ChatConsumer(
    BaseConsumer,
    RoomActionsMixin,
    RoomEventsMixin,
):

    ACTION_MAP = {
        Actions.USER_LIST: RoomActionsMixin.user_list,
        Actions.SEND_MESSAGES: RoomActionsMixin.send_message,
    }

    async def connect(self):
        self.room_id = self.scope["url_route"]["kwargs"]["room_id"]
        self.group_name = f"room_{self.room_id}"
        self.user = self.scope["user"]
        await self.accept()
        if error := await ConnectValidation.validate():
            await self.send_error(error)
            raise DenyConnection()
        await self.channel_layer.group_add(
            self.group_name,
            self.channel_name,
        )
        await RoomActionsMixin.user_list(self)

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.group_name,
            self.channel_name,
        )
        await self.close()
