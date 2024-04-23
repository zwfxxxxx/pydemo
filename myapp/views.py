from django.shortcuts import render, HttpResponse
#
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
@csrf_exempt
def home(request):
    return HttpResponse("Hello, world. You're at the polls index.")


