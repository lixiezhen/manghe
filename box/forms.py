from django import forms
from django.contrib.auth.models import User
from .models import Man_box,Woman_box,Comment
class Man_boxForm(forms.ModelForm):
    class Meta:
        model = Man_box
        fields =('user','name','email','age','gender','school',
                'area','qq','mobile','intro','photo','cover')

class Woman_boxForm(forms.ModelForm):
    class Meta:
        model = Woman_box
        fields =('user','name','email','age','gender','school',
                'area','qq','mobile','intro','photo','cover')

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ("commentator", "body",'pre_comment',)


