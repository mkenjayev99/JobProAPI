from django import forms
from .models import Account
from django.urls import reverse_lazy
from django.contrib.auth.forms import ReadOnlyPasswordHashField


class AccountFormsCreate(forms.ModelForm):
    password = forms.CharField(min_length=6, max_length=70, widget=forms.PasswordInput)
    password2 = forms.CharField(min_length=6, max_length=70, widget=forms.PasswordInput)

    class Meta:
        model = Account
        fields = ('email', 'role')

    def clean_password2(self):
        password = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password2')
        if password and password2:
            if password != password2:
                raise forms.ValidationError("Password did not match. Please, try again!")
            return password2
        raise forms.ValidationError("Enter the Password")

    def save(self, commit=True):
        account = super().save(commit=False)
        account.set_password(self.cleaned_data['password1'])
        if commit:
            account.save()
        return account


class AccountChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField

    class Meta:
        model = Account
        fields = ('email', 'image', 'first_name', 'last_name', 'role',
                  'bio', 'is_superuser', 'is_staff', 'is_active')

    def init(self, *args, **kwargs):
        super(AccountChangeForm, self).init(*args, **kwargs)
        self.fields['password'].help_text = "<a href='%s'>change password</a>" % reverse_lazy(
            "admin:auth_user_password_change", args=[self.instance.id]
        )

    def clean_password(self):
        return self.initial['password']

