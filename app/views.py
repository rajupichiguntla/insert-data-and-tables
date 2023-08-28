from django.shortcuts import render
from app.models import *
from django.http import HttpResponse
# Create your views here.
def insert_topic(request):
    tn=input('enter the name:')
    to=Topic.objects.get_or_create(topic_name='tn')[0]
    to.save()
    return HttpResponse('data is inserted')
def insert_webpage(request):
    tn=input('enter the topic_name:')
    to=Topic.objects.get_or_create(topic_name=tn)[0]
    to.save()
    n=input('enter tha name:')
    u=input('enter tha url:')
    wo=Webpage.objects.get_or_create(topic_name=to,name=n,url=u)[0]
    wo.save()
    return HttpResponse('data is inserted')
def insert_access(request):
    tn=input('enter the topic_name:')
    to=Topic.objects.get_or_create(topic_name=tn)[0]
    to.save()
    n=input('enter tha name:')
    u=input('enter tha url:')
    wo=Webpage.objects.get_or_create(topic_name=to,name=n,url=u)[0]
    wo.save()
    d=input('enter tha date:')
    a=input('enter tha author:')
    ac=AccessRecord.objects.get_or_create(name=wo,date=d,author=a)[0]
    ac.save()
    return HttpResponse('data is inserted')
def display_topic(request):
    QSTO=Topic.objects.all()
    d={'QSTO':QSTO}
    return render(request,'display_topic.html',d)

def display_webpage(request):
    WO=Webpage.objects.all()
    d={'WO':WO}
    return render(request,'display_webpage.html',d)
def display_access(request):
    AO=AccessRecord.objects.all()
    d={'AO':AO}
    return render(request,'display_access.html',d)
def in_topic(request):
    tn=input('enter the name:')
    to=Topic.objects.get_or_create(topic_name='tn')[0]
    to.save()
    QSTO=Topic.objects.all()
    d={'QSTO':QSTO}
    return render(request,'display_topic.html',d)
def in_webpage(request):
    tn=input('enter topic_name')
    na=input('enter name')
    ur=input('enter url')

    TO=Topic.objects.get(topic_name=tn)
    WO=Webpage.objects.get_or_create(topic_name=TO,name=na,url=ur)[0]
    WO.save()
    QSWO=Webpage.objects.all()
    d={'QSWO':QSWO}
    return render(request,'display_webpage.html',d)
def in_access(request):
    na=input('enter the name:')
    da=input('enter the date:')
    au=input('enter the name:')
    TO=Topic.objects.get(topic_name=tn)
    WO=Webpage.objects.get(name=na)
    AO=AccessRecord.objects.get(name=Wo,date=na,author=au)[0]
    AO.save()
    QSAO=AccessRecord.objects.all()
    d={'QSAO':QSAO}
    return render(request,'display_access.html',d)

