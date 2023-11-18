# Generated by Django 4.2.7 on 2023-11-18 06:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transaction',
            name='datetime',
        ),
        migrations.AddField(
            model_name='transaction',
            name='date',
            field=models.DateField(default='2020-01-01'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='transaction',
            name='time',
            field=models.TimeField(default='00:00'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='transaction',
            name='category_id',
            field=models.IntegerField(choices=[(None, 'Other'), (0, 'Clothes'), (1, 'Supermarkets'), (2, 'Restaraunts'), (3, 'Service'), (4, 'Financial'), (5, 'Medicine'), (6, 'Salary'), (7, 'Debt'), (8, 'Gift'), (9, 'Fun'), (10, 'Initial')], default=8),
        ),
    ]
