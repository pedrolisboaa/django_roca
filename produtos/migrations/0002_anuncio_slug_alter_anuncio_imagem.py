# Generated by Django 4.1.7 on 2023-03-23 02:17

from django.db import migrations, models
import stdimage.models


class Migration(migrations.Migration):

    dependencies = [
        ('produtos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='anuncio',
            name='slug',
            field=models.SlugField(blank=True, editable=False, max_length=100, verbose_name='Slug'),
        ),
        migrations.AlterField(
            model_name='anuncio',
            name='imagem',
            field=stdimage.models.StdImageField(blank=True, force_min_size=False, upload_to='produto', variations={'thumb': (124, 123)}, verbose_name='Imagem'),
        ),
    ]
