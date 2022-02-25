from django.shortcuts import render
from django.http import JsonResponse
from api.serializers import SecureSerializer, SoftwareSerializer

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView

from .models import Software, SecureHub
from .permissions import IsAdminOrReadOnly


def secureView(request):
    return JsonResponse('Hey', safe=False)


# class secureHubList(APIView):
#     permission_classes = [IsAdminOrReadOnly]

#     def get(self, request):
#         sHubs = SecureHub.objects.all()
#         serializer = SecureSerializer(sHubs, many=True)
#         return Response(serializer.data)


@api_view(['GET', 'POST'])
def secureHubList(request):
    if request.method == 'GET':
        sHubs = SecureHub.objects.all()
        serializer = SecureSerializer(sHubs, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = SecureSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


@api_view(['GET', 'POST'])
def softwareList(request):
    if request.method == 'GET':
        softwares = Software.objects.all()
        serializer = SoftwareSerializer(softwares, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = SoftwareSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
