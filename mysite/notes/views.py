from django.shortcuts import render

# Create your views here.
def Note(request):
    return render (request,'mysite/static/templates/note.html',{})
