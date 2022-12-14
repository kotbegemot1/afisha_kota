# Generated by Django 4.1.2 on 2022-11-14 21:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Название')),
                ('description', models.TextField(verbose_name='Описание')),
                ('address', models.CharField(max_length=50, verbose_name='Адрес')),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Заголовок')),
                ('description', models.TextField(verbose_name='Описание')),
                ('event_date', models.DateTimeField(verbose_name='Время проведения')),
                ('category', models.CharField(max_length=50, verbose_name='Категория')),
                ('time_create', models.DateTimeField(auto_now_add=True, verbose_name='Время создания')),
                ('time_update', models.DateTimeField(auto_now=True, verbose_name='Время обновления')),
                ('genre', models.CharField(max_length=50, verbose_name='Жанр')),
                ('place', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='afisha_main.place', verbose_name='Место проведения')),
            ],
        ),
    ]
