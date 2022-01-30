from django import forms
from projects.models import Bug, Project

class ProjectCreationForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['proj_name', 'org_name', 'domain']