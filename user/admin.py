from django.contrib import admin
from django.contrib.admin import register
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.admin import UserAdmin
from .models import BUser

class BUserCreateForm(UserCreationForm):
    class Meta:
        model = BUser
        fields = ('name', 'user_type', 'email', 'phone', 'state')


@register(BUser)
class BUserAdmin(UserAdmin):
    inlines = ()
    add_form = BUserCreateForm
    fieldsets = (
        (None, {'fields': ('password',)}),
        ('Personal Info',
         {'fields': ('name', 'email', 'phone', 'state', 'user_type')}
         ),
        ('Permissions',
         {'fields': ('is_active', 'is_superuser', 'is_staff', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login','last_updated','date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'name', 'state', 'user_type', 'phone', 'email', 'password1', 'password2',),
        }),
    )

    list_display = ('id', 'name', 'email', 'phone', 'last_updated')
    readonly_fields = ('date_joined', 'last_updated',)
    ordering = ('last_updated', 'id')

    list_filter = ('user_type', 'state')

    search_fields = ('name', 'email', 'phone')

    # readonly_fields = ('date_joined', 'last_updated',)

    ordering = ('email',)

    def get_inline_instances(self, request, obj=None):
        if not obj:
            return list()
        return super(BUserAdmin, self).get_inline_instances(request, obj)

