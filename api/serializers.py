from rest_framework import serializers
from core.models import Habit, Record, User

class HabitSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Habit
        fields = (
            'user',
            'name',
            'pk',
            'goal',
            'unit',
        )

#copied from drf tutorial and will likely need to be updated
class UserSerializer(serializers.ModelSerializer): 
    
    class Meta:
        model = User
        fields = (
            'username',
            'id',
        )

# guessing this
class RecordSerializer(serializers.ModelSerializer):

    class Meta:
        model = Record
        fields = (
            'date',
            'record',
            'pk',
            'habit',
        )

# testing for later
class HabitRecordSerializer(serializers.ModelSerializer):
    results = RecordSerializer(many=True, required=False, source='record')
    user = serializers.ReadOnlyField(source='user.username')
    
    class Meta:
        model = Habit
        fields = ('user', 'id', 'habit', 'record')