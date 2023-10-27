import xlrd
import openpyxl

def verificar_e_copiar(workbook, nome, pagou_workbook):
    for sheet in workbook.sheet_names():
        planilha = workbook.sheet_by_name(sheet)
        for row_num in range(planilha.nrows):
            row = planilha.row_values(row_num)
            if nome in row:
                pagou_planilha = pagou_workbook["pago"]
                pagou_planilha.append(row)

caminhos_arquivos = ["planilha1.xls", "planilha2.xls", "planilha3.xls"]

try:
    pagou_workbook = openpyxl.load_workbook("pagou.xlsx")
except FileNotFoundError:
    pagou_workbook = openpyxl.Workbook()
    pagou_workbook.active.title = "pago"
    pagou_workbook.save("pagou.xlsx")

nomes_no_pagou = []
with open('tarifa.txt', 'r') as file:
    for line in file:
        nome = line.split('|')[0]
        nomes_no_pagou.append(nome)

for nome in nomes_no_pagou:
    for caminho in caminhos_arquivos:
        workbook = xlrd.open_workbook(caminho)
        verificar_e_copiar(workbook, nome, pagou_workbook)
pagou_workbook.save("pagou.xlsx")
