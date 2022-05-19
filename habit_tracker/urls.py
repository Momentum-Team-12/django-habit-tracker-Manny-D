"""example URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django import views
from django.conf import settings
from django.contrib import admin
from django.urls import path
from django.urls import include
from core import views as habits_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('registration.backends.simple.urls')),
    path('', habits_views.home , name='home'),
    path('habits/', habits_views.list_habits, name='list_habits'),
    path('habits/<int:pk>',habits_views.habit_detail, name='habit_detail'),
    path('habits/<int:pk>/record/', habits_views.records_habit,name='records_habit'),
    path('habits/<int:pk>/edit/', habits_views.edit_habit,name='edit_habit'),
    path('habits/new/', habits_views.new_habit, name='new_habit'),
    path('habits/<int:pk>/delete/', habits_views.delete_habit, name='delete_habit'),
    path('habits/<int:pk>/add_record/', habits_views.add_record, name='add_record'),
    path('habits/<int:pk>/edit_record/', habits_views.edit_record,name='edit_record'),
]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns += [
        path("__debug__/", include(debug_toolbar.urls)),
    ]