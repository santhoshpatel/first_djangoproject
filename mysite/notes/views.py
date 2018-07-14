from django.shortcuts import render

from .models import Note
from .forms import NoteForm

# Create your views here.
def home(request):
    notes = Note.objects.all()
    form = NoteForm(request.POST or None)
    if form.is_valid():
        save_it = form.save(commit=False)
        save_it.save()
    context = {'notes': notes, 'form': form}
    return render(request,'note.html', context)