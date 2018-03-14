from django.contrib import admin
from .models import Category, Product, Model

class ModelsAdmin(admin.ModelAdmin): 
    list_display = ('model','desc','size','active','price')
    list_filter = ('product',)
    search_fields = ('model', 'size')
    
class ProductAdmin(admin.ModelAdmin): 
    list_display = ('name','displayOrder')
    list_filter = ('category',)

admin.site.register(Category)
admin.site.register(Product, ProductAdmin)
admin.site.register(Model, ModelsAdmin)

