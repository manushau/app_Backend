from django.contrib import admin
from .models import Users
from .models import warehouse
from .models import acc_details
from .models import messages

# Registers the Users model with the Django admin interface
admin.site.register(Users)
admin.site.register(warehouse)
admin.site.register(acc_details)
admin.site.register(messages)
# @admin.register(warehouse)
# class warehouseadmin(admin.ModelAdmin):
#     pass 