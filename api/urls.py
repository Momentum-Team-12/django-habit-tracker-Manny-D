from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from api import views as api_views

urlpatterns = [
    path('root', api_views.api_root),

    path('users', api_views.UserList.as_view(), name='api-user-list'), # working
    path('user/<int:pk>', api_views.UserDetail.as_view(), name='api-user-detail'), # working -> note user singular

    path('habits', api_views.HabitListView.as_view(), name='api-habits-list'), # working
    path('habits/create', api_views.HabitCreateView.as_view(), name='api-habit-create'), # working
    path('habits/<int:pk>', api_views.HabitDetail.as_view(), name='api-habit-detail'), # working

    path('habits/<int:pk>/records', api_views.RecordDetail.as_view(), name='api-record-detail'),# working - but would like another way to see the list of records / record details / can update (PATCH) here ok too

    path('habits/<int:pk>/record/create', api_views.RecordCreateView.as_view(), name='api-record-create'), # testing / working but functionality is odd
]

urlpatterns = format_suffix_patterns(urlpatterns)