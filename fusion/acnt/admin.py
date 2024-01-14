from django.contrib import admin
from .models import User, Client, Freelancer,JobNames,Location

# Register your models here.

admin.site.register(User)
admin.site.register(Client)
admin.site.register(Freelancer)
admin.site.register(JobNames)
admin.site.register(Location)
