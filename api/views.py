from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from core.models import Habit
from api.serializers import HabitSerializer

class HabitListView(APIView):
    def get(self, request, format=None):
        """
        Return JSON list of all habits
        """
        habits = Habit.objects.filter(user=request.user)
        serializer = HabitSerializer(habits, many=True)
        return Response(serializer.data)