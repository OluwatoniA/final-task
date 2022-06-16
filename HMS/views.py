from multiprocessing import context
from turtle import title
from django.shortcuts import render, redirect
from .forms import RecordCreateForm, RecordSearchForm, RecordUpdateForm

from HMS.models import Record

# Create your views here.
def home(request):
    title = 'Welcome To Laurent Hotel'
    context = {
        "title": title,
    }
    return render(request, "home.html",context)

def occupant_data(request):
    header = 'Data of Occupant'
    form = RecordSearchForm(request.POST or None)
    queryset = Record.objects.all()
    context = {
        "header": header,
        "queryset": queryset,
        "form": form,
    }
    if request.method == 'POST':
        queryset = Record.objects.filter(room_number__icontains=form['room_number'].value(),
                                                occupant_name__icontains=form['occupant_name'].value()
                                                )
        context = {
        "form": form,
        "header": header,
        "queryset": queryset,
    }
    return render(request, "occupant_data.html",context)

def add_occupants(request):
    form = RecordCreateForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('/occupant_data')
    context = {
            "form": form,
            "title": "Add Occupant",
    }
    return render(request, "add_occupants.html", context)

def update_data(request, pk):
	queryset = Record.objects.get(id=pk)
	form = RecordUpdateForm(instance=queryset)
	if request.method == 'POST':
		form = RecordUpdateForm(request.POST, instance=queryset)
		if form.is_valid():
			form.save()
			return redirect('/occupant_data')

	context = {
		'form':form
	}
	return render(request, 'add_occupants.html', context)

def delete_data(request, pk):
    queryset = Record.objects.get(id=pk)
    if request.method == 'POST':
        queryset.delete()
        return redirect('/occupant_data')
    return render(request, 'delete_data.html')                                