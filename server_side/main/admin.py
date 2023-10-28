from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.user_data)
admin.site.register(models.message)
admin.site.register(models.post)
admin.site.register(models.team)