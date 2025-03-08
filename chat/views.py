from django.shortcuts import render, redirect
from chat.models import Room, Message
from django.http import HttpResponse, JsonResponse

# Create your views here.
def home(request):
    return render(request, 'home.html')

def room(request, room):
    username = request.GET.get('username')
    room_details = Room.objects.get(name=room)
    return render(request, 'room.html', {
        'username': username,
        'room': room,
        'room_details': room_details
    })





def checkview(request):
    room = request.POST['room_name']
    username = request.POST['username']

    if Room.objects.filter(name=room).exists():
        return redirect('/'+room+'/?username='+username)
    # else:
    #     new_room = Room.objects.create(name=room)
    #     new_room.save()
    #     return redirect('/'+room+'/?username='+username)
    else:
        error = str("The room : "+ room+" does not exist")
        return render(request,"home.html", {
            'error': error,
        })
    
def createRoom(request):
    return render(request, 'createRoom.html')

def CreateNewRoom(request):
    username = request.POST.get('username')
    room_name = request.POST.get('room')  # Get the room name from the form
    
    # Check if a room with this name already exists
    if Room.objects.filter(name=room_name).exists():
        output = "The room already exists"
    else:
        # Create a new room with the name from the form
        new_room = Room.objects.create(name=room_name)
        new_room.save()
        output = "The room has been created"
    
    return render(request, "home.html")







def send(request):
    message = request.POST['message']
    username = request.POST['username']
    room_id = request.POST['room_id']

    new_message = Message.objects.create(value=message, user=username, room=room_id)
    new_message.save()
    return HttpResponse('Message sent successfully')

def getMessages(request, room):
    room_details = Room.objects.get(name=room)

    messages = Message.objects.filter(room=room_details.id)
    return JsonResponse({"messages":list(messages.values())})