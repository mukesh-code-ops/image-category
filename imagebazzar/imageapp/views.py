from django.shortcuts import render,HttpResponse
# from models import *
from imageapp.models import *
# Create your views here.
def index(request):
    cats=category.objects.all()
    images=image.objects.all()
    data={'images':images ,'cats':cats}
    return render(request,'home.html',data)
def categoryy(request,cid):
    
    cats=category.objects.all()
    categor=category.objects.get(pk=cid)
    images=image.objects.filter(title=categor)

    
    data={'images':images ,'cats':cats}
    return render(request,'home.html',data)
def aboutus (request):
    return HttpResponse("this is aboutus")
