# Generated by Django 4.0.1 on 2022-01-19 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hugo', '0002_about_md_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='about',
            name='md_date',
            field=models.DateField(auto_now=True, verbose_name='修改日期'),
        ),
    ]
