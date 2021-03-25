from django.contrib import admin
from .models import *
# Register your models here.


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
	list_display = ['name','id']


admin.site.register(Product)
admin.site.register(Order)
admin.site.register(Tag)