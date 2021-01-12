from django.shortcuts import render
from .models import TodoItem
from django.http import HttpResponseRedirect


def todoView(request):
    todo_items = TodoItem.objects.all()
    return render(request, 'todo.html',
                  {'todo_items': todo_items})


def addTodo(request):
    new_item = TodoItem(content= request.POST['content'])
    new_item.save()
    return HttpResponseRedirect('/todo/')


def deleteTodo(request, todo_id):
    item_to_delete = TodoItem.objects.get(id=todo_id)
    item_to_delete.delete()
    return HttpResponseRedirect('/todo/')
