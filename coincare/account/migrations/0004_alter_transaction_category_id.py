# Generated by Django 4.2.7 on 2023-11-19 00:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_alter_transaction_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='category_id',
            field=models.IntegerField(choices=[(0, 'Одежда'), (1, 'Супермаркеты'), (2, 'Рестораны'), (3, 'Сфера обслуживания'), (4, 'Финансы'), (5, 'Медицина'), (6, 'Зарплата'), (7, 'Долги'), (8, 'Подарки'), (9, 'Развлечения'), (10, 'Начальная сумма'), (11, 'Другое')], default=8),
        ),
    ]
