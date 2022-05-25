from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.reverse import reverse
from rest_framework.response import Response
from rest_framework import generics
from core.models import Habit, User, Record
from api.serializers import HabitSerializer, UserSerializer, RecordSerializer

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': reverse('api-user-list', request=request, format=format),
        'habits': reverse('api-habit-list', request=request, format=format),
        'records': reverse('api-record-list', request=request, format=format),
    })

#from class - working as a GET but not POST / changing arg to ListCreateAPIView may work but needs modification
class HabitListView(APIView):
    def get(self, request, format=None):
        """
        Return JSON list of all habits
        """
        habits = Habit.objects.filter(user=request.user)
        serializer = HabitSerializer(habits, many=True)
        return Response(serializer.data)

#from drf tutorial and likely will change
class HabitDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer

#working
class UserList(generics.ListAPIView):
	queryset = User.objects.all()
	serializer_class = UserSerializer

#from drf tutorial - not working
class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

#testing - not working
class RecordDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Record.objects.all()
    serializer_class = RecordSerializer