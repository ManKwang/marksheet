from django.db import models as m
from django.contrib.auth.models import User
from datetime import date


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
