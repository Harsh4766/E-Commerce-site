from django.contrib import admin
from . models import product,contact,order,updateorder
# Register your models here.
admin.site.register(product)
admin.site.register(contact)
admin.site.register(order)
admin.site.register(updateorder)