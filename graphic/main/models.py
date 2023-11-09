from django.db import models

class Data(models.Model):
    id = models.IntegerField('index', primary_key=True)
    date = models.TextField('Дата внесения информации')
    source = models.TextField('Источник')
    selection = models.TextField('Выборка (описание)')
    MKB_code = models.TextField('Код класса МКБ 10')
    MKB_name = models.TextField('Наименование класса МКБ 10')
    first_type = models.TextField('Тип заболеваемости 1')
    second_type = models.TextField('Тип заболеваемости 2')
    third_type = models.TextField('Тип заболеваемости 3')
    morbidity = models.FloatField('Заболеваемость')
    country = models.TextField('Страна') 
    district = models.TextField('Федеральный округ')
    industry = models.TextField('Отрасль')
    age = models.TextField('Квант возраста')
    gender = models.TextField('Пол')
    year = models.IntegerField('Год данных')
    source_link = models.TextField('Ссылка на источник')

    def __str__(self):
        return self.MKB_name