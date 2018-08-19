from django.contrib import admin
from api_user.models import Student, Hobi, Major
# Register your models here.


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ( 'name', 'lname',)

@admin.register(Hobi)
class HobiAdmin(admin.ModelAdmin):
    list_display = ('hobi_name',)


@admin.register(Major)
class MajorAdmin(admin.ModelAdmin):
    list_display = ('name',)


    
