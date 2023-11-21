import pandas as pd
import requests
import json
from datetime import date


import pandas as pd
from .models import Trade
from datetime import date
import time
import plotly as plt
import plotly.express as px
from plotly.offline import plot
from plotly.graph_objs import Scatter, Bar
from django.contrib import messages
from plotly.subplots import make_subplots

class TradesHandle():
    key='G0DBWYM63WEJLTIG'#API KEY  IOGRGGJFMMTXXGOP
    count = 0
    sum = 0
    html = 'TABLE HERE'
    plots = []
    barplot = None
    lineplot = None
    pieplot=None
    cfplot=[]
    request = None
    full_html='TABLE HERE'

    def __init__(self, request, trades) -> None:
        self.request = request
        if trades != None:
            data = []
            for item in trades:
                a = []
                a.append(item.trade_type)
                a.append(item.token)
                a.append(int(item.quantity))
                a.append(item.date)
                a.append(item.time)
                a.append(item.trade_price)
                a.append(self.get_price(item.token))
                a.append(item.trade_price*item.quantity)
                a.append(float(a[-2])*item.quantity)
                if int(a[-2])!=0:
                    data.append(a)
                else:
                    continue
                self.count += 1
            self.df = pd.DataFrame(data=data, columns=[
                'Тип сделки', 'Токен', 'Количество', 'Дата', 'Время', 'Цена при сделке', 'Цена сейчас','Стоимость при покупке','Стоимость сейчас']
            ).sort_values(by=['Дата', 'Время'], ascending=False)
            df = self.df
            
            df['Тип сделки'] = df.apply(
                lambda x: 'Продажа' if x['Тип сделки'] else 'Покупка', axis=1)
            self.html = df.head(5).to_html(classes='table', index=False)
            self.full_html=df.to_html(classes='table', index=False)
    def get_price(self, token):
        today = date.today().day-2
        year = date.today().year
        month = date.today().month

        #url = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={token}&apikey={self.key}'
        url = f'http://iss.moex.com/iss/engines/stock/markets/shares/securities/{token}/candles.json?from={year}-{month}-{today}&interval=24'
        r = requests.get(url)
        data = r.json()['candles']['data']
        if len(data)>0:
            price = data[0][1]
         
            return price
        else:
            return -1
    
    def generate_plots(self):
        df = self.df

        today = date.today().day-2
        year = date.today().year
        month = date.today().month
        data1=df[df['Тип сделки']=='Покупка']
        data1.groupby('Токен')['Стоимость при покупке'].mean()
        if not data1.empty:
            self.barplot=plot(px.histogram(data1, x='Токен', y='Стоимость при покупке', barmode='group'),output_type='div')
            self.pieplot=plot(px.pie(data1, names = 'Токен', values = 'Стоимость при покупке'),output_type='div')
            tokens = pd.unique(data1['Токен'])
            plots=[]
            for o in tokens:
                j = requests.get(f'http://iss.moex.com/iss/engines/stock/markets/shares/securities/{o}/candles.json?from={year-1}-{month}-{today}&till={year}-{month}-{today}&interval=24')
                j.encoding='utf-8'
                #j=j.content.encode('ascii','ignore')
                #j=j.decode()
                messages.info(self.request, j)
                j=json.loads(j.text)

                if len(j['candles']['data'])>0:
                    data = [{k : r[i] for i, k in enumerate(j['candles']['columns'])} for r in j['candles']['data']]
                    frame = pd.DataFrame(data)
                    fig=px.line(list(frame['close'])).update_traces(showlegend=False)
                    fig.update_xaxes(title_text = '')
                    fig.update_yaxes(title_text = f' {str(o)}')
                    plots.append(plot(fig,output_type='div'))
            self.cfplot=plots
                
            
            #self.cfplot=plot(px.pie(data1, names = 'Токен', values = 'Стоимость сейчас'),output_type='div')
            #j = requests.get(f'http://iss.moex.com/iss/engines/stock/markets/shares/securities/{token}/candles.json?from={year-1}-{month}-{today}&till={year}-{month}-{today}&interval=24').json()

    