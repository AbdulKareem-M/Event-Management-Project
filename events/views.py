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
