from django.shortcuts import render, get_object_or_404

from galeria.models import Fotografia

def index(request):
    dados = {
    1:{'nome': 'Nebulosa de Carina',
       'legenda' : 'WebbTelescope / Nasa / james Webb'},
    2:{'nome': 'galax de Carina',
       'legenda' : 'Telescope / Nasa / james Webb'},
    }

    fotografias = Fotografia.objects.all()
    return render(request, 'galeria/index.html', {'cards':fotografias})

def imagem(request, foto_id):
    fotografia = get_object_or_404(Fotografia, pk=foto_id)
    return render(request, 'galeria/imagem.html', {'fotografia': fotografia})