from django import forms
from .models import Post

class WebAppForm(forms.ModelForm):
    post = forms.CharField(widget=forms.TextInput)

    class Meta:
        model = Post
        fields = ('post',)