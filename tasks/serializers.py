from rest_framework import serializers
from .models import Task


class TaskSerializer(serializers.ModelSerializer):
    """
    Сериализатор для модели Task.
    """

    class Meta:
        model = Task
        fields = ['id', 'title', 'is_completed']

    def validate_title(self, value):
        """
        Валидация поля title: оно не должно быть пустым или состоять только из пробелов.
        """
        if not value.strip():
            raise serializers.ValidationError("Title cannot be empty.")
        return value