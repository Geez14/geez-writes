from django import forms
from .models import BlogPost


class PostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ("title", "author", "body")
        # form-control is the class needed in bootstrap integration
        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control",id:"text-input", "placeholder":"Enter title for this blog"}),
            "author": forms.Select(attrs={"class": "form-control", id:"select-author"}),
            "body": forms.Textarea(attrs={"class": "form-control", id:"body-content", "placeholder":"Enter Your Blog here in Markdown"}),
        }