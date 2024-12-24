import serial
import json

from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view

# Arduino bağlantısını başlatıyoruz (port numarasını kendi sisteminize göre ayarlayın)
arduino = serial.Serial('/dev/ttyACM3', 9600, timeout=1)

@api_view(['POST'])
def save_coordinate(request):
    try:
        # İstekten gelen veriler
        data_type = request.data.get('dataType', 'default')
        selected_task = request.data.get('selectedTask', 'default')
        selected_mode = request.data.get('selectedMode', 'default')

        print(f"Veri Tipi: {data_type}")
        print(f"Seçilen Görev: {selected_task}")
        print(f"Seçilen Mod: {selected_mode}")

        if data_type == "coordinate":
            coordinates = json.loads(request.data.get('coordinates', '[]'))
            # Koordinatları LoRa üzerinden göndermek için formatlıyoruz
            coordinate_messages = []
            for coordinate in coordinates:
                latitude = coordinate['latitude']
                longitude = coordinate['longitude']
                coordinate_messages.append(f"{latitude},{longitude}")
                print(f"Gelen veri: {latitude},{longitude}")
            # Tüm koordinatları tek bir mesajda virgülle ayırarak birleştiriyoruz
            message = ",".join(coordinate_messages) + "\n"
            print(f"Tüm koordinatlar: {message}")
            # Tüm koordinatları Arduino'ya bir kerede gönderiyoruz
            arduino.write(message.encode())
            print("Koordinatlar gönderildi")

        elif data_type == "task":
            arduino.write(selected_task.encode())
            print("Görev bilgisi gönderildi")

        elif data_type == "mode":
            arduino.write(selected_mode.encode())
            print("Mod bilgisi gönderildi")

        # Arduino'dan gelen veriyi okuyoruz
        incoming_data = arduino.readline().decode().strip()
        print(f"Arduino'dan gelen veri: {incoming_data}")

        # Başarılı yanıt döndür
        return Response({
            "status": "success",
            "message": "Veriler işlendi ve Arduino'ya gönderildi",
            "incoming_data": incoming_data
        }, status=200)

    except Exception as e:
        # Hata durumunda yanıt döndür
        print(f"Hata: {str(e)}")
        return Response({
            "status": "error",
            "message": f"Hata oluştu: {str(e)}"
        }, status=500)

def index(request):
    return render(request, 'map_app/index.html')

def loraSender(request):
    pass
