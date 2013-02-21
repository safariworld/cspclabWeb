# -*- coding: utf-8 -*-
from django import forms
from models import WritingEntries, CommentsModel
from django.forms import Textarea, TextInput
class WriteForm(forms.ModelForm):
    class Meta:
        model = WritingEntries
        exclude = ('user',)
        fields = ('category', 'title', 'content', 'attachedFile')
        widgets = {
                'content':Textarea(attrs={'class':'ckeditor'}),
            'title':TextInput(attrs={'class':'input-medium'}),
        }
class CommentForm(forms.ModelForm):
    class Meta:
        model = CommentsModel
        exclude = ('user',)
        fields = ('content',)
