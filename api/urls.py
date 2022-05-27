from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from api import views as api_views

urlpatterns = [
    path('habits', api_views.HabitListView.as_view(), name='api-habits-list'), # working

    path('habits/create', api_views.HabitCreateView.as_view(), name='api-habit-create'), # testing

    path('habits/<int:pk>', api_views.HabitDetail.as_view(), name='api-habit-detail'), # working
    path('users', api_views.UserList.as_view(), name='api-user-list'), # working
    path('user/<int:pk>', api_views.UserDetail.as_view(), name='api-user-detail'), # working -> note user singular
    path('root', api_views.api_root),

    path('habits/record/<int:pk>', api_views.RecordDetail.as_view(), name='api-record-detail'),# working - but need another way to see the list of records / record details
]

urlpatterns = format_suffix_patterns(urlpatterns)