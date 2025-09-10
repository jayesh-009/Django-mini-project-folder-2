from django.contrib import admin
from myapp.models import Employee,Student,Movie,Login,Additem

# Register your models here.

class EmployeeAdmin(admin.ModelAdmin):
    list_display=['eno','ename','esal','eaddr']
    
admin.site.register(Employee)

class StudentAdmin(admin.ModelAdmin):
    list_display=['name','marks']

admin.site.register(Student,StudentAdmin)

class MovieAdmin(admin.ModelAdmin):

    list_display=['rdate','moviename','hero','heroine','rating']

admin.site.register(Movie,MovieAdmin)

class LoginAdmin(admin.ModelAdmin):

    list_display=['name','datetime']

class ItemaddAdmin(admin.ModelAdmin):
    list_display=['name','quantity']
