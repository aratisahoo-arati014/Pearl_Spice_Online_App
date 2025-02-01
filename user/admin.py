from django.contrib import admin

from .models import *


# Register your models here.
#class contactusAdmin(Model.ModelAdmin):
    #list_display=('Name')
class contactusAdmin(admin.ModelAdmin):
    list_display = ('Name','Email','Mobile','Subject','Message')


admin.site.register(contactus,contactusAdmin)

class tbl_registerAdmin(admin.ModelAdmin):
    list_display = ('name','email','mobile','password','pincode','city','address','picture')

admin.site.register(tbl_register,tbl_registerAdmin)

class tbl_categoryAdmin(admin.ModelAdmin):
    list_display = ('id','product_category','category_picture')

admin.site.register(tbl_category,tbl_categoryAdmin)

class tbl_sliderAdmin(admin.ModelAdmin):
    list_display = ('id','slider_picture','title','description')

admin.site.register(tbl_slider,tbl_sliderAdmin)

class tbl_productAdmin(admin.ModelAdmin):
    list_display = ('id','product_name','category','price','discount_price','quantity','product_image')

admin.site.register(tbl_product,tbl_productAdmin)

class tbl_cartAdmin(admin.ModelAdmin):
    list_display = ('id','userid','product_id','product_image','product_price','quantity','total_price','product_name','added_date')

admin.site.register(tbl_cart,tbl_cartAdmin)

class tbl_orderAdmin(admin.ModelAdmin):
    list_display = ('id','userid','product_id','product_image','product_price','product_quantity','total_price','status','order_date')

admin.site.register(tbl_order,tbl_orderAdmin)

class tbl_booktableAdmin(admin.ModelAdmin):
    list_display = ('id','name','email','mobile','people','bookingtime','eventtype','bookingdate')
admin.site.register(tbl_booktable,tbl_booktableAdmin)