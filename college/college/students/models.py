from django.db import models
from django.contrib.auth.models import User


class Student(models.Model):
    student_name = models.CharField(max_length=100)
    student_email = models.TextField(unique=True)
    student_phone = models.IntegerField()
    ssc_marks = models.IntegerField()
    inter_marks = models.IntegerField()
    is_verified = models.BooleanField(default=False)


    def __str__(self):
        return self.student_name


class Register(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    Student = models.OneToOneField(Student, on_delete=models.CASCADE)
    department = models.CharField(max_length=50)


class Staff(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    staff_name = models.CharField(max_length=100)
    staff_department = models.TextField()
    staff_email = models.TextField()
    staff_phone = models.IntegerField()
    qualification = models.TextField()
    experiance = models.IntegerField()


    def __str__(self):
        return self.staff_name

