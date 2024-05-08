from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# class CreateUserForm(UserCreationForm):
#     class Meta:
#         model = User
#         fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']
#         widgets = {
#             'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}),
#             'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
#             'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}),
#             'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}),
#             'password1': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}),
#             'password2': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirm Password'}),
#         }


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Tên đăng nhập'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Họ'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Tên'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].widget = forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Mât khẩu'})
        self.fields['password2'].widget = forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Xác nhận mật khẩu'})