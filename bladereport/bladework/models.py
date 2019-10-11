from django.db import models
from django.utils import timezone
from django.urls import reverse_lazy, reverse
from datetime import datetime, date

from django.utils.timezone import now
# Create your models here.


class Turbine(models.Model):
    wtg_number = models.CharField(max_length=120)
    windfarm = models.CharField(max_length=120, blank=True)
    wtg_manufacturer = models.CharField(max_length=120, blank=True)
    wtg_model = models.CharField(max_length=120)
    customer = models.CharField(max_length=120, blank=True)
    hub_heigth = models.CharField(max_length=10, blank=True)
    blade_type = models.CharField(max_length=10, blank=True)
    blade_length = models.CharField(max_length=10, blank=True)
    set_number = models.CharField(max_length=12, blank=True)
    kwh = models.CharField(max_length=10, blank=True)
    turbine_work_hours = models.CharField(max_length=10, blank=True)
    inspection_period = models.DateField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.wtg_number

    def get_absolut_url(self):
        return reverse("bladework:turbine_detail", kwargs={"pk": self.id})

    def get_delete_url(self):
        return reverse("bladework:turbine_delete", kwargs={"pk": self.id})



class Blade(models.Model):
    turbine = models.ForeignKey(Turbine, max_length=12, on_delete=models.CASCADE)

    A = "A"
    B = "B"
    C = "C"
    BLADE = [(A, 'A'),
             (B, 'B'),
             (C, 'C')]
    blade = models.CharField(max_length=1, choices=BLADE)
    blade_number = models.CharField(max_length=12, blank=True)
    inspection_time = models.DateField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.blade_number

    def get_absolut_url(self):
        return reverse("bladework:blade_detail", kwargs={"pk": self.id})

    def get_delete_url(self):
        return reverse("bladework:blade_delete", kwargs={"pk": self.id})




class Damage(models.Model):
    blade = models.ForeignKey(Blade, on_delete=models.CASCADE)
    damage_type = models.CharField(max_length=200)
    PREASURESIDE = 'PS'
    SECTIONSIDE = 'SS'
    LEADINGEDGE = 'LE'
    TRAILINGEDGE = 'TE'
    POSITION_ON_BLADE = [(PREASURESIDE, 'PS - Preasure Side'),
                         (SECTIONSIDE, 'SS - Section Side'),
                         (LEADINGEDGE, 'LE - Leading Edge'),
                         (TRAILINGEDGE, 'TE - Trailing Edge')]

    position = models.CharField(max_length=2,
                                choices=POSITION_ON_BLADE,
                                default=LEADINGEDGE,
                                )

    distance_from = models.CharField(max_length=10, null=True)
    damage_type = models.CharField(max_length=60, blank=True)

    ONE = '1'
    TWO = '2'
    THREE = '3'
    FOUR = '4'
    CATEGORY_LEVEL = [(ONE, '1'),
                      (TWO, '2'),
                      (THREE, '3'),
                      (FOUR, '4')]

    category = models.CharField(max_length=1,
                                choices=CATEGORY_LEVEL,
                                default=ONE)

    length = models.CharField(max_length=10)
    width = models.CharField(max_length=10, blank=True)



    def __str__(self):
        return self.category

    def get_absolut_url(self):
        return reverse("bladework:damage_detail", kwargs={"pk": self.id})


    def get_delete_url(self):
        return reverse("bladework:damage_delete", kwargs={"pk": self.id})
# class Turbine(models.Model):
#     windfarm = models.CharField(max_length=120, blank=True)
#     wtg_model = models.CharField(max_length=120)
#     wtg_number = models.CharField(max_length=120)
#     kwh = models.CharField(max_length=10, blank=True)
#     turbine_work_hours = models.CharField(max_length=10, blank=True)
#     hub_heigth  = models.CharField(max_length=10, blank=True)
#     customer = models.CharField(max_length=120, blank=True)
#     blade_type = models.CharField(max_length=120)
#     set_number = models.CharField(max_length=120, blank=True)
#     blade_A_number = models.CharField(max_length=120, blank=True)
#     blade_B_number = models.CharField(max_length=120, blank=True)
#     blade_C_number = models.CharField(max_length=120, blank=True)
#     inspection_period = models.DateField(auto_now_add=True, blank=True)
#     service_company = models.CharField(max_length=120, blank=True)
#     name_of_technicians = models.CharField(max_length=120)
#     temperature = models.CharField(max_length=10, blank=True)
#     humidity = models.CharField(max_length=10, blank=True)
#
#     def __str__(self):
#         return self.wtg_number
#
#     def get_absolut_url(self):
#         return reverse("bladework:turbine_detail", kwargs={"pk": self.id})
#
#     def get_delete_url(self):
#         return reverse("bladework:turbine_delete", kwargs={"pk": self.id})
#
#     # def get_email_url(self):
#     #     return reverse("meditater:email_formating", kwargs={"pk": self.id})
#
#     # def get_sendingemail_url(self):
#     #     return reverse("meditater:send_email", kwargs={"pk": self.id})
#
#
#
#
#
#






















# class Damage(models.Model):
#     turbine = models.ForeignKey(Turbine, related_name="blades", on_delete=models.CASCADE)
#
#     A = "A"
#     B = "B"
#     C = "C"
#     BLADE = [(A, 'A'),
#              (B, 'B'),
#              (C, 'C')]
#     blade = models.CharField(max_length=1,
#                              choices=BLADE)
#     blade_number = models.CharField(max_length=20, null=True)
#     finding = models.CharField(max_length=20)
#     inspection_time = models.DateField(auto_now_add=True, blank=True)
#
#     PREASURESIDE = 'PS'
#     SECTIONSIDE = 'SS'
#     LEADINGEDGE = 'LE'
#     TRAILINGEDGE = 'TE'
#     POSITION_ON_BLADE = [(PREASURESIDE, 'PS - Preasure Side'),
#                        (SECTIONSIDE, 'SS - Section Side'),
#                        (LEADINGEDGE, 'LE - Leading Edge'),
#                        (TRAILINGEDGE, 'TE - Trailing Edge')]
#
#     ps_ss_le_te = models.CharField(max_length=2,
#                                    choices=POSITION_ON_BLADE,
#                                    default=LEADINGEDGE,
#     )
#
#     pd_from = models.CharField(max_length=10, null=True)
#     damage_type = models.CharField(max_length=60)
#
#     ONE = '1'
#     TWO = '2'
#     THREE = '3'
#     FOUR = '4'
#     CATEGORY_LEVEL = [(ONE, '1'),
#                       (TWO, '2'),
#                       (THREE, '3'),
#                       (FOUR, '4')]
#
#     category = models.CharField(max_length=1,
#                                 choices=CATEGORY_LEVEL,
#                                 default=ONE)
#
#     length = models.CharField(max_length=10)
#     width = models.CharField(max_length=10, blank=True)
#
#     INTERNAL = 'INT'
#     EXTERNAL = 'EXT'
#     INSPECTION_TYPE = [(INTERNAL, 'internal'),
#                        (EXTERNAL, 'external')]
#     inspection_type = models.CharField(max_length=3,
#                                        choices=INSPECTION_TYPE,
#                                        default=INTERNAL,
#     )
#
#
#
#
#
#
#

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

