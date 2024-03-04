from django.shortcuts import render
from Notebook import models

# Create your views here.
def index(request):
    return render(request,"index.html",{})
def megoldas(request):
    return render(request,"megoldas.html",{})
def w_2van(request):
    return render(request,"w_2van.html",{})
def w_3gyarto(request):
    return render(request,"w_3gyarto.html",{})
def w_4teljes(request):
    return render(request,"w_4teljes.html",{})
def w_5vasarlas(request):
    return render(request,"w_5vasarlas.html",{})
def w_6nulla(request):
    return render(request,"w_6nulla.html",{})
def w_7intel(request):
    return render(request,"w_7intel.html",{})
def w_(request):
    return render(request,"w_",{})
def feltoltes(request):
    return render(request,"feltoltes.html",{})
def feltoltes_fajl(request, tabla):
    #for i in request

    return render(request,"feltoltes_fajl.html",{"tabla":tabla})
def feltoltes_fajl_kuld(request, tabla):
    
    tipus={"gep":models.gep,"oprendszer":models.oprendszer,"processzor":models.processzor}[tabla]
    for i in request.POST['tartalom'].split('\n'):
        
        print(i)
    return render(request,"feltoltes_fajl_kuld.html",{"tabla":tabla})