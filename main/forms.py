from django import forms as f
from django.contrib.auth.models import User, Group
from django.core.exceptions import EmptyResultSet
from main.models import Classes, Code
from datetime import datetime


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


class SignInForm(f.Form):
    email = f.EmailField(required=True)
    password = f.CharField(required=True, max_length=32, widget=f.PasswordInput)

    attrs = {
        'class': 'form-control'
    }

    email.widget.attrs.update({**attrs, **{
        'placeholder': 'Email',
        'autofocus': 'autofocus'
    }})

    password.widget.attrs.update({**attrs, **{
        'placeholder': 'Пароль',
        'style': 'margin-bottom: 10px;',
    }})


class CreateClassForm(f.Form):
    school_name = f.CharField(required=True, max_length=255)
    year = f.IntegerField(min_value=10, max_value=99, required=True)
    director_name = f.CharField(required=True, max_length=255)

    attrs = {
        'class': 'form-control'
    }

    school_name.widget.attrs.update({**attrs, **{
        'placeholder': 'Назва НЗ',
        'autofocus': 'autofocus'
    }})

    year.widget.attrs.update({**attrs, **{
        'placeholder': 'Рік (2 цифри)',
    }})

    director_name.widget.attrs.update({**attrs, **{
        'placeholder': 'Ім\'я директора',
    }})

    def save(self, code, user):
        class_ = Classes()
        class_.director_name = self.cleaned_data['director_name']
        class_.year = self.cleaned_data['year']
        class_.school_name = self.cleaned_data['school_name']

        code_ = Code.objects.get(code=code)

        class_.assigned_code = code_
        class_.created_by = user
        class_.created_at = datetime.now()

        class_.save()

        return class_


class AddStudentForm(f.Form):
    first_name = f.CharField(max_length=40, required=True, label='Ім\'я')
    last_name = f.CharField(max_length=50, required=True, label='Прізвище')
    third_name = f.CharField(max_length=50, required=True, label='По батькові')
    passport_lot = f.CharField(required=True, label='Серія паспорта', max_length=2)
    passport_number = f.CharField(required=True, label='Номер паспорта', max_length=10)
    gender = f.ChoiceField(required=True, widget=f.Select(), choices=([('m', 'Ч'), ('f', 'Ж')]), label='Стать')

    attrs = {
        'class': 'form-control'
    }

    first_name.widget.attrs.update({**attrs, **{
        'placeholder': 'Ім\'я',
        'autocomplete': 'off',
    }})

    last_name.widget.attrs.update({**attrs, **{
        'placeholder': 'Прізвище',
        'autocomplete': 'off',
    }})

    third_name.widget.attrs.update({**attrs, **{
        'placeholder': 'По батькові',
        'autocomplete': 'off',
    }})

    passport_lot.widget.attrs.update({**attrs, **{
        'placeholder': 'Серія',
        'autocomplete': 'off',
    }})

    passport_number.widget.attrs.update({**attrs, **{
        'placeholder': 'Номер паспорта',
        'autocomplete': 'off',
    }})

    gender.widget.attrs.update(attrs)
