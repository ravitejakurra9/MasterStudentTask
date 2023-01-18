from django.contrib import admin

from MasterStudentApp.models import Student, Master, Task

# Register your models here.

admin.site.register(Student)
admin.site.register(Master)
admin.site.register(Task)