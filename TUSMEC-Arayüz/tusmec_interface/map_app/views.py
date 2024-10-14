import serial
import time

from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Coordinate
from .serializer import CoordinateSerializer

@api_view(['POST'])
def save_coordinate(request):
    serializer = CoordinateSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=400)

from django.shortcuts import render

def index(request):
    return render(request, 'map_app/index.html')

def loraSender(request):
    pass
