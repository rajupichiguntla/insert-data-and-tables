from django.shortcuts import render
from app.models import *
from django.db.models.functions import Length
from django.db.models import Q

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
    #WO=Webpage.objects.filter(topic_name__startswith='c')
    #WO=Webpage.objects.filter(name__startswith='r')
    #WO=Webpage.objects.filter(url__startswith='h')
    #WO=Webpage.objects.exclude(name__startswith='r')
    #WO=Webpage.objects.exclude(name__endswith='a')
    #Webpage.objects.filter(topic_name='kabaddi').update(name='Ronaldo')
    #Webpage.objects.filter(name='rakesh').update(name='Rana')
    #Webpage.objects.filter(name='ram').update(url='https://ram.in')
    #Webpage.objects.filter(name='raki').update(name='Rana') #no operation
    #Webpage.objects.update_or_create(topic_name='cricket',defaults={'name':'balaji'})# it will error because two row is satifily it will not  allow update_or_create MultipleObjectsReturned at /display_webpage/get() returned more than one Webpage -- it returned 2!
    #Webpage.objects.update_or_create(topic_name='runing',defaults={'name':'balaji'})it will updated because only row is satifily
    #cto=Topic.objects.get_or_create(topic_name='cricket')
    #Webpage.objects.update_or_create(topic_name=cto,defaults={'name':'balu',url:'http//bala.in'})
    Webpage.object.delete(name=raju)
    
    
    
    
    d={'WO':WO}
    return render(request,'display_webpage.html',d)
def display_access(request):
    AO=AccessRecord.objects.all()
    #AO=AccessRecord.objects(filter(date__year__gr='2020'))
    #AO=AccessRecord.objects(filter(author__startswith='v'))
    #AO=AccessRecord.objects(filter(name__startswith='v'))

    d={'AO':AO}
    return render(request,'display_access.html',d)
'''def in_topic(request):
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
    return render(request,'display_access.html',d)'''





