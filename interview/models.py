from django.db import models
from application.models import Application

# Create your models here.
class Interview(models.Model):
    applicant = models.ForeignKey(Application, on_delete=models.SET_NULL, null=True, blank=True)