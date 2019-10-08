from django.db import models as m
from django.contrib.auth.models import User
from .Code import Code


class Classes(m.Model):
    school_name = m.CharField(max_length=255)
    year = m.SmallIntegerField()
    director_name = m.CharField(max_length=255)
    assigned_code = m.ForeignKey(Code, on_delete=m.CASCADE)
    created_by = m.ForeignKey(User, on_delete=m.CASCADE)
    created_at = m.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{} - {}'.format(self.school_name, self.created_at)
