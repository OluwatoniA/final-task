from django.contrib import admin
from .forms import RecordCreateForm

# Register your models here.

from .models import Record

class RecordCreateAdmin(admin.ModelAdmin):
    list_display = ['room_number', 'occupant_name', 'number_of_night']
    form = RecordCreateForm
    list_filter = ['room_number']
    search_fields = ['room_number', 'occupant_name']


admin.site.register(Record, RecordCreateAdmin)
