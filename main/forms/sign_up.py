from django import forms as f
from django.contrib.auth.models import User, Group


class SignUpForm(f.Form):
    email = f.EmailField(required=True)
    password = f.CharField(required=True, max_length=32, widget=f.PasswordInput)
    repeat_password = f.CharField(required=True, max_length=32, widget=f.PasswordInput)

    attrs = {
        'class': 'form-control'
    }

    email.widget.attrs.update({**attrs, **{
        'placeholder': 'Email',
        'autofocus': 'autofocus'
    }})

    password.widget.attrs.update({**attrs, **{
        'placeholder': 'Пароль',
    }})

    repeat_password.widget.attrs.update({**attrs, **{
        'placeholder': 'Пароль (ще раз)',
        'style': 'margin-bottom: 10px;'
    }})

    def clean(self):
        cleaned_data = super().clean()
        psw = cleaned_data.get('password')
        r_psw = cleaned_data.get('repeat_password')

        if psw != r_psw:
            self.add_error('repeat_password', 'Введені Вами паролі повинні збігатися')

    def save(self):
        user = User.objects.create_user(self.cleaned_data['email'], self.cleaned_data['email'],
                                        self.cleaned_data['password'])
        group = Group.objects.get(name='teacher')
        user.groups.add(group)
        user.save()

        return user
