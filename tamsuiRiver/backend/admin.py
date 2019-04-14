from django.contrib import admin

# Register your models here.
from backend.models import Request, Company, Farmer

admin.site.register(Request)
admin.site.register(Company)
admin.site.register(Farmer)