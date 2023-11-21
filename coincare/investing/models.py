from django.db import models
from django.utils.translation import gettext as _
# Create your models here.
class Trade(models.Model):
    CATEGORIES = (
        (False, 'Покупка'),
        (True, 'Продажа')
    )

    uid = models.BigIntegerField()
    trade_type=models.BooleanField(choices=CATEGORIES, default=False)
    token = models.CharField(max_length=4)
    quantity = models.IntegerField()
    date=models.DateField()
    time=models.TimeField()
    trade_price=models.FloatField()

    

    def __str__(self) -> str:
        return f'{self.uid} купил {self.token}'