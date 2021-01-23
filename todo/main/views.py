from django.shortcuts import render, HttpResponse


def homepage(request):
    return render(request, "index.html")

def third(request):
    return HttpResponse ('This is page test 3')

# Create your views here.
