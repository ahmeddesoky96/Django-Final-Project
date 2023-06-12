import re
from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from .models import MyUser
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate


from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from .models import MyUser

class MyUserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    confirm_password = forms.CharField(widget=forms.PasswordInput(), label=_('Confirm password'))
    image = forms.CharField(max_length=50)
    birth_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}), label=_('Date of birth'))

    class Meta:
        model = MyUser
        fields = ['first_name', 'last_name', 'email', 'password', 'confirm_password', 'phone_number', 'image', 'birth_date', 'facebook_profile', 'country']


    def clean_email(self):
        email = self.cleaned_data.get('email')
        if MyUser.objects.filter(email=email).exists():
            raise ValidationError(_('This email address is already in use.'))
        elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
            raise ValidationError(_('Enter a valid email address.'))
        return email

    def clean_phone_number(self):
        phone_number = self.cleaned_data.get('phone_number')
        if not phone_number.isdigit():
            raise ValidationError(_('Phone number must contain only digits.'))
        return phone_number

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')
        if password and confirm_password and password != confirm_password:
            raise ValidationError(_('The passwords do not match.'))
        return cleaned_data
    


class EmailAuthenticationForm(AuthenticationForm):
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'placeholder': 'Email'}))
    username = forms.CharField(label='Username', widget=forms.TextInput(attrs={'placeholder': 'Username'}), required=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password'].widget.attrs['placeholder'] = 'Password'

    def clean(self):
        email = self.cleaned_data.get('email')
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        if email and password:
            # Authenticate using email and password
            self.user_cache = authenticate(email=email, password=password)
            if self.user_cache is None:
                # Authentication failed, try username and password
                self.user_cache = authenticate(username=username, password=password)
                if self.user_cache is None:
                    raise forms.ValidationError(
                        self.error_messages['invalid_login'],
                        code='invalid_login',
                        params={'email': self.username_field.verbose_name},
                    )
        return self.cleaned_data