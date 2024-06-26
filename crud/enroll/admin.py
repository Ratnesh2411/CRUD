from django.contrib import admin

from . import models

@admin.register(models.userProfile)
class UserprofileAdmin(admin.ModelAdmin):
    list_display = ('id','name','email','password')


