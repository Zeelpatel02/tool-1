from django.shortcuts import render, HttpResponse
from .models import FilesUpload

#add manualy
import os
from django.conf import settings
from django.shortcuts import render
from django.templatetags.static import static

# Create your views here.
def index(request):
    if request.method =="POST":
        file = request.FILES["file"]
        document = FilesUpload.objects.create(file=file)
        document.save()
        # message = "Your File is Succesfully uploaded..."
        # return render(request,"index.html",{"messg":message})
        return render(request, 'index.html')
    path = settings.MEDIA_ROOT
    pdf_list = os.listdir(path + '/')
    context = {'pdfs' : pdf_list}
    return render(request, "index.html", context)
def tool(request):
    path = settings.MEDIA_ROOT
    pdf_list = os.listdir(path + '/')
    context = {'pdfs' : pdf_list[::-1]}
    return render(request, 'tool.html', context)
