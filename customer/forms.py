from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):

    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', )


class LoginForm(forms.Form):

    user = None

    username = forms.CharField()
    password = forms.CharField()

    def __init__(self, *args, **kwargs):

        self.request = kwargs.pop('request', None)
        return super(LoginForm, self).__init__(*args, **kwargs)

    def clean(self):

        username = self.cleaned_data['username']
        password = self.cleaned_data['password']

        user = authenticate(self.request, username=username, password=password)
        if not user:
            raise forms.ValidationError("Username or password is not valid")

        self.user = user
        
        return self.cleaned_data

