from django.shortcuts import render,HttpResponse
import time,requests
from rest_framework.response import Response
from rest_framework.views import APIView
# Create your views here.
def home(request):
    return HttpResponse('<h1>Home Page</h1>')
class PingView(APIView):
    def get(self,request):
        return Response({'status':'OK'})

class ScheduleView(APIView):
    def get(self,request):
        url=request.query_params['url']
        url_datetime=request.query_params['time']
        if(time.strftime('%d-%m-%Y %H:%M')==url_datetime):
            response=requests.get(url,verify=False)
            return Response({'status_code':response.status_code})
        return Response({'respone':"The current time doesnt match"})