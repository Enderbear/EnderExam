from django import forms
from models import CustomUser


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = CustomUser
        fields = ['U_name', 'email', 'password']
        exclude = ['U_password']  # 不需要用户在注册时设置U_password，因为它将由模型处理

    def save(self, commit=True):
        # 重写save方法来处理密码加密
        user = super(RegisterForm, self).save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user