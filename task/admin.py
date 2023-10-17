from django.contrib import admin

from task.models import Menu


# Register your models here.
class MenuInline(admin.TabularInline):
    model = Menu
    fields = ('name', 'slug',)
    prepopulated_fields = {'slug': ('name',)}
    extra = 3


@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = ('name', 'parent', 'slug',)
    prepopulated_fields = {'slug': ('name',)}
    inlines = (MenuInline,)
