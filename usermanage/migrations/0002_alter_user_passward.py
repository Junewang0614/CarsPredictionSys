# Generated by Django 3.2.4 on 2022-01-03 08:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usermanage', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='passward',
            field=models.CharField(max_length=40, verbose_name='密码'),
        ),
    ]