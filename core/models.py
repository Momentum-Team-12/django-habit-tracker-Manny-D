from django.db import models
from datetime import datetime
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    def __repr__(self):
        return f"<User username={self.username}>"

    def __str__(self):
        return self.username

class Habit(models.Model):
	name = models.CharField(max_length=200, null=True, blank=True)
	goal = models.IntegerField
	unit = models.CharField(max_length=100)
	created_at = models.DateField(auto_now_add=True)
	user = models.ForeignKey('User', null=True, blank=True,on_delete=models.CASCADE, related_name='habits')

	def __str__(self):
	    return self.name

class Record(models.Model):
	date = models.DateField(auto_now_add=datetime.now)
	habit = models.ForeignKey('Habit', null=True, blank=True,on_delete=models.CASCADE, related_name='habit_record')
	user = models.ForeignKey('User', null=True, blank=True,on_delete=models.CASCADE, related_name='habit_user_record')
	
	class Meta:
		constraints = [
			models.UniqueConstraint(fields=['date','habit'], name='daily')
		]

	def __str__(self):
	    return self.habit