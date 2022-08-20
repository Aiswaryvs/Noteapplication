from django.forms import ModelForm
from django import forms
from notes.models import Notes

class NotesForm(ModelForm):
    class Meta:
        model=Notes
        fields=["title","content","image"]
        widgets={
            "title":forms.TextInput(attrs={"class":"form-control"}),
            "content":forms.Textarea(attrs={"class":"form-control"}),
            "image":forms.FileInput(attrs={"class":"form-control"})

        }
