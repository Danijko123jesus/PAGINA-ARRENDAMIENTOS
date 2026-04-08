from django.shortcuts import render
from .models import Inmuebles
from django.db.models import Q # Importamos Q para búsquedas complejas

def lista_inmuebles(request):
    # Obtenemos el término de búsqueda desde la URL (si existe)
    query = request.GET.get('q')
    
    if query:
        # Filtramos si el nombre O la ubicación contienen lo que escribió el usuario
        propiedades = Inmuebles.objects.filter(
            Q(titulo__icontains=query) | 
            Q(ubicacion_especifica__icontains=query)
        )
    else:
        # Si no hay búsqueda, mostramos todo
        propiedades = Inmuebles.objects.all()
        
    return render(request, 'propiedades/index.html', {'propiedades': propiedades})