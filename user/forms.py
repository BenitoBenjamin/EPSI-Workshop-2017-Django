from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
    
class CustomRegistration(RegistrationForm):
    user_pref_1 = form.CharField(**kwargs)
    user_pref_2 = form.CharField(**kwargs)
    
    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")
    
    def clean_email(self):
        data = self.cleaned_data["email"]
        if User.objects.filter(email=data).exists():
            raise forms.ValidationError("Email déjà existant")
        return data

    def save(self, *args, **kwargs):
        user = super(CustomRegistration, self).save(*args, **kwargs)
        profile = Profile()
        profile.user = user
        profile.user_pref_1 = self.cleaned_data["user_pref_1"]
        profile.user_pref_2 = self.cleaned_data["user_pref_2"]
        profile.save()
        return user