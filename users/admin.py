from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User


@admin.register(User)
class customUserAdmin(UserAdmin):
    fieldsets=(
        ("Profile",
         {
            "fields":("username","password",
                      "email","avatar",
                      "gender","birth",
                      "nickname","phone_num",
                      "location","user_kind"),
            "classes":("wide",)     
        },
         ),
        ("Permissions",
         {
             "fields":(
                "is_active",
                "is_staff",
                "is_superuser",
                "groups",
                "user_permissions", 
             ),
             "classes":("collapse",)
         },
         ),
        ("Important Dates",
         {
          "fields": ("last_login", "date_joined"
                               ),
                    "classes" : ("collapse",)
         },
         )
    )
