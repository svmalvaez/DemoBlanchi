from django.shortcuts import render

# Create your views here.
def index(request):
	return render(request, 'index.html')

def pedidos(request):
	return render(request, 'pedidos.html')

def sign_in(request):
	return render(request, 'signin.html')