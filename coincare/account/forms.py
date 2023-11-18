from django import forms

from django.conf import settings

from django.utils.translation import gettext as _
from .models import Transaction

class TransactionForm(forms.ModelForm):
    date_formats=[
                '%Y-%m-%d',      # '2006-10-25'
                '%m/%d/%Y',       # '10/25/2006'
                '%m/%d/%y'         # '10/25/06'
                ]      
    time_formats=[
                "%H:%M:%S",  # '14:30:59'
                "%H:%M:%S.%f",  # '14:30:59.000200'
                "%H:%M",  # '14:30'
                ]
    years_choices=[]
    month_choices= {
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
    day_choices=[]
    for i in range(1900,2101):
        years_choices.append(str(i))
    date=forms.DateField(widget=forms.SelectDateWidget(years=years_choices, months=month_choices),required=True)
    comment = forms.CharField(required=False)# hh:mm
    uid=forms.IntegerField(widget=forms.HiddenInput(), required=False)
    time=forms.TimeField(widget=forms.TimeInput(
                                                #input_formats=time_formats,
                                                attrs={'placeholder':'hh:mm'}),
                                                required=True)
    
    class Meta:
        model = Transaction
        fields = ['uid','sum','transaction_type','category_id','date','time','comment']