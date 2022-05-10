from django.shortcuts import render
from .models import Data

# Create your views here.'\
def home(request):
    datos_personas = Data.objects.all()
    # Se envia los datos
    return render(request, "Login.html", {"datos": datos_personas})