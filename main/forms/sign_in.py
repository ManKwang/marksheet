from django import forms as f


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
