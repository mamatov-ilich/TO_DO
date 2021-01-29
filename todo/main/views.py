from django.shortcuts import render, HttpResponse, redirect
from .models import ToDo


def third(request):
    return render(request, "index.html")

def homepage(request):
    todo_list = ToDo.objects.all()
    return render(request, "test.html", {"todo_list": todo_list})


    
def add_todo(request):
    form = request.POST
    text = form["todo_text"]
    todo = ToDo(text=text)
    todo.save()
    return redirect(homepage)
<<<<<<< HEAD


def delete_todo(request, id):
    todo = ToDo.objects.get(id=id)
    todo.delete()
    return redirect(homepage)
=======
>>>>>>> 0f6bfc325b0292569889df59e29cc059450b0310
