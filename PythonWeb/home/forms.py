from django import forms
import re
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
class RegistrationForm(forms.Form):
    username = forms.CharField(label="Tài khoản", max_length=30)
    email = forms.EmailField(label="Email")
    password1 = forms.CharField(label="Mật khẩu", widget =forms.PasswordInput())
    password2 = forms.CharField(label="Nhập lại mật khẩu", widget =forms.PasswordInput())
    def clean_password2(self):
        if 'password1' in self.cleaned_data: #kiem tra pass1 co nhap chua
            password1 = self.cleaned_data['password1']#lay du lieu pass1 va pass2
            password2 = self.cleaned_data['password2']
            if password1 == password2 and password1:#tranh truong hop go dau cach lien tuc
                return password2
        raise forms.ValidationError("Mật khẩu không hợp lệ")
    def clean_username(self):
        username = self.cleaned_data['username']
        if not re.search(r'^\w+$',username):#kiem tra ten tk co ky tu db hay khong
            raise forms.ValidationError("Tên tài khoản có ký tự đặc biệt")
        try:
            User.objects.get(username=username)#kiem tra xem username co trung ko
        except ObjectDoesNotExist:
            return username
        raise forms.ValidationError("Tài khoản đã tồn tại")
    def save(self):
        User.objects.create_user(username=self.cleaned_data['username'],email=self.cleaned_data['email'],password=self.cleaned_data['password1'])