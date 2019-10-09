# Generated by Django 2.2.5 on 2019-10-09 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bladework', '0002_remove_damage_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='damage',
            name='blade_number',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='damage',
            name='pd_from',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='damage',
            name='inspection_type',
            field=models.CharField(choices=[('INT', 'internal'), ('EXT', 'external')], default='INT', max_length=2),
        ),
        migrations.AlterField(
            model_name='damage',
            name='width',
            field=models.TextField(blank=True, max_length=10),
        ),
        migrations.AlterField(
            model_name='turbine',
            name='blade_a_number',
            field=models.CharField(blank=True, max_length=120),
        ),
        migrations.AlterField(
            model_name='turbine',
            name='blade_b_number',
            field=models.CharField(blank=True, max_length=120),
        ),
        migrations.AlterField(
            model_name='turbine',
            name='blade_c_number',
            field=models.CharField(blank=True, max_length=120),
        ),
        migrations.AlterField(
            model_name='turbine',
            name='customer',
            field=models.CharField(blank=True, max_length=120),
        ),
        migrations.AlterField(
            model_name='turbine',
            name='hub_heigth',
            field=models.CharField(blank=True, max_length=120),
        ),
        migrations.AlterField(
            model_name='turbine',
            name='humidity',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='turbine',
            name='kwh',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='turbine',
            name='service_company',
            field=models.CharField(blank=True, max_length=120),
        ),
        migrations.AlterField(
            model_name='turbine',
            name='set_number',
            field=models.CharField(blank=True, max_length=120),
        ),
        migrations.AlterField(
            model_name='turbine',
            name='temperature',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='turbine',
            name='turbine_work_hours',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='turbine',
            name='windfarm',
            field=models.CharField(blank=True, max_length=120),
        ),
    ]