from django.db import models
from django.utils import timezone

class cita (models.Model):
    hora=models.TimeField
    user=models.AutoField
