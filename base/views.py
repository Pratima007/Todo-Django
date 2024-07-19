from django.shortcuts import render , redirect
from .models import Firstproject

# Create your views here.
def home(request):
    fst_obj=Firstproject.objects.all()
    context={'firsts':fst_obj}
    return render (request,'index.html',context)

def create(request):
    if request.method == "POST":
        name=request.POST.get('name')
        description=request.POST.get('description')
        status=request.POST.get('status')
        Firstproject.objects.create(name=name,description=description,status=status)
        return redirect('home')
    return render (request,'create.html')
def edit(request,pk):
    todo_objs = Firstproject.objects.get(id=pk)
    context = {'todos':todo_objs}
    if request.method == "POST":
        todo_objs.name=request.POST.get('name')
        todo_objs.description=request.POST.get('description')
        todo_objs.save()
        return redirect('home')
    return render(request,'edit.html',context)
def delete(request, pk):
    todo_objs=Firstproject.objects.get(id=pk)
    todo_objs.delete()
    return redirect('home')