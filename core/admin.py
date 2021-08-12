from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Profile)
admin.site.register(Address)
admin.site.register(Product)
admin.site.register(orderItem)
admin.site.register(Order)
admin.site.register(shopperReview)
admin.site.register(productReview)
admin.site.register(orderHistory)
