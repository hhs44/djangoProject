# Generated by Django 4.0.1 on 2022-03-07 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hugo', '0004_alter_about_md_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='about',
            name='aliases',
            field=models.CharField(blank=True, default='"migrate-from-jekyl"', max_length=255, verbose_name='aliases'),
        ),
        migrations.AlterField(
            model_name='about',
            name='image',
            field=models.ImageField(blank=True, default='', upload_to='', verbose_name='封面'),
        ),
        migrations.AlterField(
            model_name='about',
            name='series',
            field=models.CharField(blank=True, default='"Themes Guide"', max_length=255, verbose_name='series'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='aliases',
            field=models.CharField(blank=True, default='"migrate-from-jekyl"', max_length=255, verbose_name='aliases'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='image',
            field=models.ImageField(blank=True, default='', upload_to='', verbose_name='封面'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='series',
            field=models.CharField(blank=True, default='"Themes Guide"', max_length=255, verbose_name='series'),
        ),
    ]