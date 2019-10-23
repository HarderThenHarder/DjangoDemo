from django.contrib import admin

# Register your models here.
from vote.models import Teacher, Subject

class SubjectAdmin(admin.ModelAdmin):
    list_display = ('no', 'name', 'intro', 'create_date', 'is_hot')
    ordering = ('no', )

class TeacherAdmin(admin.ModelAdmin):
    list_display = ('no', 'name', 'detail', 'photo', 'subject')
    ordering = ('subject', 'no')

admin.site.register(Teacher, TeacherAdmin)
admin.site.register(Subject, SubjectAdmin)