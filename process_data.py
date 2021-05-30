from pathlib import Path
from datetime import datetime
import csv
"""
Дополнительное задание.

В папке data вы найдее несколько файлов с составами фондов в формате .csv
Каждая строка это ценная бумага/торговый инструмент, столбец weight это какой процент от всего фонда занимает эта бумага

Нужно вывести в консоль:
1. Название фонда
2. Дата отчета (подсказка, дата отчета содержится в конце названия файла, например 21052021)
3. Вывести для каждого отчета 10 самых крупных компонентов (Отсортировать по weight)
4. Полностью ли заполнен фаил (сумма весов в каждом файле равна 100%)

Потом:
Сохранить все отчеты в 1 фаил top_ten_report.csv:
1. Нужны только 10 крупнейших компонентов
2. Если для фонда есть более свежие данные, старые данные не сохранять в финальный отчет
4. Столбцы: date, fund_name, currency, weight

Подсказка/вариант как получить имена всех файлов.
from pathlib import Path

reports = Path('./data').glob('*.csv')
for file in reports:
    print(report.name)
"""
def file_data(file_name):
    file_date = datetime.strptime(file_name, '%d%m%Y')
    return file_date.strftime('%d %m %Y')

def weight_to_float(item):
    item = item['Weight']
    item = item.replace('%', '')
    item = float(item.replace(',', '.'))
    return item
    
def process_data() -> None:
    reports = Path('./data').glob('*.csv')
    for file in reports:
        file_name = file.name
        file_name = file_name[:-4]
        file_name = file_name.split('_')
        print(f'Название фонда: "{file_name[0]} {file_name[1]}" Дата: {file_data(file_name[-1])}')

        
        with open ('./data/'+file.name, 'r', encoding='utf-8') as file:

            reader = csv.DictReader(file, delimiter = ',')
            

            # titles = file.readline() 
            # titles = titles.replace('\n', '')
            # titles = titles.split(',')
            
            
            # if len(titles) == 5:
            #     fields = [titles[0],titles[1],titles[2],titles[3],titles[4]]
            # else:
            #     fields = [titles[0],titles[1],titles[2],titles[3]]
            

            # reader = csv.DictReader(file, fields, delimiter = ',')
            reader = sorted(reader, key = weight_to_float, reverse = True)
            print('Топ 10 самых крупных компонентов фонда:')
            for row in range(1, 11):
                try:
                    print(reader[row]['Weight'])
                except(IndexError):
                    break

            sum_weight_str = list(i for i in reader)
            sum_weight = sum(map(weight_to_float, sum_weight_str))
            print(f"Фаил заполнен на {round(sum_weight, 2)}%")
            print()
        
if __name__ == '__main__':
    process_data()