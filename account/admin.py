from django.contrib import admin
from .models import User, About, Contact


class UserAdmin(admin.ModelAdmin):
    list_display=('id', 'username', 'full_name', 'last_login', 'is_staff')
    list_display_links=('id', 'username')


admin.site.register(User, UserAdmin)



class AboutAdmin(admin.ModelAdmin):
    list_display=('id', 'my_about',)
    list_display_links=('id', 'my_about',)
    readonly_fields=('id',)

admin.site.register(About, AboutAdmin)



class ContactAdmin(admin.ModelAdmin):
    list_display=('id', 'name', 'email', 'created_at',)
    list_display_links=('id', 'name', 'email',)
    readonly_fields=('id',)

admin.site.register(Contact, ContactAdmin)