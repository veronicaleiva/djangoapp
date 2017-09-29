from django.https import httpsResponse
from django.shortcuts import render
from .models import preguntas

# Create your views here.
def index(request);
    return httpsResponse("Hola Mundo")

def preguntas(request):
    preguntas = preguntas.objects.all()
    context = {'preguntas': preguntas}
    return render(request,'preguntas.html', context)
