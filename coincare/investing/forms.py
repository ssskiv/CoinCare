from django import forms
from .models import Trade
from django.utils.translation import gettext as _
from django.contrib.admin.widgets import AdminDateWidget, AdminTimeWidget


class TradeForm(forms.ModelForm):

    CATEGORIES = (
        (False, 'Покупка'),
        (True, 'Продажа')
    )

    quantity = forms.IntegerField(widget=forms.NumberInput(
        attrs={'placeholder': 'Введите количество акций', "style": "border-radius: 6px; border:1px solid; margin-bottom: 2%; height: 200%; box-shadow: inset 0 0 4px rgba(0, 0, 0, 0.2)"}))
    trade_type = forms.ChoiceField(
        choices=CATEGORIES, initial=False, widget=forms.Select(attrs={'placeholder': 'Введите тип сделки', "style": "border-radius: 6px; border:1px solid; margin-bottom: 2%; height: 150%; box-shadow: inset 0 0 4px rgba(0, 0, 0, 0.2)"}), required=True)
    uid = forms.IntegerField(widget=forms.HiddenInput(), required=False)
    token = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'Введите токен', "style": "border-radius: 6px; border:1px solid; margin-bottom: 2%; height: 150%; box-shadow: inset 0 0 4px rgba(0, 0, 0, 0.2)"}))
    date = forms.DateField(widget=AdminDateWidget(
        attrs={'placeholder': 'Введите дату', "style": "border-radius: 6px; border:1px solid; margin-bottom: 2%; height: 150%; box-shadow: inset 0 0 4px rgba(0, 0, 0, 0.2)"}), required=True)
    time = forms.TimeField(widget=AdminTimeWidget(
        # input_formats=time_formats,
        attrs={'placeholder': 'Укажите время', "style": "border-radius: 6px; border:1px solid; margin-bottom: 2%; height: 150%; box-shadow: inset 0 0 4px rgba(0, 0, 0, 0.2)"}),
        required=True)
    trade_price = forms.FloatField(widget=forms.HiddenInput(), required=False)
    # trade_type=forms.BooleanField(label='Тип сделки',widget=forms.CheckboxInput(),required=False)

    class Meta:
        model = Trade
        fields = ['uid', 'trade_type', 'token',
                  'quantity', 'date', 'time', 'trade_price']
