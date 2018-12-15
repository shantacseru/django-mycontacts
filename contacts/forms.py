from django import forms
from .models import Contacts
from django.contrib.auth.models import User
from django.forms import CharField, Form, PasswordInput
from django.contrib.auth import authenticate


class ContactForm(forms.ModelForm):
    user_id = forms.CharField(
        widget=forms.TextInput(attrs={'value': "default", 'type': 'hidden'})
    )

    class Meta:
        model = Contacts
        fields = ['user_id', 'first_name', 'last_name', 'email', 'phone_number', 'city', 'street', 'house', 'post_code',
                  'state', 'country']


class SignInForm(forms.Form):
    username = forms.CharField(
        max_length=150,
        widget=forms.TextInput(attrs={'class': "form-control"})
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': "form-control"})
    )

    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if username and password:
            # authenticate that the user is exist
            user = authenticate(username=username, password=password)

            if not user:  # if does not give a user model object
                raise forms.ValidationError('User does not exist')

            if not user.check_password(password):
                raise forms.ValidationError('Incorrect password')

            if not user.is_active:
                raise forms.ValidationError('User is no longer active')

        return super(SignInForm, self).clean(*args, **kwargs)


class SignUpForm(forms.ModelForm):
    password = forms.CharField(
        widget=PasswordInput()
    )

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password']
