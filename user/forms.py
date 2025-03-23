from django import forms
from django.contrib.auth.models import User
from .models import UserImage, Comment


class RegisterForm(forms.ModelForm):
    confirm_password = forms.CharField(max_length=128, widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password']
        widgets = {
            'password': forms.PasswordInput()
        }

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')
        if password and confirm_password and password != confirm_password:
            raise forms.ValidationError("Parollar mos emas!")
        return cleaned_data
    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user
        


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content', 'likes', 'rate']
        # widgets = {
        #     'likes': forms.BooleanField(),
        #     'rate': forms.BooleanField()
        # }



class UpdateUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']



class UserImageForm(forms.ModelForm):
    class Meta:
        model = UserImage
        fields = ['image']