from django.contrib import admin

# Register your models here.
from TestApp.models import Student,Degree

admin.site.register(Student)
admin.site.register(Degree)
