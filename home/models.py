from django.db import models
import email
from operator import mod
import uuid
from django.db import models
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
import pytz
from datetime import datetime
from django.utils import timezone
import pytz

# Create your models here.
class student(models.Model):
    name=models.CharField(max_length=100)
    des=models.TextField()
    def __str__(self) :
        return self.name
class Problem(models.Model):
    DIFFICULTY_CHOICES = (
        ('Easy', 'Easy'),
        ('Medium', 'Medium'),
        ('Hard', 'Hard'),
    )
    title = models.CharField(max_length=1000)
    description = models.TextField()
    difficulty = models.CharField(max_length=10, choices=DIFFICULTY_CHOICES)
    tags = models.ManyToManyField('Tag')
    categories = models.ManyToManyField('Category')

    def __str__(self):
        return self.title
class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

class TestCase(models.Model):
    # In your models add related_name arguments for foreign keys, so that you can retrieve the objects related to the House() instance.
    problem = models.ForeignKey(Problem, on_delete=models.CASCADE)
    input_data = models.TextField()
    expected_output = models.TextField()

    def __str__(self):
        return f'Test Case for {self.problem.title}'

class Solution(models.Model):
    problem = models.ForeignKey(Problem, on_delete=models.CASCADE)
    language = models.CharField(max_length=50)
    code = models.TextField()

    def __str__(self):
        return f'Solution for {self.problem.title} in {self.language}'
    
class codelearn(models.Model):
    title=models.TextField(max_length=100)
    description=models.TextField(max_length=1000)
    # def __str__(self) :
    #     return self.name
class discussitem(models.Model):
    title=models.TextField(max_length=100)
    description=models.TextField(max_length=1000)
    timestamp = models.DateTimeField(auto_now_add=True)


class exploreitem(models.Model):
    title=models.TextField(max_length=100)
    description=models.TextField(max_length=1000)
    reaction=models.TextField(max_length=100)

class User_detail(models.Model):
    user_detail_name=models.CharField(max_length=100)
    user_detail_email=models.CharField(max_length=100)
    user_detail_password=models.CharField(max_length=100)

class Cadmin(models.Model):
    Cname=models.CharField(max_length=100)
    Cdate=models.DateTimeField(auto_now_add=True)
    Cauthor=models.CharField(max_length=100)

class Newcontest(models.Model):
    nname=models.CharField(max_length=100)
    ndate=models.DateTimeField()
    nauthor=models.CharField(max_length=100)
    def __str__(self):
        return self.nname
    


class Cproblem(models.Model):
    DIFFICULTY_CHOICES = (
        ('Easy', 'Easy'),
        ('Medium', 'Medium'),
        ('Hard', 'Hard'),
    )
    newcontest=models.ForeignKey(Newcontest,on_delete=models.CASCADE)
    title = models.CharField(max_length=1000)
    description = models.TextField()
    difficulty = models.CharField(max_length=10, choices=DIFFICULTY_CHOICES)
    tags = models.TextField(default='Math')
    categories = models.TextField(default='Easy')
    compexity=models.TextField(max_length=100)
    constraints=models.TextField(max_length=100)
    pdate=models.DateTimeField(null=True,blank=True)
    def __str__(self):
        return f'Problem for {self.title}'
    def save(self, *args, **kwargs):
        if not self.pdate:  # If no date is provided, set it to the current date
            from datetime import date
            self.pdate = date.today()
        super(Cproblem, self).save(*args, **kwargs)
class CtestCase(models.Model):
    # In your models add related_name arguments for foreign keys, so that you can retrieve the objects related to the House() instance.
    newcontest=models.ForeignKey(Newcontest,on_delete=models.CASCADE)
    input_data = models.TextField()
    expected_output = models.TextField()
    def __str__(self):
        return f'Testcase for {self.newcontest.nname}'
    # def __str__(self):
    #     return f'Test Case for {self.problem.title}'

class Csolution(models.Model):
    newcontest=models.ForeignKey(Newcontest,on_delete=models.CASCADE)
    language = models.CharField(max_length=50)
    code = models.TextField()
    def __str__(self):
        return f'Solution for {self.newcontest.nname} in {self.language}'
    
class Cupdatesolution(models.Model):
    cproblem=models.ForeignKey(Cproblem,on_delete=models.CASCADE)
    language = models.CharField(max_length=50)
    code = models.TextField()
    def __str__(self):
        return f'Solution for {self.cproblem.title} in {self.language}'
    
class Cupdatetestcase(models.Model):
    cproblem=models.ForeignKey(Cproblem,on_delete=models.CASCADE)
    input_data = models.TextField()
    expected_output = models.TextField()
    def __str__(self):
        return f'Testcase for {self.cproblem.title}'




class Cdate(models.Model):
    newcontest=models.ForeignKey(Newcontest,on_delete=models.CASCADE)
    cdate=models.CharField(max_length=50)

class SubmitestCase(models.Model):
    # In your models add related_name arguments for foreign keys, so that you can retrieve the objects related to the House() instance.
    cproblem = models.ForeignKey(Cproblem, on_delete=models.CASCADE)
    submitinput_data = models.TextField()
    submitexpected_output = models.TextField()

    def __str__(self):
        return f'Test Case for {self.cproblem.title}'

class IndianDateTimeField(models.DateTimeField):
    def pre_save(self, model_instance, add):
        value = timezone.now().astimezone(pytz.timezone('Asia/Kolkata'))
        setattr(model_instance, self.attname, value)
        return value
class Myubmission(models.Model):
    user_detail = models.ForeignKey(User_detail, on_delete=models.CASCADE)
    cproblem = models.ForeignKey(Cproblem, on_delete=models.CASCADE)
    code = models.TextField()
    output=models.TextField(default="shubham")
    language = models.CharField(max_length=50)
    timetaken=models.CharField(max_length=50)
    memorytaken=models.CharField(max_length=50)
    verdict=models.CharField(max_length=100)
    timestamp = IndianDateTimeField(default=timezone.now)

    # Other fields

    def __str__(self):
        return f"Submission by {self.user_detail.user_detail_name} for Problem: {self.cproblem.title}"


# def usercontestsub(models.Model):
class Usercontestsub(models.Model):
    user_detail = models.ForeignKey(User_detail, on_delete=models.CASCADE)
    cproblem = models.ForeignKey(Cproblem, on_delete=models.CASCADE)
    newcontest=models.ForeignKey(Newcontest,on_delete=models.CASCADE)
    code = models.TextField()
    output=models.TextField(default="shubham")
    language = models.CharField(max_length=50)
    timetaken=models.CharField(max_length=50)
    memorytaken=models.CharField(max_length=50)
    verdict=models.CharField(max_length=100)
    timestamp = IndianDateTimeField(default=timezone.now)



        











    

