# -*- coding: utf-8 -*-

from django import forms

class BasicForm(forms.Form):
    username = forms.CharField(required=True, max_length=20)
    mailbox = forms.EmailField(required=True)
    message = forms.CharField(required=True, max_length=300)