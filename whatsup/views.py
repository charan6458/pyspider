from django.shortcuts import render,HttpResponse

# Create your views here.
def profile(request):
    return HttpResponse('welcome without template')
