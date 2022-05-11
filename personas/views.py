from django.shortcuts import render, redirect
from .models import Data

# Create your views here.'\
def home(request):
    datos_personas = Data.objects.all()
    # Se envia los datos
    return render(request, "Login.html", {"datos": datos_personas})

def registrarDatos(request):
    nombres = request.POST['input_name']
    apellidos = request.POST['input_lm']
    email= request.POST ['input_email']
    age= request.POST ['input_age']
    password= request.POST ['input_pass']
    id= request.POST ['input_id']

    data = Data.objects.create(nombres=nombres, apellidos=apellidos, email=email, age=age, password=password, id=id)
    print(data)
    print("TEST!!!!!")
    print("TEST!!!!!")
    print("TEST!!!!!")
    print("TEST!!!!!")
    print("TEST!!!!!")
    print("TEST!!!!!")
    # mandando datos a la variable datos
    return redirect('/')