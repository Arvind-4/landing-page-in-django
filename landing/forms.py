from django import forms
from .models import Register

class RegisterForm(forms.Form):
    email = forms.EmailField(widget=forms.TextInput(attrs={
        'class': 'form-control form-control-lg',
        'label': '',
        'placeholder': 'Email Address ...'
    }))

    # def clean_email(self, *args, **kwargs):
    #     email_form = self.cleaned_data.get('email')
    #     qs = Register.objects.all().filter(email=email_form)
    #     if qs.exists():
    #         information = 'Email already Registered!'
    #         raise forms.ValidationError(information)
    #     return email_form
