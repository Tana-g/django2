from django.shortcuts import render
from django.http import HttpResponse
import datetime
# Create your views here.
def time_info(request):
    time=datetime.datetime.now()
    msg='<h2>namaskaraa good evening...</h2>'
    msg=msg+'<h2>now server time is:'+str(time)+'</h2>'
    return HttpResponse(msg)
