from django.db import models
from datetime import date
from django.core.exceptions import ValidationError

# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    deadline = models.DateField()
    is_completed = models.BooleanField(default=False)

    class Meta:
        ordering = ['deadline']

    def clean(self):
        """ custom validation to ensure deadline is in future"""
        if self.deadline <= date.today():
            raise ValidationError("The deadline must be in the future.")
    
    def save(self, *args, **kwargs):
        """ Ensure clean is called before saving the object"""
        self.clean()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title