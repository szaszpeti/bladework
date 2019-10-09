from django.db import models
from django.utils import timezone
from django.urls import reverse_lazy, reverse

from django.utils.timezone import now
# Create your models here.
class Turbine(models.Model):
    windfarm = models.CharField(max_length=120, blank=True)
    wtg_model = models.CharField(max_length=120)
    wtg_number = models.CharField(max_length=120)
    kwh = models.CharField(max_length=20, blank=True)
    turbine_work_hours = models.CharField(max_length=20, blank=True)
    hub_heigth  = models.CharField(max_length=120, blank=True)
    customer = models.CharField(max_length=120, blank=True)
    blade_type = models.CharField(max_length=120)
    set_number = models.CharField(max_length=120, blank=True)
    blade_a_number = models.CharField(max_length=120, blank=True)
    blade_b_number = models.CharField(max_length=120, blank=True)
    blade_c_number = models.CharField(max_length=120, blank=True)
    inspection_period = models.CharField(max_length=120)
    service_company = models.CharField(max_length=120, blank=True)
    name_of_technicians = models.CharField(max_length=120)
    temperature = models.CharField(max_length=20, blank=True)
    humidity = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return self.wtg_number

    def get_absolut_url(self):
        return reverse("bladework:turbine_detail", kwargs={"pk": self.id})

    def get_delete_url(self):
        return reverse("bladework:turbine_delete", kwargs={"pk": self.id})

    # def get_email_url(self):
    #     return reverse("meditater:email_formating", kwargs={"pk": self.id})

    # def get_sendingemail_url(self):
    #     return reverse("meditater:send_email", kwargs={"pk": self.id})


class Damage(models.Model):
    turbine = models.ForeignKey(Turbine, related_name="blades", on_delete=models.CASCADE)
    blade = models.CharField(max_length=20)
    blade_number = models.CharField(max_length=20, null=True)
    finding = models.CharField(max_length=20)
    inspection_time = models.DateTimeField(default=now, editable=False)
    ps_ss_le_te = models.CharField(max_length=10, null=True)
    pd_from = models.CharField(max_length=10, null=True)
    damage_type = models.CharField(max_length=60)
    category = models.CharField(max_length=60)
    length = models.CharField(max_length=60)
    width = models.CharField(max_length=10, blank=True)

    INTERNAL = 'INT'
    EXTERNAL = 'EXT'
    INSPECTION_TYPE = [(INTERNAL, 'internal'),
                       (EXTERNAL, 'external')]
    inspection_type = models.CharField(max_length=3,
                                       choices=INSPECTION_TYPE,
                                       default=INTERNAL,
    )


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

