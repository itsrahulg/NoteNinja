from django.shortcuts import render,redirect


# Create your views here.

def homepage(request):
    return render(request,'NoteNinja/index.html')

def register(request):
    return render(request,'NoteNinja/register.html')

def login(request):
    return render(request,'NoteNinja/login.html')

def logout(request):
    pass

def viewnotes(request):
    return render(request,'NoteNinja/view-notes.html')

def createnote(request):
    pass

def updatenote(request):
    pass

def deletenote(request):
    pass






