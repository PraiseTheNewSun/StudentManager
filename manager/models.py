from django.db import models

# Create your models here.
class StudentInfo(models.Model):
    first_name = models.CharField(max_length=300)
    last_name = models.CharField(max_length=300)
    level = models.IntegerField()
    address = models.CharField(max_length=300)
    email = models.EmailField(max_length=300)

    def __str__(self):
        return self.first_name + self.last_name