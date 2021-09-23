from django.contrib.auth.admin import UserAdmin
from .views.utils.validar_cedula import verificar_cedula
from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from import_export import resources
from django.contrib.auth.hashers import make_password
from django.contrib.auth import get_user_model
from django.forms import ValidationError
from django.utils.translation import gettext as _
User = get_user_model()


class UserResource(resources.ModelResource):

    def before_import_row(self, row, **kwargs):
        try:
            if not verificar_cedula(row['identificacion']):
                raise ValidationError(_('Cedula ecuatoriana no valida'))

        except ValidationError as v:
            raise Exception(_(str(v)))
        value = row['password']
        row['password'] = make_password(value)

    class Meta:
        model = User
        import_id_fields = ('identificacion',)

        fields = ('identificacion', 'username', 'password', 'nombres',
                  'apellidos', 'carrera', 'ciclo', 'paralelo')


class UserAdmin(ImportExportModelAdmin, UserAdmin):
    add_fieldsets = (
        (None, {
            'fields': ('identificacion', 'username', 'password1', 'password2'),
        }),
    )
    list_display = ('identificacion', 'username', 'password',
                    'nombres', 'apellidos', 'carrera', 'ciclo', 'paralelo')
    # list_filter = ('created_at',)
    resource_class = UserResource
    pass


# admin.site.unregister(User)
admin.site.register(User, UserAdmin)
