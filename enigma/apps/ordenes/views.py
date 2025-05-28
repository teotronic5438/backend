from django.shortcuts import render

# Create your views here.
# apps/usuarios/views.py

from django.http import JsonResponse

def test_view(request):
    return JsonResponse({'mensaje': 'Vista de ordenes funcionando'})
