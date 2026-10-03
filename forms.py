from django import forms
from .models import Project, Inquiry, Testimony

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = '__all__'