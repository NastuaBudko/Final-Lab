# -*- coding: utf-8 -*-
import xlsxwriter

workbook = xlsxwriter.Workbook('Excel_tablitsa1.xlsx')

worksheet = workbook.add_format({'bold': True})

worksheet.write('A1', 'Код', bold)
Sworksheet.write('B1', 'Вид основніх засобів', bold)


bold.set_align('center')

enterprise = (
              ['1', 'Будівлі'],
              ['2','Машини та обладнання'],
              ['3', 'Транспортні засоби'],
              ['4', 'Інструмент та інвентар'],
)

worksheet.set_column(0, 2, 20)

for i, (code,type) in enumerate (types, start=2):
    worksheet.write(f'A{i}', code)
    worksheet.write(f'B{i}', type)


workbook.close()
