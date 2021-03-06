# Generated by Django 4.0.4 on 2022-05-19 01:50

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_habit_goal_record_created_at_record_record_and_more'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='record',
            name='daily',
        ),
        migrations.AlterField(
            model_name='record',
            name='date',
            field=models.DateField(default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='record',
            name='habit',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='habit_records', to='core.habit'),
        ),
        migrations.AlterField(
            model_name='record',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='habit_records', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddConstraint(
            model_name='record',
            constraint=models.UniqueConstraint(fields=('date', 'habit'), name='daily_record'),
        ),
    ]
