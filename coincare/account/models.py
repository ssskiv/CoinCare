from django.db import models
from django.utils.translation import gettext as _
# Create your models here.
class Transaction(models.Model):

    class Categories(models.IntegerChoices): 
        CLOTHES=0, _('Одежда')
        SUPERMARKETS=1, _('Супермаркеты')
        RESTARAUNTS=2,_('Рестораны')
        SERVICE=3,_('Сфера обслуживания')
        FINANCIAL=4,_('Финансы')
        MEDICINE=5,_('Медицина')
        SALARY=6,_('Зарплата')
        DEBT=7,_('Долги')
        GIFT=8,_('Подарки')
        FUN=9,_('Развлечения')
        INIT = 10, _('Начальная сумма')

        OTHER = 11, _("Другое")
    '''CATEGORIES=[
        (CLOTHES, 'Clothes'),
        (SUPERMARKETS, 'Supermarkets'),
        (RESTARAUNTS, 'Restaraunts'),
        (SERVICE, 'Service'),
        (FINANCIAL, 'Financial'),
        (MEDICINE, 'Medicine'),
        (SALARY, 'Salary'),
        (DEBT, 'Debt'),
        (GIFT, 'Gift'),
        (FUN, 'Fun'),
    ]'''

    uid = models.BigIntegerField()
    sum = models.BigIntegerField()
    transaction_type = models.BooleanField()
    category_id= models.IntegerField(default=Categories.GIFT,choices=Categories.choices)
    date=models.DateField()
    time=models.TimeField()
    comment=models.TextField(blank=True, null=True)

    def __str__(self) -> str:
        text=f'UID - {self.uid}, Sum - {self.sum}, Transaction type - {self.transaction_type}, Date - {self.date}, Time - {self.time}'
        return text
