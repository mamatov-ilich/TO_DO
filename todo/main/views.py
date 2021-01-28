from django.shortcuts import render, HttpResponse


def homepage(request):
    return render(request, "index.html")

def third(request):
    return render(request, "test.html")

# Create your views here.
