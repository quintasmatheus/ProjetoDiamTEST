from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User, Permission
from .models import CustomUser, Boleia


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(max_length=100, required=True)
    last_name = forms.CharField(max_length=100, required=True)
    car_brand = forms.CharField(max_length=100, required=True)
    car_model = forms.CharField(max_length=100, required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', 'first_name', 'last_name', 'car_brand', 'car_model')

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

class BoleiaForm(forms.ModelForm):
    class Meta:
        model = Boleia
        fields = ['partida', 'chegada', 'horario', 'preco', 'vagas', 'detalhes']

    horario = forms.DateTimeField(
        label='Data e hora da boleia (d/m/Y H:M)',
        input_formats=['%d/%m/%Y %H:%M'],
        widget=forms.DateTimeInput(attrs={
            'class': 'form-control datetimepicker-input',
            'data-target': '#datetimepicker1'
        })
    )