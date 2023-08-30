from django import forms

# from .models import MyModel
from .models import Task


class MyModelForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = "__all__"
