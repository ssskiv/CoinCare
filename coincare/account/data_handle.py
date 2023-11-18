import pandas as pd

from .models import Transaction

from datetime import date
import time

import plotly as plt
import plotly.express as px
from plotly.offline import plot
from plotly.graph_objs import Scatter, Bar

from django.contrib import messages


class DataHandle():
    count = 0
    sum = 0
    html = 'TABLE HERE'
    plots = []
    request = None


    def __init__(self, request, transactions) -> None:
        self.request = request
        if transactions != None:
            data = []
            for item in transactions:
                a = []
                a.append(item.transaction_type)
                a.append(item.sum)
                a.append(int(item.category_id))
                a.append(item.date)
                a.append(item.time)
                a.append(item.comment)
                data.append(a)
                self.count += 1
                if item.transaction_type == True:
                    self.sum += item.sum
                else:
                    self.sum -= item.sum
            self.df = pd.DataFrame(data=data, columns=[
                'Тип транзакции', 'Сумма', 'Категория', 'Дата', 'Время', 'Комментарий']
            ).sort_values(by=['Дата', 'Время'], ascending=False)
            df = pd.DataFrame(data=data, columns=['Тип транзакции', 'Сумма', 'Категория', 'Дата', 'Время', 'Комментарий']
                              ).sort_values(by=['Дата', 'Время'], ascending=False).head(5)

            # df['Категория'] = df['Категория'].to_string()
            df['Тип транзакции'] = df.apply(
                lambda x: 'Начисление' if x['Тип транзакции'] else 'Списание', axis=1)
            df['Категория'] = df.apply(
                func=(lambda x: Transaction.Categories(int(x['Категория'])).label), axis=1)
            # ВОТ ТУТ КЛАССЫ ДЛЯ ТАБЛИЦЫ
            self.html = df.to_html(classes='table', index=False)
            self.generate_plots()

    def generate_plots(self):

        df = self.df
        year = date.today().year
        data1 = df.apply(lambda x: x if str(x['Дата'])[
                         # df[str(df['Дата'])[:4]==year]
                         :4] == str(year) else None, axis=1)
        data1 = data1.dropna()

        months = {
            1:'Январь',
            2:'Февраль',
            3:'Март',
            4:'Апрель',
            5:'Май',
            6:'Июнь',
            7:'Июль',
            8:'Август',
            9:'Сентябрь',
            10:'Октябрь',
            11:'Ноябрь',
            12:'Декабрь',
        }

        if not data1.empty:
            grouped = pd.DataFrame(columns=['Месяц','Сумма', 'Операция'])

            grouped['Месяц'] = data1.apply(lambda x: months[int(str(x['Дата'])[5:7])],axis =1)
            grouped['Сумма']=data1.apply(lambda x: int(x['Сумма']) if x['Тип транзакции'] else -int(x['Сумма']),axis =1 )
            grouped['Операция']=data1.apply(lambda x: "Начисление" if x['Тип транзакции'] else "Списание",axis =1 )
            messages.info(self.request, grouped.to_string())#str(data1.iloc[0,3])[5:7]
            self.plots.append(plot(px.histogram(grouped, x='Месяц', y='Сумма', color='Операция', barmode='group'), output_type='div'))

            pass
