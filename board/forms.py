# -*- coding: utf-8 -*-
from django import forms
from models import WritingEntries, CommentsModel

class WriteForm(forms.ModelForm):
    class Meta:
        model = WritingEntries
        exclude = ('user',)
        fields = ('category', 'title', 'content', 'attachedFile')

class CommentForm(forms.ModelForm):
    class Meta:
        model = CommentsModel
        fields = ('content',)
