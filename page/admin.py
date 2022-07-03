from django.contrib import admin
from .models import Todo
@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
     list_display=['Added_date','item','due']

# Register your models here.
