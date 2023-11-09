# Generated by Django 4.2.6 on 2023-11-03 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Data',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False, verbose_name='index')),
                ('date', models.TextField(verbose_name='Дата внесения информации')),
                ('source', models.TextField(verbose_name='Источник')),
                ('selection', models.TextField(verbose_name='Выборка (описание)')),
                ('MKB_code', models.TextField(verbose_name='Код класса МКБ 10')),
                ('MKB_name', models.TextField(verbose_name='Наименование класса МКБ 10')),
                ('first_type', models.TextField(verbose_name='Тип заболеваемости 1')),
                ('second_type', models.TextField(verbose_name='Тип заболеваемости 2')),
                ('third_type', models.TextField(verbose_name='Тип заболеваемости 3')),
                ('morbidity', models.FloatField(verbose_name='Заболеваемость')),
                ('country', models.TextField(verbose_name='Страна')),
                ('district', models.TextField(verbose_name='Федеральный округ')),
                ('industry', models.TextField(verbose_name='Отрасль')),
                ('age', models.TextField(verbose_name='Квант возраста')),
                ('gender', models.TextField(verbose_name='Пол')),
                ('year', models.IntegerField(verbose_name='Год данных')),
                ('source_link', models.TextField(verbose_name='Ссылка на источник')),
            ],
        ),
    ]