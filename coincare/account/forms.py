from django import forms

from django.conf import settings

from django.utils.translation import gettext as _
from .models import Transaction
from django.contrib.admin.widgets import AdminDateWidget, AdminTimeWidget


class TransactionForm(forms.ModelForm):
    CATEGORIES = (
        (False, 'Списание'),
        (True, 'Начисление')
    )

    date = forms.DateField(label="Дата", widget=AdminDateWidget(
        attrs={'placeholder': "Введите дату", "style": "border-radius: 6px; border:1px solid; margin-bottom: 2%; box-shadow: inset 0 0 4px rgba(0, 0, 0, 0.2)"}), required=True)
    comment = forms.CharField(label="Комменатрий", required=False, widget=forms.TextInput(
        attrs={"placeholder": "Добавьте комментарий", "style": "border-radius: 6px; border:1px solid; margin-bottom: 2%; box-shadow: inset 0 0 4px rgba(0, 0, 0, 0.2)"}))
    uid = forms.IntegerField(label="ID пользователя",
                             widget=forms.HiddenInput(), required=False)
    time = forms.TimeField(label="Время", widget=AdminTimeWidget(
        attrs={'placeholder': 'Укажите время', "style": "border-radius: 6px; border:1px solid; margin-bottom: 2%; box-shadow: inset 0 0 4px rgba(0, 0, 0, 0.2)"}),
        required=True)
    sum = forms.IntegerField(label="", widget=forms.NumberInput(
        attrs={'placeholder': "Укажите сумму", "style": "border-radius: 6px; border:1px solid; margin-bottom: 2%; box-shadow: inset 0 0 4px rgba(0, 0, 0, 0.2)"}), required=True)
    transaction_type = forms.ChoiceField(
        choices=CATEGORIES, initial=True, widget=forms.Select(), required=True)

    class Meta:
        model = Transaction
        fields = ['uid', 'sum', 'transaction_type',
                  'category_id', 'date', 'time', 'comment']
