from django import forms
from django.contrib.auth.models import User
from .models import Profile

# Log form
class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

# User registration form

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Password',
                               widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat password',
                                widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'email')

    # Checks the second password against the first one
    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Password don\'t match.')
        return cd['password2']

class UserEditForm(forms.ModelForm):
    """Allows to edit first name, last name, email."""
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')

class ProfileEditForm(forms.ModelForm):
    """Allows to edit date of birth and upload picture."""
    class Meta:
        model = Profile
        fields = ('date_of_birth', 'photo')