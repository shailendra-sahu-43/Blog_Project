from django.contrib import admin
from ecommerceapp.models import uuser , Contact
# Register your models here.
class memberAdmin(admin.ModelAdmin):
    list_display = ('title', 'date','description','img')

admin.site.register(uuser,memberAdmin)


class contactAdmin(admin.ModelAdmin):
    list_display = ('name','email','website','message')
admin.site.register(Contact,contactAdmin)
