from django.shortcuts import render
from django.contrib.auth import login, get_user_model
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import DetailView, ListView, UpdateView
from accounts.forms import UserRegisterForm
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth import update_session_auth_hash
# Create your views here.

def register_view(request, *args, **kwargs):
    context = {}
    form = UserRegisterForm()
    if request.method == 'POST':
        form = UserRegisterForm(data=request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            form.save()
            return redirect('product-list')
        context['form'] = form