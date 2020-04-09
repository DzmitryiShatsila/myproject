from django.shortcuts import render
from . import models
# Create your views here.

def all_materials(request):
    material_list = models.Material.objects.all()
    return render(request,
                  'materials/all_materials.html',
                  {'materials': material_list})