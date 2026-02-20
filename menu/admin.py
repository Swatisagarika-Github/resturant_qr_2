from django.contrib import admin
from .models import MenuItem, Order


# ---------- Menu Items Admin ----------
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'price']   # columns shown in admin list
    search_fields = ['name']                 # search by item name
    ordering = ['id']                        # order by id


# ---------- Orders Admin ----------
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'table_no', 'timestamp', 'status']
    list_filter = ['status', 'timestamp']    # filter sidebar
    search_fields = ['table_no']
    filter_horizontal = ['items']            # nice selection UI for ManyToMany


# Register models
admin.site.register(MenuItem, MenuItemAdmin)
admin.site.register(Order, OrderAdmin)