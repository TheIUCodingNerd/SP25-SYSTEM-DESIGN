from django.contrib import admin
from .models import Student, Attendance, Grade

class StudentAdmin(admin.ModelAdmin):
    list_display = ('student_id', 'name', 'contact', 'email')

class AttendanceAdmin(admin.ModelAdmin):
    list_display = ('student', 'date', 'status')

class GradeAdmin(admin.ModelAdmin):
    list_display = ('student', 'subject', 'grade_section', 'score')

admin.site.register(Student, StudentAdmin)
admin.site.register(Attendance, AttendanceAdmin)
admin.site.register(Grade, GradeAdmin)
