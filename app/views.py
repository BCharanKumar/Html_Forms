from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from app.models import *


def insert_topic(request):
    if request.method=='POST':
        tn=request.POST['tn']
        TO=Topic.objects.create(topic_name=tn)
        return HttpResponse('Your Object Created Successfully..!')
    return render(request,'insert_topic.html')

def insert_webpage(request):
    LTO=Topic.objects.all()
    d={'LTO':LTO}
    if request.method=='POST':
        try:
            tn=request.POST['tn']
            na=request.POST['na']
            ur=request.POST['ur']
            em=request.POST['em']

            TO=Topic.objects.get(topic_name=tn)
            if em:

                WO=WebPage.objects.get_or_create(topic_name=TO,name=na,url=ur,email=em)
            else:
                WO=WebPage.objects.get_or_create(topic_name=TO,name=na,url=ur)

            return HttpResponse('Your Object Created Successfully ...!')
        except Exception as e:
            return HttpResponse(f'error is {e}')

    return render(request,'insert_webpage.html',d)

def insert_access(request):
    LWO=WebPage.objects.all()
    d={'LWO':LWO}
  

    if request.method=='POST':
        try:
            na=request.POST['na']
            au=request.POST['au'] 
            da=request.POST['da']   

            WO=WebPage.objects.get(id=na)
            AO=AccessRecord.objects.get_or_create(name=WO,author=au,date=da)
            return HttpResponse('Guys Your Object Created Successfully ...!')
        except Exception as e:
            return HttpResponse(e)
        

    return render(request,'insert_access.html',d)

def select_multiple(request):
    LTO=Topic.objects.all()
    d={'LTO':LTO}
    if request.method=='POST':
        MTN=request.POST.getlist('tn')
        print(MTN)
        EQST=WebPage.objects.none()
        for topic in MTN:
            EQST=EQST|WebPage.objects.filter(topic_name=topic)
        d1={'EQST':EQST}
        return render(request,'display_webpage.html',d1)


    return render(request,'select_multiple.html',d)





def checkbox(request):
    LTO=Topic.objects.all()
    d={'LTO':LTO}

    
    return render(request,'checkbox.html',d)


def radio_buttons(request):
    LTO=Topic.objects.all()
    d={'LTO':LTO}


    return render(request,'radio_buttons.html',d)