from rest_framework import serializers
from core.models import Habit

class HabitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habit
        fields = (
            'pk',
            'name',
            'goal',
            'unit',
        )
            