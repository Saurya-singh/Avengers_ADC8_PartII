from django.http import HttpResponse
from django.shortcuts import render,redirect
from .models import Event
from django.http import HttpResponse
from django.contrib.auth import authenticate
from django.contrib.auth.models import User

# Create your views here.
def view_event_data(request):
    events_list=Event.objects.all()
    con_var={
        'events':events_list
    }
    return render(request,'event/viewevent.html',con_var)

def view_event_form(request):
    return render(request,'event/save_event.html')
    
def view_event_save(request):
    if request.method == "POST":
        get_name=request.POST['event_name']
        get_venue=request.POST['event_venue']
        get_date=request.POST['event_date']
        get_manager=request.POST['event_manager']
        Event.objects.create(event_name=get_name,venue=get_venue,event_date=get_date,manager=get_manager)
        return HttpResponse("Added Sucessfully")    
    else:
        return HttpResponse("Error while adding") 

def view_event_delete(request,ID):
    print(ID)
    event_obj=Event.objects.get(id=ID)
    con_var={
        'event':event_obj
    }
    event_obj.delete()
    return render(request,'event/delete_data.html',con_var)
    
def get_isauthenticated_welcome(request):
    if request.user.is_authenticated:
        return render(request,"event/viewevent.html")
    else:
        return HttpResponse('Please login first')
