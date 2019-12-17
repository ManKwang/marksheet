from django import forms as f


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
