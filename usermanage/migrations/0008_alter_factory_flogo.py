# Generated by Django 3.2.4 on 2022-01-04 07:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usermanage', '0007_auto_20220104_1526'),
    ]

    operations = [
        migrations.AlterField(
            model_name='factory',
            name='flogo',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='厂商logo'),
        ),
    ]
