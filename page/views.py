

from datetime import datetime
import imp
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone 
from page.models import Todo
from django.http import HttpResponseRedirect 
# Create your views here.
def home(request):
    todo_items=Todo.objects.all().order_by("-Added_date")
    return render(request,'index.html',{"todo_items":todo_items})
@csrf_exempt
def add_todo(request):
     print(request.POST)
     content=request.POST['content']
     DATE=request.POST['date']
     print(DATE)
     created_object=Todo.objects.create(Added_date=datetime,item=content,due=DATE)
     print(content)
     Due=request.POST['date']
     #print( created_object)
     print(created_object.id)
     #tdo_list=Todo.objects.all().count()
     #print(tdo_list)
     return HttpResponseRedirect("/")
#Read on csrf_exempt
@csrf_exempt
def delete_todo(request,todo_id):
    Todo.objects.get(id=todo_id).delete()
    return HttpResponseRedirect("/")