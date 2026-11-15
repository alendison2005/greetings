from django.shortcuts import render

# Create your views here.
from django.views.generic import View
from django.http import path
from django.http import JsonResponse

class HelloWoldView(View):
  def get(self,request):
     response_data = {"message":"helloworld"}
     return JsonResponse(response_data)
  
class GoodMorningView(View):
   def get(self,request):
      response_data = {"message":"goodmorning"}
      return JsonResponse(response_data)

