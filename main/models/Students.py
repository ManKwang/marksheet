from django.db import models as m
from .Classes import Classes


class Students(m.Model):
    first_name = m.CharField(max_length=40)
    last_name = m.CharField(max_length=50)
    third_name = m.CharField(max_length=50)
    assigned_class = m.ForeignKey(Classes, on_delete=m.CASCADE)
    passport_lot = m.CharField(max_length=2)
    passport_number = m.CharField(max_length=10)
    gender = m.CharField(max_length=1)
