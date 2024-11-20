import serial
import time
import json

from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Coordinate
from .serializer import CoordinateSerializer

# Arduino bağlantısını başlatıyoruz (port numarasını kendi sisteminize göre ayarlayın)
#arduino = serial.Serial('COM7', 9600, timeout=1)

@api_view(['POST'])
def save_coordinate(request):
    # İstekten gelen JSON formatındaki koordinatları alıyoruz
    coordinates = json.loads(request.POST.get('coordinates', '[]'))
    
    # Koordinatları LoRa üzerinden göndermek için formatlıyoruz ve gönderiyoruz
    for coord in coordinates:
        print(f"Latitude: {coord['latitude']}, Longitude: {coord['longitude']}")
        
        # Koordinatları Arduino’ya göndermek için CSV formatına çeviriyoruz
    #    message = f"{coord['latitude']},{coord['longitude']}\n"
 #       arduino.write(message.encode())  # Veriyi Arduino'ya gönderiyoruz
        time.sleep(1)  # Arduino'nun veriyi işleyebilmesi için bekliyoruz
    
    # Koordinatları veritabanına kaydetmek için serializer'ı kullanıyoruz
    serializer = CoordinateSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    
    # Eğer veriler geçerli değilse, hata mesajını döndürüyoruz
    return Response(serializer.errors, status=400)

def index(request):
    return render(request, 'map_app/index.html')

def loraSender(request):
    pass
