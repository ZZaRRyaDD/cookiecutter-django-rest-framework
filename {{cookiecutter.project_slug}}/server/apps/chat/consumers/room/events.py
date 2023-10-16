class RoomEventsMixin:

    async def event_users_retrieve(self, event: dict) -> None:
        await self.send_event_response(event)

    async def message_new(self, event: dict) -> None:
        await self.send_event_response(event)
