from django.shortcuts import render
from .models import TodoItem
from django.http import HttpResponseRedirect
from .forms import Form


def todoView(request):
    todo_items = TodoItem.objects.all()
    form = Form()
    context = {'todo_items': todo_items, 'form': form}
    return render(request, 'todo.html', context)

def addTodo(request):
    form = Form(request.POST)
    form.save()
    return HttpResponseRedirect('/todo/')

def deleteTodo(request, todo_id):
    item_to_delete = TodoItem.objects.get(id=todo_id)
    item_to_delete.delete()
    return HttpResponseRedirect('/todo/')

def updateTodo(request, todo_id):
    item_to_update = TodoItem.objects.get(id=todo_id)
    form = Form(instance=item_to_update)
    if request.method == 'POST':
        print("here")
        form = Form(request.POST, instance=item_to_update)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect('/todo/')
    return render(request, 'update.html', {'form': form})
