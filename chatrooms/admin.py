from django.contrib import admin
from .models import ChatRoom, ChatMessage


@admin.register(ChatRoom)
class ChatRoomAdmin(admin.ModelAdmin):
    list_display=(
        "__str__",
        "created_at",
        "updated_at",
    )
    list_filter=(
        "created_at",
        "users",
        
    )
    
    

@admin.register(ChatMessage)
class ChatMessageAdmin(admin.ModelAdmin):
    list_display=(
       "text",
       "user",
       "room",
    )
    
