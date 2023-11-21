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
        attrs={'placeholder': "Введите дату"}), required=True)
    comment = forms.CharField(label="Комменатрий", required=False, widget=forms.TextInput(
        attrs={"placeholder": "Добавьте комментарий"}))
    uid = forms.IntegerField(label="ID пользователя",
                             widget=forms.HiddenInput(), required=False)
    time = forms.TimeField(label="Время", widget=AdminTimeWidget(
        attrs={'placeholder': 'Укажите время'}),
        required=True)
    sum = forms.IntegerField(label="", widget=forms.NumberInput(
        attrs={'placeholder': "Укажите сумму"}), required=True)
    transaction_type = forms.ChoiceField(
        choices=CATEGORIES, initial=True, widget=forms.Select(), required=True)

    class Meta:
        model = Transaction
        fields = ['uid', 'sum', 'transaction_type',
                  'category_id', 'date', 'time', 'comment']
