from django.contrib import admin
from .models import Student_Details
from django.contrib.auth.admin import UserAdmin
# Register your models here.

# class registerClass(UserAdmin):
#     list_display = ('student_admission_status','student_name')
#     search_fields = ('student_name',)
#     filter_horizontal=()
#     list_filter=()
#     fieldsets=()
admin.site.register(Student_Details),