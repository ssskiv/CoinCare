from django import forms

from django.conf import settings

from django.utils.translation import gettext as _
from .models import Transaction
from django.contrib.admin.widgets import AdminDateWidget, AdminTimeWidget

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
    for i in range(2100,1899,-1):
        years_choices.append(str(i))
    date=forms.DateField(label= "Дата", widget=AdminDateWidget(attrs={'placeholder':"Введите дату"}),required=True)
    comment = forms.CharField(label= "Комменатрий", required=False, widget=forms.TextInput(attrs={"placeholder":"Добавьте комментарий"})) 
    uid=forms.IntegerField(label= "ID пользователя", widget=forms.HiddenInput(), required=False)
    time=forms.TimeField(label= "Время", widget=AdminTimeWidget(
                                                attrs={'placeholder':'Укажите время'}),
                                                required=True)
    sum=forms.IntegerField(label="", widget=forms.NumberInput(attrs={'placeholder': "Укажите сумму"}),required=True)
    #category_id=forms.ChoiceField(widget=forms.choic())

    
    class Meta:
        model = Transaction
        fields = ['uid','sum','transaction_type','category_id','date','time','comment']