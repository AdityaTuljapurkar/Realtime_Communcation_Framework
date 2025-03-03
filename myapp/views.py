from django.shortcuts import render ,redirect
from django.http import HttpResponse
from .models import *
# Create your views here.

def home(request):
    return render(request,'home.html')

def room(request, room_id):
    username = request.GET.get('username')
    if not Home.objects.filter(room=room_id).exists():
        error = f"The room : {room_id} NOT FOUND"
        return render(request, 'home.html', {'error': error})
    return render(request, 'room.html', {'room_id': room_id, 'username': username})



def checkhome(request):
    username = request.POST['username']
    room = request.POST['room']
    if Home.objects.filter(room=room).exists():
        return redirect('/'+room+'/?username='+username)
    else:
        error = str("The room : "+ room+" does not exist")
        return render(request,"home.html", {
            'error': error,
        })
def createRoom(request):
    return render (request,'createRoom.html')

def CreateNewRoom(request):
    username = request.POST.get('username')
    room = request.POST.get('room')
    if Home.objects.filter(room =room).exists():
        output = "The room already exist"
    else :
        new_room =Home.objects.create(room = room , name = username)
        new_room.save()
        output = "The room has been created"
    return render(request,"home.html",{
        'output':output,
    })
