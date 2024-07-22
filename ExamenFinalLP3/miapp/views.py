from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Zuñiga_Persona
from .forms import ZuñigaPersonaForm

# Create your views here.
def index(request):
    return render(request, 'index.html')


def personas(request):
    return render(request, 'personas.html')



def lista_personas(request):
    personas = Zuñiga_Persona.objects.all()
    return render(request, 'lista_personas.html', {'personas': personas})

def detalle_persona(request, pk):
    persona = get_object_or_404(Zuñiga_Persona, pk=pk)
    return render(request, 'detalle_persona.html', {'persona': persona})

def nueva_persona(request):
    if request.method == "POST":
        form = ZuñigaPersonaForm(request.POST)
        if form.is_valid():
            persona = form.save(commit=False)
            persona.save()
            return redirect('detalle_persona', pk=persona.pk)
    else:
        form = ZuñigaPersonaForm()
    return render(request, 'editar_persona.html', {'form': form})

def editar_persona(request, pk):
    persona = get_object_or_404(Zuñiga_Persona, pk=pk)
    if request.method == "POST":
        form = ZuñigaPersonaForm(request.POST, instance=persona)
        if form.is_valid():
            persona = form.save(commit=False)
            persona.save()
            return redirect('detalle_persona', pk=persona.pk)
    else:
        form = ZuñigaPersonaForm(instance=persona)
    return render(request, 'editar_persona.html', {'form': form})

def eliminar_persona(request, pk):
    persona = get_object_or_404(Zuñiga_Persona, pk=pk)
    persona.delete()
    return redirect('lista_personas')