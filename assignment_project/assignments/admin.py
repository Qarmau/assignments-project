from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Assignment

#admin.site.register(Assignment)

@admin.register(Assignment)
class AssignmentAdmin(admin.ModelAdmin):
    list_display = ('title', 'grade','subject','uploaded_at')
    search_fields = ('title', 'subject')