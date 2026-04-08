from django.contrib import admin
from .models import Inmuebles, Usuarios, Roles, Comisiones

# 1. Forzamos la desvinculación por si acaso
try:
    admin.site.unregister(Inmuebles)
except admin.sites.NotRegistered:
    pass

# 2. Registro ultra-simple (Sin clases extra) para probar
# Si esto funciona, el problema era la clase InmueblesAdmin
admin.site.register(Inmuebles) 

# Los demás
admin.site.register(Usuarios)
admin.site.register(Roles)
admin.site.register(Comisiones)