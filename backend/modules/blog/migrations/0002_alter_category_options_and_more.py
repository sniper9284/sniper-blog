# Generated by Django 5.1.3 on 2024-11-06 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Категория', 'verbose_name_plural': 'Категории'},
        ),
        migrations.RenameField(
            model_name='category',
            old_name='parrent',
            new_name='parent',
        ),
        migrations.AlterField(
            model_name='category',
            name='description',
            field=models.TextField(max_length=300, verbose_name='Описание категории'),
        ),
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(blank=True, max_length=255, verbose_name='URL категории'),
        ),
    ]