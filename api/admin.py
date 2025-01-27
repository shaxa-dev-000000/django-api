from django.contrib import admin
from .models import Passport

# Register your models here.
@admin.register(Passport)
class PassportAdmin(admin.ModelAdmin):
    list_display = ("name", "surname", "passport_id")