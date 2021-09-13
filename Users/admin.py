from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from import_export import resources, fields
from django.contrib.auth.hashers import make_password
from django.contrib.auth import get_user_model

User = get_user_model()


from django.contrib.auth.admin import UserAdmin

class UserResource(resources.ModelResource):
   
    def before_import_row(self,row, **kwargs):
           value = row['password']
           row['password'] = make_password(value)
    class Meta:
        model = User
        import_id_fields = ('identificacion',)

        fields = ('identificacion', 'username', 'password', 'nombres', 'apellidos', 'carrera', 'ciclo', 'paralelo')

class UserAdmin(ImportExportModelAdmin, UserAdmin):
    add_fieldsets = (
        (None, {
            'fields': ('identificacion', 'username', 'password1', 'password2'),
        }),
    )
    list_display = ('identificacion', 'username', 'password', 'nombres', 'apellidos', 'carrera', 'ciclo', 'paralelo')
    # list_filter = ('created_at',)
    resource_class = UserResource
    pass



#admin.site.unregister(User)
admin.site.register(User, UserAdmin)
