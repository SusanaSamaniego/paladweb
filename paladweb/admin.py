

# Register your models here.
from django.contrib import admin
from .models import cita
from django.contrib import messages
# Register your models here.
admin.site.site_header="Paladweb"
#para el titulo
admin.site.index_title="¿Cómo vender en la web con una página?"
#titulo del sitio
admin.site.site_title="Creación de páginas webs: Desarrollo "





admin.site.register(cita)
class citaAdmin(admin.ModelAdmin):
    list_display = ('hora')