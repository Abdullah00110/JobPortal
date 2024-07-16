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
    
@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ["user_id", "user_name", "institution" , "degree", "passing_year"]
    def user_name(self, obj):
        return obj.user.name if obj.user.name else ''
    
@admin.register(UserSkills)
class SkillAdmin(admin.ModelAdmin) :
    list_display = ["skill", "user_name", "user_id"]
    def user_name(self, obj):
        return obj.user.name if obj.user.name else ''
    def user_id(self, obj):
        return obj.user.id if obj.user.id else ''
    
@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ["user_name", "title", "role"]
    def user_name(self, obj):
        return obj.user.name if obj.user.name else ''

@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ["user_name", "job_role", "experience_year", "company"]
    def user_name(self, obj):
        return obj.user.name if obj.user.name else ''
    
    
    
