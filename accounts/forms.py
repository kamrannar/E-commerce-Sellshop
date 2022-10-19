from django import forms
from .models import Billing,Different_shipping
from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model

User = get_user_model()


class BillingForm(forms.ModelForm):
    class Meta:
        model = Billing
        fields = '__all__'


class Different_shippingForm(forms.ModelForm):
    class Meta:
        model = Different_shipping
        fields = '__all__'


class RegisterForm(forms.ModelForm):
    confirm_password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ['first_name', 'last_name','email', 'username', 'password','confirm_password']

    def clean(self):
        super().clean()
        if self.cleaned_data['password'] != self.cleaned_data['confirm_password']:
            raise ValidationError('Passwords are not equal')

        # return super(RegisterForm,self).clean()
