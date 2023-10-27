import subprocess
import time
import pyautogui
import pyperclip
import openpyxl

pyautogui.PAUSE = 0.1


def informacoes():
    data_values = []

    open_siac_contrato()

    with open('comissao.txt', 'r') as file:
        for line in file:
            contrato = line.split('|')[0]
            l_contrato = (221, 32)
            l_locacao = (243, 100)
            l_normal = (241, 53)
            l_numero_contrato = (359, 92)
            l_cond_pagamento = (732, 120)
            l_data = (868, 246)

            mensagem = '''---------------------------
SIAC - Sist. Integrado Adm. Cemitério
---------------------------
Campo Data de Aniversário do Contrato fora da faixa
---------------------------
OK   
---------------------------
'''

            time.sleep(0.5)
            pyautogui.click(*l_contrato)

            if int(contrato) < 1000000:
                pyautogui.click(*l_normal)
            else:
                pyautogui.click(*l_locacao)

            pyautogui.write(contrato)
            pyautogui.press('enter')
            pyautogui.press('enter')
            pyautogui.press('enter')
            pyautogui.hotkey('ctrl', 'c')
            erro = pyperclip.paste()

            if erro in mensagem:
                pyautogui.press('esc')
                pyautogui.click(*l_numero_contrato)
            else:
                pyautogui.click(*l_data)
                pyautogui.hotkey('ctrl', 'c')
                data_venda = pyperclip.paste()
                pyautogui.click(*l_cond_pagamento)
                pyautogui.hotkey('ctrl', 'c')
                valor = pyperclip.paste()
                pyautogui.press('enter')
                pyautogui.hotkey('ctrl', 'c')
                numero_parcela = pyperclip.paste()
                if numero_parcela == "0":
                    parcela = "À VISTA"
                else:
                    parcela = "À PRAZO"
                pyautogui.press('esc')

                data_values.append({
                    'contrato': contrato,
                    'data': data_venda,
                    'valor': valor,
                    'parcela': parcela,
                    'numero_parcela': numero_parcela
                })

    return data_values


def open_siac_contrato():
    # Caminho para o arquivo executável do aplicativo
    trajectory_tax = r'C:\Program Files (x86)\SIAC - Sist. Integrado Adm. Cemitério\UUMNUMBRCE02X.exe'

    try:
        # Abre o aplicativo usando o caminho especificado
        subprocess.Popen(trajectory_tax)
    except FileNotFoundError:
        print("O arquivo do siac não foi encontrado.")
    except Exception as e:
        print(f"Ocorreu um erro ao abrir o siac: {e}")


if __name__ == "__main__":
    data_array = informacoes()

    subprocess.Popen('comissao.xlsx', shell=True)

    workbook = openpyxl.load_workbook('comissao.xlsx')
    sheet = workbook.active

    for data in data_array:
        sheet.append([data['contrato'], data['data'], data['valor'], data['parcela'], data['numero_parcela']])

    workbook.save('comissao.xlsx')
