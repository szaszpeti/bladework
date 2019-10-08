from django.db import models
from django.utils import timezone
from django.urls import reverse_lazy, reverse
# Create your models here.
class Turbine(models.Model):
    windfarm = models.CharField(max_length=120)
    wtg_model = models.CharField(max_length=120)
    wtg_number = models.CharField(max_length=120)
    kwh = models.CharField(max_length=20)
    turbine_work_hours = models.CharField(max_length=20)
    hub_heigth  = models.CharField(max_length=120)
    customer = models.CharField(max_length=120)
    blade_type = models.CharField(max_length=120)
    set_number = models.CharField(max_length=120)
    blade_a_number = models.CharField(max_length=120)
    blade_b_number = models.CharField(max_length=120)
    blade_c_number = models.CharField(max_length=120)
    inspection_period = models.CharField(max_length=120)
    service_company = models.CharField(max_length=120)
    name_of_technicians = models.CharField(max_length=120)
    temperature = models.CharField(max_length=20)
    humidity = models.CharField(max_length=20)

    def __str__(self):
        return self.wtg_number


class Damage(models.Model):
    turbine = models.ForeignKey(Turbine, related_name="blades", on_delete=models.CASCADE)
    blade = models.CharField(max_length=20)
    finding = models.CharField(max_length=20)
    ps_ss_le_te = models.CharField(max_length=10, null=True)
    email = models.EmailField(max_length=60)
    damage_type = models.CharField(max_length=60)
    category = models.CharField(max_length=60)
    length = models.CharField(max_length=60)
    width = models.TextField(max_length=1000, blank=True)
    inspection_type = models.CharField(max_length=20)


    # def __str__(self):
    #     return self.name

    # def get_absolut_url(self):
    #     return reverse("meditater:meditater_detail", kwargs={"pk": self.id})
    #
    # def get_delete_url(self):
    #     return reverse("meditater:meditater_delete", kwargs={"pk": self.id})
    #
    # def get_email_url(self):
    #     return reverse("meditater:email_formating", kwargs={"pk": self.id})
    #
    # def get_sendingemail_url(self):
    #     return reverse("meditater:send_email", kwargs={"pk": self.id})

