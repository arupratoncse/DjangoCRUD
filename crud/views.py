from django.shortcuts import render, redirect, get_object_or_404
from .models import Student
from .forms import createFrom

def index(request):
    data = Student.objects.all()
    return render(request, "index.html",{"data": data})


def addNew(request):
	if request.method == "POST":
		form = createFrom(request.POST)
		if form.is_valid():
			form.save()
			return redirect('index')
	else:
		form = createFrom()
		return render(request,"new.html",{"form": form})


def edit(request,id):
	student= get_object_or_404(Student,pk=id)
	if request.method == "POST":
		form = createFrom(request.POST, instance=student)
		if form.is_valid():
			form.save()
			return redirect("index")
	else:
		form = createFrom(instance=student)
		return render(request,"edit.html",{"form": form})


def delete(request,id):
	st= get_object_or_404(Student,pk=id)
	if request.method == "POST":
		st.delete()
		return redirect('index')
	else:
		return render(request,"delete.html",{"st": st})