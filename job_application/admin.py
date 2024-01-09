from django.contrib import admin
from .models import Form, ContactForm


class FormAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "email")
    search_fields = ("first_name", "last_name", "email")
    list_filter = ("date", "occupation")
    ordering = ("-first_name",)
    readonly_fields = ("occupation",)


class ContactFormAdmin(admin.ModelAdmin):
    list_display = ("name", "subject", "email")
    search_fields = ("name", "subject", "email")
    list_filter = ("subject",)
    readonly_fields = ("message",)


admin.site.register(Form, FormAdmin)
admin.site.register(ContactForm, ContactFormAdmin)
