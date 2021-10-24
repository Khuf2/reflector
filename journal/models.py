from django.db import models
from django.contrib.auth.models import User

from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class Journal_Page(models.Model):
    
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    pub_date = models.DateField('Date')

    satisfaction_rating = models.IntegerField(default=0, validators=[MinValueValidator(1), MaxValueValidator(10)])
    stress_rating = models.IntegerField(default=0, validators=[MinValueValidator(1), MaxValueValidator(10)])

    fitness_num = models.IntegerField(default=0, validators=[MinValueValidator(1), MaxValueValidator(10)])
    fitness_resp = models.TextField(blank=True)
    
    nutrition_num = models.IntegerField(default=0, validators=[MinValueValidator(1), MaxValueValidator(10)])
    nutrition_resp = models.TextField(blank=True)
    
    productivity_num = models.IntegerField(default=0, validators=[MinValueValidator(1), MaxValueValidator(10)])
    productivity_resp = models.TextField(blank=True)
    
    social_num = models.IntegerField(default=0, validators=[MinValueValidator(1), MaxValueValidator(10)])
    social_resp = models.TextField(blank=True)
    
    sleep_num = models.IntegerField(default=0, validators=[MinValueValidator(1), MaxValueValidator(10)])
    sleep_resp = models.TextField(blank=True)

    extra_resp = models.TextField(blank=True)

    def __str__(self):
        return str(self.author) + ':' + str(self.pub_date)

    class Meta:
       unique_together = ("author", "pub_date")