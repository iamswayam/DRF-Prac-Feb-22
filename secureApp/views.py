from ast import Raise
from django.shortcuts import render
from django.http import JsonResponse
from api.serializers import SecureSerializer, SoftwareSerializer

from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.parsers import JSONParser


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
@permission_classes([IsAuthenticated])
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


# @api_view(['GET', 'PUT', 'DELETE'])
# @permission_classes([IsAuthenticated])
# def secureHub1(request, pk):

#     if request.method == 'GET':
#         try:
#             sHub1 = SecureHub.objects.get(pk=pk)
#         except SecureHub.DoesNotExist:
#             return Response({'error': 'Research not found!'}, status=status.HTTP_404_NOT_FOUND)

#         serializer = SecureSerializer(sHub1)
#         return Response(serializer.data)

#     elif request.method == 'PUT':
#         # sHub1 = SecureHub.objects.get(pk=pk)
#         sHub1 = JSONParser().parse(request)
#         serializer = SecureSerializer(sHub1, data=sHub1)

#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    # elif request.method == 'DELETE':
    #     sHub1 = SecureHub.objects.get(pk=pk)
    #     sHub1.delete()
    #     return Response(status=status.HTTP_204_NO_CONTENT)

class secureHub1(generics.RetrieveUpdateDestroyAPIView):
    queryset = SecureHub.objects.all()
    serializer_class = SecureSerializer
    permission_classes = [IsAuthenticated]


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
