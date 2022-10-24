from django.contrib import admin
from .models import User
from .forms import UsuarioRegistrarForm, UsuarioAtualizarForm
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin


class UsuarioAdmin(BaseUserAdmin):
    form = UsuarioAtualizarForm
    add_form = UsuarioRegistrarForm

    list_display = ('id', 'email', 'username', 'nome', 'telefone', 'is_admin')
    list_filter = ('is_admin',)
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('username', 'nome', 'telefone',)}),
        ('Permissions', {'fields': ('is_admin',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'username', 'nome', 'telefone', 'password1', 'password2'),
        }),
    )
    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ()


admin.site.register(User, UsuarioAdmin)
