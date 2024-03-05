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
    fn={models.gep:lambda l:models.gep.objects.create(gyarto=l[0],tipus=l[1],kijelzo=float(l[2].replace(",",".")),memoria=int(l[3]),merevlemez=int(l[4]),videovezerlo=l[5],processzorid=int(l[6]),oprendszerid=int(l[7]),db=int(l[8])),
        models.processzor:lambda l: models.processzor.objects.create(id=int(l[0]),gyarto=l[1],tipus=l[2]),
        models.oprendszer:lambda l: models.oprendszer.objects.create(id=int(l[0]),nev=l[1])}
    for i in request.POST['tartalom'].split('\n'):
        fn[tipus](i.strip().split('\t'))
    return render(request,"feltoltes_fajl_kuld.html",{"tabla":tabla})