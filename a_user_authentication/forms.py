from django import forms 
from django.utils.safestring import mark_safe 

from allauth import account
class LoginForm(account.forms.LoginForm):
    def __init__(self, *args, **kwargs): 
        super().__init__(*args, **kwargs)

        if 'password' in self.fields:
            self.fields['password'].help_text = '<a href="/accounts/password/reset/">Forgot Password</a>'
        
        self.fields['password'].label = mark_safe('<i class="fa-solid fa-lock"> </i>')
        self.fields['login'].label = mark_safe('<i class="fa-solid fa-user"> </i>')
