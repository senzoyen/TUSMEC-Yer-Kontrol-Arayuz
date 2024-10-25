from django.urls import path
from .views import save_coordinate, index  # views'tan import ettik

urlpatterns = [
    path('', index, name='index'),
    path('save_coordinate/', save_coordinate, name='save_coordinate'),  # 'views.' kullanmanıza gerek yok
]
