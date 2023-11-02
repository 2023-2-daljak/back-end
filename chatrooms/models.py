from django.db import models
from common.models import Common


class ChatRoom(Common):
    """Chatroom Model Definition"""

    users = models.ManyToManyField(
        "users.User",

    )

    def __str__(self) -> str:
        return "ChattingRoom"


class ChatMessage(Common):
    """ChatMessage Model Definition"""

    text = models.TextField()
    user = (
        models.ForeignKey(
            "users.User", null=True, blank=True, on_delete=models.SET_NULL
        ),
    )
    room = (
        models.ForeignKey(
            "chatrooms.ChatRoom",
            on_delete=models.CASCADE,
            related_name="messages",
        ),
    )

    def __str__(self):
        return f"{self.user} says {self.text}"
