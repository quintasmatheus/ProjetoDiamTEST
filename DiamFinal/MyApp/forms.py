from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import CustomUser, Boleia


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    car_brand = forms.CharField(max_length=100, required=True)
    car_model = forms.CharField(max_length=100, required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', 'car_brand', 'car_model')

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        customUser = CustomUser(user=user, car_brand=self.cleaned_data['car_brand'], car_model=self.cleaned_data['car_model'])
        if commit:
            user.save()
            customUser.save()

        user.save()
        customUser.save()
        return user