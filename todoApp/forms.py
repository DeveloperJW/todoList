from django import forms
from .models import List


# Custom Form for Admin usage
class ListForm(forms.ModelForm):
    class Meta:
        model = List
        fields = ["item", "detail", "completed"]


