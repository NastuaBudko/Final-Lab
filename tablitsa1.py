# -*- coding: utf-8 -*-
from prettytable import PrettyTable

th = ['Підприємство', 'Код виду основніх засобів', 'Залишок на 1.01.2018', 'Надійшло у 2018', 'Вибуток у 2018']
td = ['Універсам 22', '1', '44 048,00', '500,00', '200,00',
      'Дніпрянка   ', '1', '22 456,00', '365,00', '123,00',
      'Універсам 22', '2', '5 564,00', '2 751,00', '135,00',
      'Дніпрянка   ', '2', '10 087,00', '15 972,00', '135,00',
      'Універсам 22', '3', '0,00', '0,00', '0,00',
      'Дніпрянка   ', '3', '206,00', '34,00', '50,00',
      'Універсам 22', '4', '116,00', '64,00', '23,00',
      'Дніпрянка   ', '4', '34,00', '23,00', '25,00',]

colums = len(th)
table = PrettyTable(th)

td_data = td[:]

while td_data:
    table.add_row(td_data[:colums])
    td_data = td_data[colums:]

print(table)
