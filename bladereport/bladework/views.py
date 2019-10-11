from django.shortcuts import render
from django.views.generic import (TemplateView,
                                  ListView,
                                  DetailView,
                                  DeleteView,
                                  CreateView,
                                  UpdateView)
from django.shortcuts import render, get_object_or_404
from .models import Turbine, Damage, Blade
from .forms import TurbineForm, DamageForm, BladeForm

from django.urls import reverse_lazy, reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
# from .forms import UploadFileForm
from django.core.mail import send_mail
import django_excel as excel
from smtplib import SMTP_SSL as SMTP
from email.mime.text import MIMEText

import openpyxl
from django.http import HttpResponse


from datetime import datetime

class HomeView(TemplateView):
    # model = Meditater
    template_name = "index.html"
    #
    # def meditaters(self):
    #     return Meditater.objects.all()
    #!!!!USE "VIEW.MEDITATERS" on the template

class TurbineCreateView(CreateView):
    model = Turbine
    template_name = "getturbinedata.html"
    fields = '__all__'
    success_url = reverse_lazy('bladework:blade_create')

class DamageCreateView(CreateView):
    model = Damage
    template_name = "getdamage.html"
    fields = '__all__'
    success_url = reverse_lazy('bladework:take_photo')

class BladeCreateView(CreateView):
    model = Blade
    template_name = "blade_create.html"
    fields = '__all__'
    success_url = reverse_lazy('bladework:damage_create')



class PhotoView(TemplateView):
    # model = Meditater
    template_name = "takephoto.html"
    #
    # def meditaters(self):
    #     return Meditater.objects.all()
    #!!!!USE "VIEW.MEDITATERS" on the template

class TurbineListView(LoginRequiredMixin, ListView):
    model = Turbine
    ordering = ["wtg_number"]
    template_name = "turbinelist_view.html"
    #context_object_name = 'post'#

class TurbineDeleteView(LoginRequiredMixin, DeleteView):
    model = Turbine
    template_name = "turbine_delete.html"
    success_url = reverse_lazy('bladework:turbine_list_view')

class BladeDeleteView(LoginRequiredMixin, DeleteView):
    model = Blade
    template_name = "blade_delete.html"
    success_url = reverse_lazy('bladework:turbine_list_view')

class DamageDeleteView(LoginRequiredMixin, DeleteView):
    model = Damage
    template_name = "damage_delete.html"
    success_url = reverse_lazy('bladework:turbine_list_view')

class TurbineDetailView(LoginRequiredMixin, DetailView):
    model = Turbine
    template_name = "turbine_detail.html"

class BladeDetailView(LoginRequiredMixin, DetailView):
    model = Blade
    template_name = "blade_detail.html"

class TurbineUpdateView(LoginRequiredMixin, UpdateView):
    model = Turbine
    template_name = "turbine_edit.html"
    fields = '__all__'
    success_url = reverse_lazy('bladework:turbine_list_view')

class BladeUpdateView(LoginRequiredMixin, UpdateView):
    model = Blade
    template_name = "blade_edit.html"
    fields = '__all__'
    success_url = reverse_lazy('bladework:turbine_list_view')

class DamageUpdateView(LoginRequiredMixin, UpdateView):
    model = Damage
    template_name = "damage_edit.html"
    fields = '__all__'
    success_url = reverse_lazy('bladework:turbine_list_view')

def find_index(request):
    print ("THis is the request from find", request)
    queryset_list = Turbine.objects.all().order_by("wtg_number")


    query = request.GET.get("q")
    print (query)
    if query:
        queryset_list = queryset_list.filter(
            Q(wtg_number__icontains=query) |
            Q(windfarm__icontains=query) |
            Q(name_of_technicians__icontains=query)


        ).distinct()
        number_found = len(queryset_list)

        return render(request, 'query_result.html', {'queryset': queryset_list, "query":query, "number":number_found})


def photo_upload(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = DocumentForm()
    return render(request, 'core/model_form_upload.html', {
        'form': form
    })