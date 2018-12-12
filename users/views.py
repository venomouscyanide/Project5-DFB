from django.shortcuts import render
from django.urls import reverse_lazy
from .forms import CustomUserCreationFrom
from django.views.generic import CreateView
# Create your views here.
class SignUpView(CreateView):
	form_class=CustomUserCreationFrom
	success_url=reverse_lazy('login')
	template_name='signup.html'