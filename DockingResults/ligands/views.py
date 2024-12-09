from django.shortcuts import render
from .models import Ligand
from django.shortcuts import get_object_or_404

def index(request):
    return render(request, 'index.html')

def results(request):
    from django.shortcuts import render, get_object_or_404
from .models import Ligand

def results(request):
    ligand_key = request.GET.get('ligand')
    ligand_map = {
        "ligand1": "Troriluzole",
        "ligand2": "Donepezil",
        "ligand3": "Galanathamine",
        "ligand4": "Memantine",
        "ligand5": "Rivastigmine",
    }

    ligand_name = ligand_map.get(ligand_key)
    if not ligand_name:
        return render(request, '404.html')  # Or return a custom error page

    ligand = get_object_or_404(Ligand, name=ligand_name)
    return render(request, 'results.html', {'ligand': ligand})

def simulations(request):
    return render(request, 'sim.html')
def about(request):
    return render(request, 'about.html')
