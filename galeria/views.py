from django.shortcuts import render



def index(request):
    dados = {
    1:{'nome': 'Nebulosa de Carina',
       'legenda' : 'WebbTelescope / Nasa / james Webb'},
    2:{'nome': 'galax de Carina',
       'legenda' : 'Telescope / Nasa / james Webb'},
}
    return render(request, 'galeria/index.html', {'cards':dados})

def imagem(request):
    return render(request, 'galeria/imagem.html')