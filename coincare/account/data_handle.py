import pandas as pd


class DataHandle():
    count = 0
    sum = 0
    html='TABLE HERE'
    def __init__(self, transactions) -> None:
        if transactions != None:
            data = []
            for item in transactions:
                a = []
                a.append(item.transaction_type)
                a.append(item.sum)
                a.append(item.category_id)
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
                                   'tr_type', 'sum', 'cat_id', 'date', 'time', 'comment'])
            
            self.html=pd.DataFrame(data=data, columns=['Тип транзакции', 'Сумма','Категория','Дата','Время','Комментарий']
                                   ).to_html(classes='',)
