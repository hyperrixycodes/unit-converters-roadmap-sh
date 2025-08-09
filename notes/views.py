from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Note
from .forms import NoteForm
# Create your views here.

def index(request):
    return HttpResponse("Hello notes app")

def notes_list(request):
    notes = Note.objects.filter(user=request.user)
    return render(request, 'notes/notes_list.html',{
        'notes': notes
    })

def create_note(request):
    form = NoteForm(request.POST)
    if form.is_valid():
        note = form.save(commit=False)
        note.user = request.user
        note.save()
        return redirect('notes_list')

    context = {
        'form': form,
    }
    return render(request, 'notes/create_note.html', context)
    
def edit_note(request, id):
    note = get_object_or_404(Note, id=id, user=request.user)
    form = NoteForm(request.POST, instance=note)
    if form.is_valid():
        note = form.save(commit=False)
        note.save()
        return redirect('notes_list')
    
    return render(request, 'notes/edit_note.html', {
        'form': form,
    })

def delete_note(request, id):
    note = get_object_or_404(Note, id=id, user=request.user)
    if request.method == "POST":
        note.delete()
        return redirect('notes_list')

    return render(request, 'notes/edit_note.html', {
        'note': note,
    })