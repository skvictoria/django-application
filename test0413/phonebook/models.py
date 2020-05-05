from django.db import models

# Create your models here.
class PhoneBook(models.Model):
    name = models.CharField(max_length=50, null=False) #데이터가 무조건 들어와야 한다!
    tele = models.CharField(max_length=20)
    email = models.EmailField() #@형식
    addr = models.CharField(max_length=100)
    birth = models.DateField()
    writer = models.CharField(max_length = 200, null=False)
    #################################
    ###model에 'writer' 추가하기#########
    #1. 가상환경 에서
    #2. manage.py makemigrations phonebook
    #3. select option -> 1
    #4. default value -> 'admin'
    #5. manage.py migrate phonebook
    #6. manage.py runserver
    ####################################