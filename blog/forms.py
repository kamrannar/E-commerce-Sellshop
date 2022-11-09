from django import forms
from .models import Comment


class CommentsForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name','email','comment')
        widgets = {
          'comment': forms.Textarea(attrs={'rows':4, 'cols':30}),
        }