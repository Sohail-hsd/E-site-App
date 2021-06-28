from django.contrib import admin

from .models import Product,mainImage,Contact,Order,updateOrder

# Register your models here.
class conf_contact(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone')

class conf_prod(admin.ModelAdmin):
    list_display = ('product_name','image','category','pub_date')

class conf_order(admin. ModelAdmin):
    list_display = ('name','order_id','email','phone')

class conf_update_order(admin.ModelAdmin):
    list_display = ('update_id','order_id','update_desc')

admin.site.register(Product,conf_prod)
admin.site.register(mainImage)
admin.site.register(Contact,conf_contact)
admin.site.register(Order,conf_order)
admin.site.register(updateOrder,conf_update_order)

