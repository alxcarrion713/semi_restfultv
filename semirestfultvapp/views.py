from django.shortcuts import render, redirect
from . models import Show
from django.contrib import messages

# Create your views here.
def index(request):
    return redirect('/shows')

def shows(request):
    Show.objects.all()
    context= {
        'themshows': Show.objects.all()
    }


    return render(request, "allshows.html", context)

def addshow(request):
    return render(request, "add.html")

def createshow(request):
    print(request.POST)
    errors= Show.objects.show_validator(request.POST)
    print(errors)
    if len(errors)>0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect("/shows/new")

    else:
        newshow = Show.objects.create(title = request.POST['t'],network = request.POST['nw'], release_date = request.POST['rd'], description = request.POST['desc'])

    return redirect(f'/shows/{newshow.id}')

def showinfo(request,idshow):
    showobj= Show.objects.get(id=idshow)
    print(showobj)
    context = {
        'tvshow': showobj

    }
    return render(request, "infoshow.html", context)

def editshow(request, idshow):
    showtoedit = Show.objects.get(id= idshow)
    print(showtoedit)

    context ={
        'showobj': showtoedit

    }
    return render(request, "edit.html", context)

def updateshow(request, idshow):
    errors= Show.objects.show_validator(request.POST)
    print(errors)
    if len(errors)>0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect(f"/shows/{idshow}/edit")

    else:
        print(request.POST)
        showobj = Show.objects.get(id=idshow)
        showobj.title= request.POST['t']
        showobj.network= request.POST['nw']
        showobj.release_date= request.POST['rd']
        showobj.description= request.POST['desc']
        showobj.save()
    return redirect(f"/shows/{idshow}")

def delete(request, idshow):
    showdelete= Show.objects.get(id=idshow)
    showdelete.delete()
    return redirect("/shows")