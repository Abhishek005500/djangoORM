from django.contrib import admin
from .models import Album,Song,Course,Semester,Subject
# Register your models here.

admin.site.register(Album)
admin.site.register(Song)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ["name"]


admin.site.register(Course)

admin.site.register(Semester)
admin.site.register(Subject, SubjectAdmin)





