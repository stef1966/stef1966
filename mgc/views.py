from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from .models import Projet, FormCovid
from django.template import loader

from django import template
register = template.Library()

# Create your views here.
def index(request):
    latest_form_list = FormCovid.objects.order_by('-created_at')[:10]
    template = loader.get_template('mgc/covidForm.html')
    context = {
        'latest_entrepot_list': latest_form_list,
    }
    return HttpResponse(template.render(context, request))

def IndexPageController(request):
    return HttpResponseRedirect("/mgc/homePage")

def CovidForm(request):
    return render(request, "mgc/covidForm.html")

def add_Form(request):
    print("Ajouter entrepot:", request.POST)
    # if request.method!="POST":
    #     return HttpResponse("<h2>Method Now Allowed</h2>")
    # else:
    #     # file=request.FILES['photo']
    #     # fs=FileSystemStorage()
    #     # photo_img=fs.save(file.name,file)
    #     try:
    #         vLargeur = Decimal(request.POST.get('largeur') if request.POST.get('largeur','') != "" else 0)
    #         vProfondeur = Decimal(request.POST.get('profondeur') if request.POST.get('profondeur','') != "" else 0)
    #         vP2=vLargeur * vProfondeur
    #         # vP2=vLargeur*vProfondeur
    #         entrepot=Entrepots(
    #             numEnt=request.POST.get('numEnt',''),
    #             largeur = vLargeur,
    #             profondeur = vProfondeur,
    #             prixMensuel = request.POST.get('prix','') if request.POST.get('prix','') != "" else "0",
    #             entree = request.POST.get('entree','') if request.POST.get('entree','') != "" else "",
    #             type = request.POST.get('type','') if request.POST.get('type','') != "" else "",
    #             etage = request.POST.get('etage','') if request.POST.get('etage','') != "" else "",
    #             p2 = vP2,
    #             notes = request.POST.get('notes','') if request.POST.get('notes','') != "" else "",
    #             status = request.POST.get('disponibilite','') if request.POST.get('disponibilite','') != "" else "")
    #             # status=request.POST.get('profondeur',''),
    #             # prixMensuel=request.POST.get('prixMensuel',''))
    #             # entree=request.POST.get('entree',''),
    #             # type=request.POST.get('type',''),
    #             # etage=request.POST.get('etage',''),
    #             # p2=request.POST.get('superficie',''),
    #             # notes=request.POST.get('notes',''),
    #             # status=request.POST.get('disponibilite',''))
    #             # photo=photo_img)
    #         print(" try:", entrepot)
    #         entrepot.save()
    #         print("Succee")
    #         messages.success(request,"Added Successfully")
    #     except Exception as e:
    #         print("Voici erreur entrepot: ", e)
    #         messages.error(request,"Failed to Add Entrepot")
    #         print(request, " Fail")

    return HttpResponseRedirect("/mgc/addform")
