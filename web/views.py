from django.shortcuts import render,redirect
from .models import Flan
from .forms import ContactFormForm

# Create your views here.

def index(request):
    flanes_publicos = Flan.objects.filter(is_private=False) #Filtra los flanes que son publicos tmb puede ser is_private=False
    return render(request,'index.html',{'flanes': flanes_publicos})


def about(request):
    return render(request, 'about.html')

def welcome(request):
    flanes_privados = Flan.objects.filter(is_private=True)
    return render(request, 'welcome.html',{'flanes':flanes_privados})

def contacto(request):
    if request.method == 'POST':
        form = ContactFormForm(request.POST)
        if form.is_valid():   #Si el formulario es valido
            form.save()
            return redirect('exito')
    else:
            form = ContactFormForm()
                
    return render(request,'contacto.html',{'form': form})


def exito(request):
    return render(request, 'exito.html')

def prueba(request):
    if request.method == 'POST':
        form = ContactFormForm(request.POST)
        if form.is_valid():   #Si el formulario es valido
            form.save()
            return redirect('exito')
    else:
            form = ContactFormForm()
                
    return render(request,'prueba.html',{'form': form})