from django.db import models
from datetime import datetime
from calendar import HTMLCalendar
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    def __repr__(self):
        return f"<User username={self.username}>"

    def __str__(self):
        return self.username

class Habit(models.Model):
	name = models.CharField(max_length=200, null=True, blank=True)
	goal = models.IntegerField(default=0)
	unit = models.CharField(max_length=100)
	created_at = models.DateField(auto_now_add=True)
	user = models.ForeignKey('User', null=True, blank=True,on_delete=models.CASCADE, related_name='habits')

	def __str__(self):
	    return self.name

class Record(models.Model):
	created_at = models.DateTimeField(auto_now_add=True)
	date = models.DateTimeField(default=datetime.now)
	record = models.IntegerField(default=0)
	habit = models.ForeignKey('Habit', null=True, blank=True,on_delete=models.CASCADE, related_name='habit_records')
	user = models.ForeignKey('User', null=True, blank=True,on_delete=models.CASCADE, related_name='habit_records')
	
	class Meta:
		constraints = [
			models.UniqueConstraint(fields=['date','habit', 'user'], name='daily_record')
		]

	def __str__(self):
	    return self.habit