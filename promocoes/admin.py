from django.contrib import admin
from .models import Promocao, PromocaoAdmin

# Register your models here.

admin.site.register(Promocao, PromocaoAdmin)