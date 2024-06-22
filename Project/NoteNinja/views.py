from django.shortcuts import render,redirect
from . forms import CreateUserForm,LoginForm

from django.contrib.auth.models import auth

from django.contrib.auth import authenticate,login,logout



from django.contrib.auth.decorators import login_required
from . models import createNote
from . forms import CreateNoteForm

# Create your views here.

def homepage(request):
    return render(request,'NoteNinja/index.html')



def register(request):

    form = CreateUserForm()

    if request.method == "POST":
        form = CreateUserForm(request.POST)

        if form.is_valid:
            form.save()
            return redirect('login')
        
    context = {'registrationForm' : form}

    return render(request,'NoteNinja/register.html',context)



def login(request):

    form = LoginForm()

    if request.method == "POST":
        form = LoginForm(request, data=request.POST)

        if form.is_valid():

            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username,password=password)

            if user is not None:
                auth.login(request, user)

                return redirect('view-notes')
            
    context = {'LoginForm' :form}

    return render(request,'NoteNinja/login.html',context)




def logout(request):

    auth.logout(request)

    return redirect("")



@login_required(login_url='login')
def viewnotes(request):
    getAllNotes = createNote.objects.all()
    context = {'all_notes': getAllNotes}
    return render(request,'NoteNinja/view-notes.html',context)





@login_required(login_url='login')
def createnote(request):

    createForm = CreateNoteForm()

    if request.method == "POST":
        createForm = CreateNoteForm(request.POST)

        if createForm.is_valid():
            createForm.save()
            return redirect('view-notes')
        
    
    context = {'allDetails':createForm}
    return render(request,'NoteNinja/create-note.html',context)







@login_required(login_url='login')
def updatenote(request,pk):
    note = createNote.objects.get(id=pk)

    updatenote = CreateNoteForm(instance = note)

    if request.method == "POST":
        updatenote = CreateNoteForm(request.POST, instance = note)

        if updatenote.is_valid():
            updatenote.save()
            return redirect('view-notes')
    
    context = {'updateNote':updatenote}
    return render(request,'NoteNinja/update-note.html',context)



@login_required(login_url='login')
def deletenote(request,pk):
    note = createNote.objects.get(id = pk)

    if request.method == "POST":
        note.delete()
        return redirect('view-notes')
    
    return render(request,'NoteNinja/delete-note.html')














