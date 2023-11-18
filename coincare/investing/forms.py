from django import forms
from .models import Trade
from django.utils.translation import gettext as _


class TradeForm(forms.ModelForm):
    years_choices=[]
    month_choices = {
        1: _("jan"),
        2: _("feb"),
        3: _("mar"),
        4: _("apr"),
        5: _("may"),
        6: _("jun"),
        7: _("jul"),
        8: _("aug"),
        9: _("sep"),
        10: _("oct"),
        11: _("nov"),
        12: _("dec"),
    }
    for i in range(2100, 1899, -1):
        years_choices.append(str(i))

    quantity = forms.IntegerField(widget=forms.NumberInput())
    uid = forms.IntegerField(widget=forms.HiddenInput(), required=False)
    token= forms.CharField(widget=forms.TextInput())
    date = forms.DateField(widget=forms.SelectDateWidget(
        years=years_choices, months=month_choices), required=True)
    time = forms.TimeField(widget=forms.TimeInput(
        # input_formats=time_formats,
        attrs={'placeholder': 'hh:mm'}),
        required=True)

    class Meta:
        model = Trade
        fields = ['uid', 'trade_type', 'token', 'quantity', 'date', 'time']
