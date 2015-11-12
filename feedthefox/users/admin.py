from django.contrib import admin
from django.contrib.auth import get_user_model


User = get_user_model()


class UserAdmin(admin.ModelAdmin):
    list_display = ('mozillian_username', 'email', 'first_name', 'last_name', 'country',)
    search_fields = ('mozillian_username', 'email', 'first_name', 'last_name', 'country',)

    class Meta:
        model = User


admin.site.register(User, UserAdmin)
