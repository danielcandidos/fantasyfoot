# -*- coding: utf-8 -*-
'''
Created on 25/05/2014
@author: Daniel
'''
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.contrib.auth.decorators import login_required

from soccer.models import Clube, Jogador
from soccer.forms import FormClube, FormJogador

########################################################################################
#@login_required
def homeClube (request):
    lista_clubes = Clube.objects.all()
    
    return render_to_response("homeClub.html", {'lista_clubes': lista_clubes},
                        context_instance=RequestContext(request))
########################################################################################


########################################################################################
def homeJogador (request):
    lista_jog = Jogador.objects.all()
    
    return render_to_response("homeJogador.html", {'lista_jog': lista_jog},
                        context_instance=RequestContext(request))
########################################################################################


########################################################################################
#@login_required
def adicionaClube(request):
    if request.method == "POST":
        form = FormClube(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return render_to_response("mensagens/salvo.html", {})
        pass
    else:            
        form = FormClube()
    
    return render_to_response("novoClube.html", {"form": form},
                        context_instance = RequestContext(request))
########################################################################################


########################################################################################
#@login_required
def infoClube(request, nr_clube):
    clube = get_object_or_404(Clube, pk=nr_clube)
    
    if request.method == "POST":
        form = FormClube(request.POST, request.FILES, instance=clube)
        
        if form.is_valid():
            clube = form.save(commit=False)
            #clube.usuario = request.user
            clube.save()
            return render_to_response("mensagens/salvo.html", {})        
    else:
        form = FormClube(instance=clube)   
    
    return render_to_response("infoClube.html",{'form': form},
                    context_instance=RequestContext(request))
########################################################################################


########################################################################################
def adicionaJogador(request):
    if request.method == "POST":
        form = FormJogador(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return render_to_response("mensagens/salvo.html", {})
        pass
    else:            
        form = FormJogador()
    
    return render_to_response("novoJogador.html", {"form": form},
                        context_instance = RequestContext(request))
########################################################################################