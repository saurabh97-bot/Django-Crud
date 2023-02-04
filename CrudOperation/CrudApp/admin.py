from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Employee)
admin.site.register(Student)

# =============================================================================

@admin.register(TestModel)
class TestAdmin(admin.ModelAdmin):
    list_display = ['name','text','phone','active','created_on']