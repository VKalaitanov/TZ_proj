from django.contrib import admin
from .models import Task

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    """
    Админка для модели Task.
    Отображает в списке название задачи и статус выполнения.
    """
    list_display = ('title', 'is_completed')
    search_fields = ('title',)
    list_filter = ('is_completed',)