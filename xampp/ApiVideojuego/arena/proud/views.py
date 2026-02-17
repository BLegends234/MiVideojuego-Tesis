from django.shortcuts import render
from django.http import JsonResponse
from proud.models import usuarios, score
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from proud.serializers import UsuariosSerializers, ScoreSerializers
# Create your views here.
def ObetenerJsonUsuarios(request):
    user = usuarios.objects.all()
    dato = {'user':list(user.values('id','NombreUsuario','Correo','Password'))}
    return JsonResponse(dato)

def ObetenerJsonScore(request):
    punto = usuarios.objects.all()
    dato = {'punto':list(punto.values('id','Puntos','Usuario'))}
    return JsonResponse(dato)

@api_view(['GET','POST'])
def ListaUsuario(request):
    if request.method == 'GET':
        user = usuarios.objects.all()
        userSerial = UsuariosSerializers(user,many=True)
        return Response(userSerial.data)
    if request.method == 'POST':
        userSerial = UsuariosSerializers(data=request.data)
        if userSerial.is_valid():
            userSerial.save()
            return Response(userSerial.data, status=status.HTTP_201_CREATED)
        else:
            return Response(userSerial.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','POST'])       
def ListaScore(request):
    if request.method == 'GET':
        punto = score.objects.all()
        scoreSerial = ScoreSerializers(punto,many=True)
        return Response(scoreSerial.data)
    if request.method == 'POST':
        scoreSerial = ScoreSerializers(data=request.data)
        if scoreSerial.is_valid():
            scoreSerial.save()
            return Response(scoreSerial.data, status=status.HTTP_201_CREATED)
        else:
            return Response(scoreSerial.errors, status=status.HTTP_400_BAD_REQUEST)
        
@api_view(['GET','DELETE','PUT'])
def detallesUsuario(request,id):
    try:
        user = usuarios.objects.get(id=id)
    except:
        return Response(status=status.HTTP_400_BAD_REQUEST)
    if request.method == 'GET':
        userSerial = UsuariosSerializers(user)
        return Response(userSerial.data)
    if request.method == 'PUT':
        userSerial = UsuariosSerializers(user,data=request.data)
        if userSerial.is_valid():
            userSerial.save()
            return Response(userSerial.data,status=status.HTTP_201_CREATED)
        else:
            return Response(userSerial.errors, status=status.HTTP_400_BAD_REQUEST)
    if request.method == 'DELETE':
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
@api_view(['GET','DELETE','PUT'])
def detallesScore(request,id):
    try:
        punto = score.objects.get(id=id)
    except:
        return Response(status=status.HTTP_400_BAD_REQUEST)
    if request.method == 'GET':
        puntoSerial = ScoreSerializers(score)
        return Response(puntoSerial.data)
    if request.method == 'PUT':
        puntoSerial = ScoreSerializers(punto,data=request.data)
        if puntoSerial.is_valid():
            puntoSerial.save()
            return Response(puntoSerial.data,status=status.HTTP_201_CREATED)
        else:
            return Response(puntoSerial.errors, status=status.HTTP_400_BAD_REQUEST)
    if request.method == 'DELETE':
        punto.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
