from django.shortcuts import render
from django.http import JsonResponse


def secureView(request):
    return JsonResponse('Hey', safe=False)