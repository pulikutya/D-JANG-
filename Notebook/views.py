from django.shortcuts import render

# Create your views here.
def megoldas(request):
    return render(request,"megoldas.html",{})
def _2van(request):
    return render(request,"_2van.html",{})
def _3gyarto(request):
    return render(request,"_3gyarto.html",{})
def _4teljes(request):
    return render(request,"_4teljes.html",{})
def _5vasarlas(request):
    return render(request,"_5vasarlas.html",{})
def _6nulla(request):
    return render(request,"_6nulla.html",{})
def _7intel(request):
    return render(request,"_7intel.html",{})
def _(request):
    return render(request,"_",{})