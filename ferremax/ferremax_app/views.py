from django.shortcuts import render, get_object_or_404, redirect
from .forms import RegistroForm, ProductoForm, EliminarProForm,ModificarForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from .models import Producto, CategoriaProducto, Especialidad
# Create your views here.
def home(request):
    return render (request, 'home.html')

def registrar(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            nombre_completo = form.cleaned_data.get('nombre_completo')
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            confirmar_password = form.cleaned_data.get('confirmar_password')

            # Verifica que las contraseñas ingresadas sean iguales
            if password != confirmar_password:
                return render(request, 'registrar.html', {
                    'form': RegistroForm(),
                    'error': 'Las contraseñas no coinciden.'
                })

            try:
                user = User.objects.create_user(username=email, email=email, password=password, first_name=nombre_completo)
                user.save()
                login(request, user)
                return redirect('home')
            except IntegrityError:
                return render(request, 'registrar.html', {
                    'form': RegistroForm(),
                    'error': 'El correo electrónico ya está registrado.'
                })
    else:
        form = RegistroForm()
    return render(request, 'registrar.html', {'form': form})

def tasks(request):
    return render (request, 'tasks.html')

def cerrar_sesion(request):
    logout(request)
    return redirect('home')

def ingresar(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=email, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                # Maneja el caso en que el usuario no esté registrado, la contraseña sea incorrecta
                # o el correo electrónico esté mal formateado
                return render(request, 'ingresar.html', {
                    'form': form,
                    'error': 'Correo electrónico o contraseña incorrectos.'
                })
        else:
            # Maneja el caso en que el correo electrónico esté mal formateado
            return render(request, 'ingresar.html', {
                'form': form,
                'error': 'Por favor ingrese un correo electrónico válido.'
            })
    else:
        form = AuthenticationForm()
    return render(request, 'ingresar.html', {'form': form})

def ingresar_productos(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ingresarproductos')
    else:
        form = ProductoForm()
    return render(request, 'ingresarproductos.html', {'form': form})

def modificar_producto(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    if request.method == 'POST':
        form = ModificarForm(request.POST, instance=producto)
        if form.is_valid():
            form.save()
            return redirect('lista_productos')  # Ajusta el nombre de la vista de redirección según tu proyecto
    else:
        form = ModificarForm(instance=producto)
    return render(request, 'modificarproducto.html', {'form': form})

def eliminar_producto(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    if request.method == 'POST':
        form = EliminarProForm(request.POST)
        if form.is_valid() and form.cleaned_data['confirmacion']:
            producto.delete()
            return redirect('lista_productos')  # Ajusta el nombre de la vista de redirección según tu proyecto
    else:
        form = EliminarProForm()
    return render(request, 'eliminarproducto.html', {'form': form, 'producto': producto})

def lista_productos(request):
    productos = Producto.objects.all()
    return render(request, 'listaproductos.html', {'productos': productos})