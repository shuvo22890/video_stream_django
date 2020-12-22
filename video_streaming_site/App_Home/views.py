from django.shortcuts import render
from .models import Category, Video
from App_Login.models import Review

# Create your views here.
def home(request):
    video = Video.objects.all()
    atleastOne = True
    search = ''
    if request.method == 'GET':
        search = request.GET.get('search', '')
        srchVdo = Video.objects.filter(name__icontains=search)
        video = srchVdo
        if srchVdo.count() < 1:
            atleastOne = False

    return render(request, 'App_Home/index.html', {'videos': video, 'atleastOne': atleastOne, 'search': search})

def cat(request):
    cats = Category.objects.all()
    return render(request, 'App_Home/Categories.html', {'cats': cats})


def catVideo(request, catId):
    filtered = Video.objects.filter(cat=catId)
    catName = Category.objects.get(pk=catId)

    if filtered.count() < 1:
        filtered = False

    return render(request, 'App_Home/catVideo.html', {'catVideo': filtered, 'name': catName})
