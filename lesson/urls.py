from django.urls import path
from . import views

app_name = 'lesson'
urlpatterns = [
    path('', views.all_materials, name='all_materials'),
    path('<int:year>/<int:month>/<int:day>/<slug:slug>',
         views.material_details,
         name='material_details'),
]