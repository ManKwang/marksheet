from django.db import models as m
from django.contrib.auth.models import User
from datetime import date


# Create your models here.
class Code(m.Model):
    code = m.CharField(max_length=255, unique=True)
    due_to = m.DateField()
    amount = m.IntegerField()
    assigned_to = m.ForeignKey(User, on_delete=m.CASCADE)
    created_at = m.DateTimeField()

    @property
    def is_past_due(self):
        return date.today() > self.due_to

    def __str__(self):
        return self.code


class Classes(m.Model):
    school_name = m.CharField(max_length=255)
    year = m.SmallIntegerField()
    director_name = m.CharField(max_length=255)
    assigned_code = m.ForeignKey(Code, on_delete=m.CASCADE)
    created_by = m.ForeignKey(User, on_delete=m.CASCADE)
    created_at = m.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{} - {}'.format(self.school_name, self.created_at)


class Students(m.Model):
    first_name = m.CharField(max_length=40)
    last_name = m.CharField(max_length=50)
    third_name = m.CharField(max_length=50)
