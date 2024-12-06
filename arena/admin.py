from django.contrib import admin
from .models import (
    Field,
    Schedule,
)

# Register your models here.
@admin.register(Field)
class FieldAdmin(admin.ModelAdmin):
    pass