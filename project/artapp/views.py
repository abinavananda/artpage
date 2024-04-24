from django.shortcuts import render
from .models import Art
from django.views import View



def index(request):
    return render(request,'index.html')

class CategoryView(View):
    def get(self,request,val):
        art = Art.objects.filter(category=val)
        return render(request,"category.html",locals())


def about_view(request):
    return render(request, 'about.html')  


def service(request):
    return render(request, 'service.html')  
