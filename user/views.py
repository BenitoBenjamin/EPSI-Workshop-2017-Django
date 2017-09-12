from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
)

from user.forms import CustomRegistration

class Registration(CreateView):
    template_name = "user/registration.django"
    form_class = CustomRegistration
    success_url = reverse_lazy("news:index")

# Create your views here.
