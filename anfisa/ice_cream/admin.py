from django.contrib import admin

from .models import IceCream
#admin.site.register(IceCream)

class IceAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    # Это свойство сработает для всех колонок: где пусто — там будет эта строка
    empty_value_display = '-пусто-'


admin.site.register(IceCream, IceAdmin)

# Register your models here.
