from django.db import models

# Create your models here.
class Trade(models.Model):

    uid = models.BigIntegerField()
    trade_type=models.BooleanField()
    token = models.CharField(max_length=4)
    quantity = models.IntegerField()
    date=models.DateField()
    time=models.TimeField()
    trade_price=models.FloatField()

    def __str__(self) -> str:
        return f'{self.uid} купил {self.token}'