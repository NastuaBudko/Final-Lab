# -*- coding: utf-8 -*-
from prettytable import PrettyTable

th = ['Код віду основніх засобів', 'Вид основніх засобів']
td = ['1', 'Будівлі',
      '2','Машини та обладнання',
      '3', 'Транспортні засоби',
      '4', 'Інструмент та інвентар',]

colums = len(th)
table = PrettyTable(th)

td_data = td[:]

while td_data:
    table.add_row(td_data[:colums])
    td_data = td_data[colums:]

print(table)
