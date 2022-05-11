from django.shortcuts import redirect, render
from .models import Data

# Create your views here.'\
def home(request):
    datos_personas = Data.objects.all()
    # Se envia los datos
    return render(request, "Login.html", {"datos": datos_personas})

def registrarDatos(request):
    nombres = request.POST.get('input_name')
    apellidos = request.POST.get ('input_lm')
    email= request.POST.get ('input_email')
    age= request.POST.get ('input_age')
    password= request.POST.get('input_pass')

    datos = Data.objects.create(nombres=nombres, apellidos=apellidos, email=email, age=age, password=password)

    # mandando datos a la variable datos
    return redirect('/')