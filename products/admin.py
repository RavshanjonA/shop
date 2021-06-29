from django.contrib import admin
from .models import Product, Offer
from django.contrib.auth.models import Group,User


admin.site.site_header = "Shop Admin"
admin.site.site_title = "Shop Admin Portal"
admin.site.index_title = "Welcome to Shop Researcher Portal"


class OfferAdmin(admin.ModelAdmin):
    list_display = ('code' , 'discount')


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name' , 'price', 'stock', 'image')

admin.site.unregister(Group)
admin.site.unregister(User)


admin.site.register(Offer,OfferAdmin)
admin.site.register(Product,ProductAdmin)
