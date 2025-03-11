from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'informacion/pelis.html')

def futbol(request):
    nombre = "Real Madrid"
    data = {
        equipo": nombre
    }
    return render(request, 'informacion/futbol.html', data)

def jugadores(request):
    context = 

def colores(request):
    #RECUPERAMOS LA VARIABLE QUE NOS ESTAN ENVIANDO
    #MEDIENATE GET (MICOLOR)
    #DEBEMOS COMPROBAR QUE RECIBIMOS ALGO LLAMADO micolor
    if ('micolor') in request.GET):
    colorRecibido = request.GET['micolor']
    #CON EL COLOR RECIBIDO SE LO DEVOLVEMOS AL DIBUJO
    #PARA PINTARLO
    context = {
        "colordibujo": colorRecibido
    }
    return render(request, 'informacion/colores.html', context=)
else:

def saludo(request):
    return render(request, 'informacion/saludo.html')
    return render(request, 'informacion/colores.html')

def saludo(request):
    #PREGUNTAMOS DE FORMA OBLIGATORI SI HEMOS
    #RECIBIDO DATOS DEL FORMULARIO
    if ('cjasnombre' in request.POST):
        nombreRecibido = request.POST['cajanombre']
        context = {}

