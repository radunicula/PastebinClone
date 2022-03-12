from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import TextInput
from users.models import ExtendUser


class UserForm(UserCreationForm):
    class Meta:
        model = ExtendUser
        fields = ['username', 'first_name', 'last_name', 'phone', 'email']
        widgets = {
            'username': TextInput(attrs={'placeholder': 'user name', 'class': 'form-control'}),
            'first_name': TextInput(attrs={'placeholder': 'first name', 'class': 'form-control'}),
            'last_name': TextInput(attrs={'placeholder': 'last name', 'class': 'form-control'}),
            'phone': TextInput(attrs={'placeholder': 'phone', 'class': 'form-control'}),
            'email': TextInput(attrs={'placeholder': 'email', 'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['placeholder'] = 'password'
        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['placeholder'] = 'confirm password'
