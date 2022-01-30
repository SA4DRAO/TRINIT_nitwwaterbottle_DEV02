from django.db import models
from django.contrib.auth.models import User
from django.forms import ModelForm
# Create your models here.
SEVERITY = (
        ("Severe","Severe"),
        ("Moderate","Moderate"),
        ("Mild","Mild")
)

STATUS = (
        ("Open","Open"),
        ("In Progress","In Progress"),
        ("To be Re-Assigned","To be Re-Assigned"),
        ("Closed","Closed")
)


class Project(models.Model):
    team_leader = models.ForeignKey(User, on_delete=models.CASCADE)
    proj_name = models.CharField(max_length=50);
    org_name = models.CharField(max_length=50)
    domain = models.CharField(max_length=50)
    
    def __str__(self):
        return self.proj_name



class Bug(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    description = models.CharField (max_length=400)
    severity = models.CharField(max_length=50, choices=SEVERITY)
    status = models.CharField(max_length=50, choices=STATUS)

    def __str(self):
        return self.title
    


# class SaveProject():
#         model = Project
#         field = ['project_name', 'organization_name', 'project_technology']