from django.shortcuts import render
from django.views.generic import View
from .models import EventModel
from .forms import EventForm

# Create your views here.
class Create(View):
  def get(self, request):
    form = EventForm
    return render(request, 'create.html', {'form':form})
  
  def post(self, request):
    form = EventForm(request.POST)
    if form.is_valid():
      EventModel.objects.create(**form.cleaned_data)
      form = EventForm
    return render(request, 'create.html', {'form':form})

class Read(View):
  def get(self, request):
    data = EventModel.objects.all()
    return render(request, 'read.html', {'data':data})


class Update(View):
  def get(self, request, **kwargs):
    id = kwargs.get('pk')
    data = EventModel.objects.get(id=id)
    form = EventForm(instance=data)
    return render(request, 'update.html', {'form':form})
  
  def post(self, request, **kwargs):
    id = kwargs.get('pk')
    data = EventModel.objects.get(id=id)
    form = EventForm(request.POST, instance=data)
    if form.is_valid():
      form.save()
    return render(request, 'success.html')
  
class Delete(View):
  def get(self, request, **kwargs):
    id = kwargs.get('pk')
    data = EventModel.objects.get(id=id)
    data.delete()
    return render(request, 'delete.html')
