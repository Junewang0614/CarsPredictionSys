# Generated by Django 3.2.4 on 2022-01-04 10:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carmanage', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='series',
            name='sinfo',
            field=models.TextField(blank=True, null=True, verbose_name='车型信息'),
        ),
    ]
