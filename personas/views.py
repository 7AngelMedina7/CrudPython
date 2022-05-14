from django.shortcuts import render, redirect
from .models import Data

# Create your views here.'\
def home(request):
    datos_personas = Data.objects.all()
    # Se envia los datos
    return render(request, "Login.html", {"datos": datos_personas})

def registrarDatos(request):
    nombres = request.POST['name_']
    apellidos = request.POST['apellido_']
    email= request.POST ['email_']
    age= request.POST ['edad_']
    password= request.POST ['contra_']
    id= request.POST ['id_']

    data = Data.objects.create(nombres=nombres, apellidos=apellidos, email=email, age=age, password=password, id=id)
    
    # mandando datos a la variable datos en /
    return redirect('/')

def edicionDatos(request,id):
    data = Data.objects.get(id=id)
    return render(request, "edicionDatos.html",{"data":data})

def editarDatos(request):
    id= request.POST ['id_']
    nombres = request.POST['name_']
    apellidos = request.POST['apellido_']
    email= request.POST ['email_']
    age= request.POST ['edad_']
    password= request.POST ['contra_']

    data =  Data.objects.get(id=id)
    data.nombres = nombres
    data.apellidos = apellidos
    data.email = email
    data.age = age
    data.password = password
    data.save()

    return redirect('/')

def eliminarDatos(request, id):
    data = Data.objects.get(id=id)
    data.delete()

    #mandar ruta inicial o ruta raiz
    return redirect('/')