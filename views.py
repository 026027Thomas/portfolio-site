from django.shortcuts import render, redirect
from .forms import ProjectForm

def add_project(request):
    if request.method == "POST":
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('projects')
    else:
        form = ProjectForm()

    return render(request, 'add_project.html', {'form': form})