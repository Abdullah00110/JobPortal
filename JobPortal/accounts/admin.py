from django.contrib import admin
from accounts.models import *
from django.contrib.auth.admin import UserAdmin
# Register your models here.

class UserModelAdmin(UserAdmin):
    list_display = ["email" , "name" , "tc", "is_admin"]
    list_filter = ["is_admin"]
    fieldsets = [
        
        (None, {"fields": ["email", "password"]}),
        ("Personal info", {"fields": ["name", "tc"]}),
        ("Permission", {"fields":["is_admin"]})
    ]
    
    add_fieldsets = [
        
        (
            None,
            {
                "classes": ["wide"],
                "fields" : ["email", "name", "tc", "password", "password2"],
            },
        ),
    ]
    
    search_fields = ["email"]
    ordering = ["email", "name"]
    filter_horizontal = []
    
    
admin.site.register(User, UserModelAdmin)

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin) :
    list_display = ["user_name", "image"]

    def user_name(self, obj):
        return obj.user.name if obj.user.name else ''
    
