from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.db import models
from django.db.models import JSONField, Q

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

class HistoryManager(models.Manager):
    def filter_by_products(self, product1_id, product2_id):
        return self.filter(Q(product_id__contains=[product1_id]) | Q(product_id__contains=[product2_id]))

class History(models.Model):
    id = models.AutoField(primary_key=True)
    account_id = models.ForeignKey(User, on_delete=models.CASCADE)
    product_id = JSONField()
    time = models.DateTimeField(auto_now_add=True)

    objects = HistoryManager()  # Sử dụng custom manager

    def __str__(self):
        return str(self.product_id)

    class Meta:
        db_table = 'history'