from django.shortcuts import render,redirect
from django.shortcuts import get_object_or_404, redirect
from django.contrib import messages
from .models import Flan, Carrito, ItemCarrito
from .forms import ContactFormForm,CustomUserCreationForm
from django.contrib.auth.views import LoginView,LogoutView
from django.contrib.auth.decorators import login_required #para que los usuarios logueados pueda ver la pagina que tenga el decorativo
from django.contrib.auth import authenticate, login

# Create your views here.

def index(request):
    flanes_publicos = Flan.objects.filter(is_private=False) #Filtra los flanes que son publicos tmb puede ser is_private=False
    return render(request,'index.html',{'flanes': flanes_publicos})


def about(request):
    return render(request, 'about.html')

@login_required
def welcome(request):
    flanes_privados = Flan.objects.filter(is_private=True)
    return render(request, 'welcome.html',{'flanes':flanes_privados})

def contacto(request):
    if request.method == 'POST':
        form = ContactFormForm(request.POST)
        if form.is_valid():   #Si el formulario es valido
            form.save()
            messages.success(request, "Hemos recibido tu mensaje correctamente")
            return redirect('index')
    else:
            form = ContactFormForm()
                
    return render(request,'contacto.html',{'form': form})


def exito(request):
    return render(request, 'exito.html')

def flan_detail(request,flan_id):
    flan = Flan.objects.get(id=flan_id)
    return render(request, 'flan_detail.html', {'flan':flan})

def registro(request):
    data={
        'form':CustomUserCreationForm()
    }
    
    if request.method == 'POST':
        formulario = CustomUserCreationForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user= authenticate(username=formulario.cleaned_data["username"],password=formulario.cleaned_data["password1"])
            login(request,user)
            messages.success(request, "Te haz registrado correctamente")
            return redirect(to='index')
        data["form"] = formulario
    return render(request,'registration/registro.html',data)


def error_404(request):
    return render(request, '404.html', status=404)

class CustomLoginView(LoginView):
    template_name = 'registration/login.html'
    
class CustomLogoutView(LogoutView): 
    next_page = '/'
    

def agregar_al_carrito(request, flan_id):
    return redirect('index')


def carrito(request):
    return render(request, 'carrito.html')
