from django.shortcuts import render
from django.http import HttpResponse
# from enroll1.models import * 
# from rest_framework.views import APIView
# from django.http import JsonResponse

# Create your views here.
 
def home1(request):
    return render(request,'enroll/main.html')



# Create your views here.
