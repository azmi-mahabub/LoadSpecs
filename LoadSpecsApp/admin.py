from django.contrib import admin
from .models import User, TeamLead, Employee, Team, MoodCheckin, Task, InsightReport
admin.site.register([User, TeamLead, Employee, Team, MoodCheckin, Task, InsightReport])

# Register your models here.
