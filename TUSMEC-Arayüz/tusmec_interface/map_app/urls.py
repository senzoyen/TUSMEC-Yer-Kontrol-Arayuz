from django.urls import path
from .views import save_coordinate,index

urlpatterns = [
    path('', index, name='index'),
    path('save-coordinate/', save_coordinate, name='save-coordinate'),
]
