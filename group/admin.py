from django.contrib import admin
from group.models import Group


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    pass
