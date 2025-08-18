from django.db import models
from django.contrib.auth.models import User, AbstractUser

# Create your models here.

# --------------------
# Base User (common for both Employee and TeamLead)
# --------------------
class User(AbstractUser):
    is_employee = models.BooleanField(default=False)
    is_team_lead = models.BooleanField(default=False)
    joined_date = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.username


# --------------------
# Team
# --------------------
class Team(models.Model):
    team_id = models.AutoField(primary_key=True)
    team_name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey("TeamLead", on_delete=models.CASCADE, related_name="created_teams")

    def __str__(self):
        return self.team_name

# --------------------
# Employee
# --------------------
class Employee(models.Model):
    employee_id = models.AutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    team = models.ForeignKey(Team, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"Employee: {self.user.username} - {self.employee_id}"

# --------------------
# Team Lead
# --------------------
class TeamLead(models.Model):
    team_lead_id = models.AutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    team = models.ForeignKey(Team, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"Team Lead: {self.user.username} - {self.team_lead_id}"


# --------------------
# Task
# --------------------
class Task(models.Model):
    task_id = models.AutoField(primary_key=True)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    assigned_to = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name="tasks")

    title = models.CharField(max_length=255)
    description = models.TextField()
    status = models.CharField(max_length=50, choices=[
        ("pending", "Pending"),
        ("in_progress", "In Progress"),
        ("completed", "Completed"),
    ])
    priority = models.CharField(max_length=50, choices=[
        ("low", "Low"),
        ("medium", "Medium"),
        ("high", "High"),
    ])
    due_date = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title} ({self.status}) ({self.priority})"


# --------------------
# Mood Check-in
# --------------------
class MoodCheckin(models.Model):
    checkin_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(Employee, on_delete=models.CASCADE)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    mood = models.CharField(max_length=50, choices=[
        ("happy", "Happy"),
        ("neutral", "Neutral"),
        ("stressed", "Stressed"),
        ("burnout", "Burnout"),
    ])
    notes = models.TextField(blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.user.username} - {self.mood}"


# --------------------
# Insight Report
# --------------------
class InsightReport(models.Model):
    report_id = models.AutoField(primary_key=True)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    generated_by = models.ForeignKey(TeamLead, on_delete=models.CASCADE)
    summary_text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Report {self.report_id} - {self.team.team_name}"