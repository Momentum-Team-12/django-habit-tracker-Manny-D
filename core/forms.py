from django import forms
from .models import Habit, Record


class HabitForm(forms.ModelForm):
    class Meta:
        model = Habit
        fields = [
            'name',
            'goal',
            'unit',
        ]

class RecordForm(forms.ModelForm):
    class Meta:
        model = Record
        fields = [
            'date',
            'record'
        ]

# class FavoriteForm(forms.ModelForm):
#         class Meta:
#             model = Favorite
#             fields = [
#         ]

# class CreateUserForm(UserCreationForm):
#     class Meta:
#         model = User
#         fields = [
#             'username',
#             'email',
#             'password1',
#             'password2',
#         ]