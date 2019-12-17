from django import forms as f
from main.models import Classes, Code
from datetime import datetime


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
