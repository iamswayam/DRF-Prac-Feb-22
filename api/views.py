from django.shortcuts import render
from django.http import JsonResponse


def apiView(request):
    return JsonResponse('Hello')
