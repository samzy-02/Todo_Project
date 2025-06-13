from django.shortcuts import render,redirect,get_object_or_404
from .forms import TodoForm
from .models import Todo
# Create your views here.
def home(request):
    Todos = Todo.objects.all()
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = TodoForm()   
    return render(request, 'home.html', {'form':form, 'Todos':Todos})

def delete(request, pk):
    item = get_object_or_404(Todo, pk=pk)
    item.delete()
    return redirect('home')

def editTodo(request, pk):
    item = get_object_or_404(Todo, pk=pk)
    if request.method == 'POST':
        form = TodoForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form= TodoForm(instance=item)
        return render(request, 'update.html', {'form':form})