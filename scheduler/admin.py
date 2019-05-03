from django.contrib import admin
from .models import Student, Course, Instructor

class CourseInline(admin.TabularInline):
    model = Course
    extra = 3

class InstructorAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Instructor Name',          {'fields': ['i_name']}),
        ('Instructor ID',    {'fields': ['i_id']}),
    ]
    inlines = [CourseInline]
    list_display = ('i_name', 'i_id')
    search_fields = ['i_name']


admin.site.register(Student)
admin.site.register(Course)
admin.site.register(Instructor, InstructorAdmin)