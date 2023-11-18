from django.db import models
from django.utils.translation import gettext as _
# Create your models here.
class Transaction(models.Model):

    class Categories(models.IntegerChoices): 
        CLOTHES=0, _('Clothes')
        SUPERMARKETS=1, _('Supermarkets')
        RESTARAUNTS=2,_('Restaraunts')
        SERVICE=3,_('Service')
        FINANCIAL=4,_('Financial')
        MEDICINE=5,_('Medicine')
        SALARY=6,_('Salary')
        DEBT=7,_('Debt')
        GIFT=8,_('Gift')
        FUN=9,_('Fun')
        INIT = 10, _('Initial')

        __empty__ = _("Other")
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
