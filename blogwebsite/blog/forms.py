from .models import Comment
from django import forms

class CommentForm(forms.ModelForm):
	class Meta:
		model = Comment
		fields = ['parent_id', 'name', 'email', 'content']
		widgets = {'parent_id': forms.HiddenInput()}

