from django.shortcuts import render, redirect
from django.contrib import messages

def login_view(request):
    if request.method == 'POST':
        correo = request.POST.get('correo')
        password = request.POST.get('password')
        if correo and password: 
            messages.error(request, 'Correo o contraseña incorrectos (Simulación).')
        else:
            messages.error(request, 'Por favor, ingresa tu correo y contraseña.')
    return render(request, 'login.html')

def recuperar_password(request):
    if request.method == 'POST':
        return redirect('validar_codigo')
    return render(request, 'recuperar_password.html')

def validar_codigo(request):
    if request.method == 'POST':
            return redirect('nueva_password')  # Redirige al login después de validar el código
    return render(request, 'validar_codigo.html')

def nueva_password(request):
    if request.method == 'POST':
        return redirect('login')
    return render(request, 'nueva_password.html')