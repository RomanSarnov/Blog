from django import forms
from django.contrib.auth.forms import PasswordChangeForm, SetPasswordForm
from blog.models import Post,CustomUser
from django.utils.translation import gettext, gettext_lazy as _
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields=['title','body']

class UpdateUserForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'first_name', 'birthday','last_name','avatar')
        labels={'username':'Ник'}

