from django.contrib import admin
from phonebook.models import PhoneBook

# Register your models here.

class PhoneBookView(admin.ModelAdmin):
    list_display=('id','name','tele','email','addr','birth')

admin.site.register(PhoneBook, PhoneBookView)