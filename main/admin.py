from django.contrib import admin
from .models import Property, RentHistory, SalesHistory

admin.site.register(Property)
admin.site.register(RentHistory)
admin.site.register(SalesHistory)
