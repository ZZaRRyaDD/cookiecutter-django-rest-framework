from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class ChatConfig(AppConfig):
    """Class-configuration of chat app."""

    name = 'apps.chat'
    verbose_name = _("Chat")
