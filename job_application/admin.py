from django.contrib import admin
from .models import Form


class FormAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "email")
    search_fields = ("first_name", "last_name", "email")
    list_filter = ("date", "occupation")
    readonly_fields = ("occupation",)


admin.site.register(Form, FormAdmin)

# Register your models here.
