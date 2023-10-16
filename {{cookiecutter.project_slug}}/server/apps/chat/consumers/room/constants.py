from typing import Final


class Actions:
    USER_LIST: Final[str] = "user_list"
    SEND_MESSAGES: Final[str] = "send_message"


class Events:
    EVENT_USERS_RETRIEVE: Final[str] = "event_users_retrieve"
    MESSAGE_NEW: Final[str] = "message_new"
