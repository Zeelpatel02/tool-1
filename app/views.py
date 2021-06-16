from django.shortcuts import render, HttpResponse
from .models import FilesUpload

#add manualy
import os
from django.conf import settings
from django.shortcuts import render, redirect
from django.templatetags.static import static

# Create your views here.
def index(request):
    if request.method =="POST":
        file = request.FILES["file"]
        document = FilesUpload.objects.create(file=file)
        document.save()
        message = "Your File is Succesfully uploaded!!!"
        return render(request,"index.html",{"messg":message})
        # return render(request, 'index.html')
    # else:
    #     message = "Welcome to Rehome's Tool"
    #     return render(request, 'index.html', {"messg":message})
    path = settings.MEDIA_ROOT
    pdf_list = os.listdir(path + '/')
    context = {'pdfs' : pdf_list}
    return render(request, "index.html", context)
def tool(request, num):
    path = settings.MEDIA_ROOT
    pdf_list = os.listdir(path + '/')
    num = num
    zippedlist = zip(pdf_list, range(1,len(pdf_list)+1))
    context = {'pdfs' : pdf_list[::-1], "var" : pdf_list[int(num-1)] , "lpdf" : zippedlist, "next" : num+1, "back" : num-1 ,"lastnum" : len(pdf_list)+1}
    return render(request, 'tool.html', context)



