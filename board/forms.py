# -*- coding: utf-8 -*-
from django import forms
from models import WritingEntries

class WriteForm(forms.ModelForm):
    class Meta:
        model = WritingEntries
        fields = ('category', 'title', 'content')
