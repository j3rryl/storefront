from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
#request handler ik what youre thinking ->template??

# def home(request):
#     return HttpResponse('Home Page')
# def room(request):
#     return HttpResponse('ROOM')

rooms=[
    {
        'id':1,
        'name':"Let's learn python!"
    },
    {
        'id':2,
        'name':"Design with python!"
    },
    {
        'id':3,
        'name':"Frontend Dev's!"
    },
    
]
def home(request):
    context = {'rooms':rooms}
    return render(request, 'base/home.html', context)
def room(request, pk):
    room=None
    for i in rooms:
        if i['id']==int(pk):
            room=i
    context = {'room':room}
    return render(request, 'base/room.html', context)