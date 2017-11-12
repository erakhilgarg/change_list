from django.contrib import admin
from .models import Node


class NodeAdmin(admin.ModelAdmin):
    list_display = ('name', 'ip',)


admin.site.register(Node, NodeAdmin)

