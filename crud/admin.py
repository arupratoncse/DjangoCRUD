from django.contrib import admin
from .models import Student

# Register your models here.
class studentModel(admin.ModelAdmin):
    list_display = ["__str__"]
    search_fields = ["__str__","email"]
    class Meta:
        Model=Student
admin.site.register(Student,studentModel)
