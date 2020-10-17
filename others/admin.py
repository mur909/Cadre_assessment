from django.contrib import admin
from others import models

# Register your models here.
class PermissionAdmin(admin.ModelAdmin):
    list_display = ['title', 'url']  # 可显示的
    list_editable = ['url']  # 可编辑的


class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'roles', 'department']
    list_editable = ['department', 'roles']

    # def name(self, obj):
    #     return obj.roles.values_list('name', flat=True)[0]
    # name.short_description = '管理员等级'


admin.site.register(models.Permission, PermissionAdmin)
admin.site.register(models.Role)
admin.site.register(models.User, UserAdmin)