from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages

from galeria.models import Fotografia

def index(request):
    if not request.user.is_authenticated:
        messages.error(request, 'usuario nao logado')
        return redirect('login')
    
    dados = {
    1:{'nome': 'Nebulosa de Carina',
       'legenda' : 'WebbTelescope / Nasa / james Webb'},
    2:{'nome': 'galax de Carina',
       'legenda' : 'Telescope / Nasa / james Webb'},
    }

    fotografias = Fotografia.objects.order_by('-data_fotografia').filter(publicada=True)
    return render(request, 'galeria/index.html', {'cards':fotografias})

def imagem(request, foto_id):
    fotografia = get_object_or_404(Fotografia, pk=foto_id)
    return render(request, 'galeria/imagem.html', {'fotografia': fotografia})

def buscar(request):
   if not request.user.is_authenticated:
        messages.error(request, 'usuario nao logado para buscar')
        return redirect('login')
   fotografias = Fotografia.objects.order_by('-data_fotografia').filter(publicada=True)
   if  'buscar' in request.GET:
       nome_buscar = request.GET['buscar']
       if nome_buscar:
           fotografias = fotografias.filter(nome__icontains=nome_buscar)
   return render(request, 'galeria/buscar.html', {'cards': fotografias})