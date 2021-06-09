# Generated by Django 3.2.4 on 2021-06-09 08:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_auto_20210609_0952'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='is_active',
            field=models.BooleanField(default=False, verbose_name='Actif ?'),
        ),
        migrations.AlterField(
            model_name='account',
            name='is_admin',
            field=models.BooleanField(default=False, verbose_name='Admin ?'),
        ),
        migrations.AlterField(
            model_name='account',
            name='is_staff',
            field=models.BooleanField(default=False, verbose_name='Staff ?'),
        ),
        migrations.AlterField(
            model_name='account',
            name='is_superadmin',
            field=models.BooleanField(default=False, verbose_name='Super Admin ?'),
        ),
    ]
