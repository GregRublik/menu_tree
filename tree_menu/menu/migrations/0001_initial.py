# Generated by Django 5.0.3 on 2024-03-24 09:27

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True, verbose_name='Название меню')),
                ('description', models.TextField(blank=True, max_length=300, verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'Меню',
                'verbose_name_plural': 'Меню',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='MenuItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True, verbose_name='Название пункта меню')),
                ('description', models.TextField(blank=True, max_length=300, verbose_name='Описание')),
                ('url', models.CharField(blank=True, help_text='Указывается для перехода на ресурс из конечного пункта меню, если не указать, то алгоритм будет пытаться найти потомков данного пункта меню и создать из них подменю', max_length=50, verbose_name='URL-адрес стороннего ресурса')),
                ('menu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='menu_items', to='menu.menu')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='menu.menuitem')),
            ],
            options={
                'verbose_name': 'Пункт меню',
                'verbose_name_plural': 'Пункты меню',
                'ordering': ['id'],
            },
        ),
    ]
