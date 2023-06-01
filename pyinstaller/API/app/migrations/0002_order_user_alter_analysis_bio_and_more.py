# Generated by Django 4.1.2 on 2023-05-20 04:29

import app.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='user',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='analysis',
            name='bio',
            field=models.CharField(help_text='БИО материал', max_length=512),
        ),
        migrations.AlterField(
            model_name='analysis',
            name='description',
            field=models.CharField(help_text='Описание услуги', max_length=512),
        ),
        migrations.AlterField(
            model_name='analysis',
            name='name',
            field=models.CharField(help_text='Название услуги', max_length=512),
        ),
        migrations.AlterField(
            model_name='analysis',
            name='preparation',
            field=models.CharField(help_text='Необходимая подготовка', max_length=512),
        ),
        migrations.AlterField(
            model_name='analysis',
            name='price',
            field=models.DecimalField(decimal_places=2, help_text='Цена услуги', max_digits=10),
        ),
        migrations.AlterField(
            model_name='analysis',
            name='time_result',
            field=models.CharField(help_text='Время выполнения', max_length=128),
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(help_text='Название категории', max_length=512),
        ),
        migrations.AlterField(
            model_name='order',
            name='address',
            field=models.CharField(help_text='Адрес', max_length=512),
        ),
        migrations.AlterField(
            model_name='order',
            name='comment',
            field=models.CharField(help_text='Комментарий', max_length=512),
        ),
        migrations.AlterField(
            model_name='order',
            name='date_time',
            field=models.DateField(default=django.utils.timezone.now, help_text='Удобная дата'),
        ),
        migrations.AlterField(
            model_name='order',
            name='phone',
            field=models.CharField(help_text='Телефон для связи', max_length=12),
        ),
        migrations.AlterField(
            model_name='patient',
            name='date_of_birth',
            field=models.DateField(default=app.models.get_default_date, help_text='Дата пождения'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='first_name',
            field=models.CharField(help_text='Имя', max_length=512),
        ),
        migrations.AlterField(
            model_name='patient',
            name='image',
            field=models.ImageField(help_text='Изображение профиля', upload_to='patients/%Y/%m/%d/'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='last_name',
            field=models.CharField(help_text='Фамилия', max_length=512),
        ),
        migrations.AlterField(
            model_name='patient',
            name='middle_name',
            field=models.CharField(help_text='Отчество', max_length=512),
        ),
        migrations.AlterField(
            model_name='patient',
            name='pol',
            field=models.CharField(help_text='Пол', max_length=64),
        ),
    ]
