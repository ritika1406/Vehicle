from django.shortcuts import render, redirect, get_object_or_404
from django.conf import settings
from django.urls import reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import *
from django.contrib.auth.models import Group, User

#Helpers
from .forms import VehicledataModelForm

# Create your views here.
class VehicleDataListView(ListView):
    template_name = 'index.html'
    queryset = Vehicledata.objects.all()

class VehicleDataDetailView(DetailView):
    template_name = 'detail.html'
    # queryset = Vehicledata.objects.all()

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Vehicledata, id=id_)


# def VehicleData(request):
#     vehicle = Vehicledata.objects.all()
#     context={
#         "vehicle": vehicle
#     }
#     return render( request, "index.html", context)

class VehicledataCreateView(CreateView):
    template_name = 'add.html'
    form_class = VehicledataModelForm
    queryset = Vehicledata.objects.all()
    
    
    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)

class VehicledataUpdateView(UpdateView):
    template_name = 'add.html'
    form_class = VehicledataModelForm
    
    
    def get_object(self):
        vehiclenumber_ = self.kwargs.get("vehiclenumber")
        return get_object_or_404(Vehicledata, vehiclenumber=vehiclenumber_)
    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)


class VehicledataDeleteView(DeleteView):
    
    template_name = "delete.html"

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Article, id=id_)
    def get_success_url(self):
        return reverse('Vehicledata: Vehicledata')
