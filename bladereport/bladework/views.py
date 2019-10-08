from django.shortcuts import render
from django.views.generic import (TemplateView,
                                  ListView,
                                  DetailView,
                                  DeleteView,
                                  CreateView,
                                  UpdateView)
from django.shortcuts import render, get_object_or_404
from .models import Turbine, Damage
from .forms import TurbineForm, DamageForm

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
    success_url = reverse_lazy('bladework:damage')

class DamageCreateView(CreateView):
    model = Damage
    template_name = "getdamage.html"
    fields = '__all__'
    success_url = reverse_lazy('bladework:home')
