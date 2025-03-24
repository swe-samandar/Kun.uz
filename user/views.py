from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from .models import UserImage
from .forms import RegisterForm,  UpdateUserForm, UserImageForm, CommentForm
from .models import Comment

class Register(View):
    def get(self, request):
        user_form =  RegisterForm()
        image_form = UserImageForm()
        context = {
            'user_form': user_form,
            'image_form': image_form,
        }

        return render(request, 'register.html', context=context)


    def post(self, request):
        user_form =  RegisterForm(request.POST)
        image_form = UserImageForm(request.FILES)
        context = {
            'user_form': user_form,
            'image_form': image_form,
            }
        
        if user_form.is_valid() and image_form.is_valid():
            user = user_form.save()
            image = image_form.save(commit=False)
            image.user = user
            image.save()
            return redirect('login')
        
        else:
            user_form =  RegisterForm()
            image_form = UserImageForm()

        return render(request, 'register.html', context=context)
        


class LoginUser(View):
    def get(self, request):
        form = AuthenticationForm()
        return render(request, 'login.html', {'form': form})


    def post(self, request):
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('dashboard')

        return render(request, 'login.html', {'form': form})



class Dashboard(LoginRequiredMixin, View):
    template_name = 'dashboard.html'
    login_url = 'login/' 

    def get(self, request):
        profile = UserImage.objects.filter(user=request.user).first()
        return render(request, 'dashboard.html', {'profile': profile})



class UpdateUser(LoginRequiredMixin, View):
    template_name = 'update_user.html'
    login_url = 'login/' 

    def get(self, request):
        user = get_object_or_404(User, id=request.user.id)
        image = UserImage.objects.filter(user=user).first()
        user_form = UpdateUserForm(instance=user)
        image_form = UserImageForm(instance=image)
        return render(request, 'update_user.html', {'user_form': user_form, 'image_form': image_form})


    def post(self, request):
        user = get_object_or_404(User, id=request.user.id)
        image = UserImage.objects.filter(user=user).first()
        user_form = UpdateUserForm(request.POST, instance=user)
        image_form = UserImageForm(request.POST, request.FILES, instance=image)
        if user_form.is_valid() and image_form.is_valid():
            user = user_form.save()
            image = image_form.save(commit=False)
            image.user = user
            image.save()
            return redirect('dashboard')
        
        else:
            user = get_object_or_404(User, id=request.user.id)
            user_form = UpdateUserForm(instance=user)
            image_form = UserImageForm()
        return render(request, 'update_user.html', {'user_form': user_form, 'image_form': image_form})



class UpdateUserImage(LoginRequiredMixin, View):
    template_name = 'update_image.html'
    login_url = 'login/' 

    def get(self, request):
        profile = UserImage.objects.filter(user=request.user).first()
        form = UserImageForm(instance=profile)
        return render(request, 'update_image.html', {'form':form})


    def post(self, request):
        profile = UserImage.objects.filter(user=request.user).first()
        form = UserImageForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            image = form.save(commit=False)
            image.user = request.user
            image.save()
            return redirect('dashboard')
        
        else:
            form = UserImageForm()
        
        return render(request, 'update_image.html', {'form':form})



class LogoutUser(View):
    def get(self, request):
        logout(request)
        return redirect('login')