import pyautogui
import time
import subprocess
import pyperclip
from unidecode import unidecode

pyautogui.PAUSE = 0.05


def invoiced():
    print('''
    ***************************
    *** LEIA A DOCUMENTAÇÃO ***
    ***************************
    ''')

    answer = input('(s/n) Quer colocar a data? ')

    if answer == 's':
        date = input('data: ')
    elif answer == 'n':
        print("ok :) ")
    else:
        print('invalido!')

    open_siac_invoiced()
    time.sleep(1)
    open_banking_movement()
    sequential = pay_sequential()

    with open('geral.txt', 'r') as file:
        for line in file:
            values = line.strip().split('|')

            if answer == 's':
                date = date     # foi só pro amarelo sumir
                monetary = values[0]
                modality = values[1]
                company = values[2]

            else:
                date = values[0]
                monetary = values[1]
                modality = values[2]
                company = values[3]


            # acrescenta 1
            sequential = change_sequential(sequential)
            pyautogui.write(str(sequential))
            pyautogui.press("enter")
            time.sleep(0.15)
            pyautogui.write(date)
            pyautogui.press("enter")
            time.sleep(0.15)
            if str(company) == '1':
                pyautogui.press("d")
            else:
                pyautogui.press("c")
            pyautogui.press("enter")
            pyautogui.press("enter")
            pyautogui.press("s")
            pyautogui.press("enter")
            pyautogui.write(date)
            pyautogui.press("enter")
            pyautogui.press("2")
            pyautogui.press("2")
            pyautogui.press("2")
            pyautogui.press("enter")
            pyautogui.press("1")
            pyautogui.press("up")
            pyautogui.press("enter")
            pyautogui.press("3")
            pyautogui.press("enter")
            pyautogui.press("enter")
            pyautogui.press("enter")
            pyautogui.press("enter")
            pyautogui.write(monetary)
            pyautogui.press("enter")
            pyautogui.press("enter")
            pyautogui.press("enter")
            pyautogui.press("enter")
            pyautogui.press("enter")
            pyautogui.press("enter")
            pyautogui.press("enter")
            pyautogui.write("1")
            pyautogui.press("enter")
            if str(company) == '1':
                pyautogui.write("APLIC. INVEST FACIL")
            elif str(company) == '2':
                pyautogui.write("RESGATE INVEST FACIL")
            else:
                pyautogui.write("REF. FATURAMENTO CARTAO {} {}".format(company.upper(), unidecode(modality.upper())))
            pyautogui.press("enter")
            pyautogui.press("enter")
            pyautogui.press("enter")
            pyautogui.press("enter")
            pyautogui.press("enter")
            pyautogui.press("enter")
            pyautogui.press("c")
            pyautogui.press("enter")
            pyautogui.press("enter")
            pyautogui.press("enter")
            pyautogui.press("enter")
            pyautogui.press("enter")

            if valid_company(company):
                pyautogui.write("404")
            else:
                pyautogui.write("1796")

            pyautogui.press("enter")

            if valid_company(company):
                pyautogui.write("INVEST PLUS BRADESCO")
            else:
                pyautogui.write("REDECARD SA")

            pyautogui.press("enter")
            pyautogui.press("enter")
            pyautogui.press("enter")
            time.sleep(0.1)


def pay_sequential():
    sequential = pyperclip.paste()
    return sequential


def open_siac_invoiced():
    # Caminho para o arquivo executável do aplicativo
    trajectory_invoiced = r'C:\Program Files (x86)\SIAC - Sist. Integrado Adm. Cemitério\UUMNUMBRCE07.exe'

    try:
        # Abre o aplicativo usando o caminho especificado
        subprocess.Popen(trajectory_invoiced)
    except FileNotFoundError:
        print("O arquivo do siac não foi encontrado.")
    except Exception as e:
        print(f"Ocorreu um erro ao abrir o siac: {e}")


def open_banking_movement():
    location_movimentacao = (108, 31)
    location_sub_movimentacao = (116, 54)
    location_sequencial = (385, 207)
    button_last_sequential = (364, 166)
    pyautogui.click(*location_movimentacao)
    pyautogui.click(*location_sub_movimentacao)
    pyautogui.click(*button_last_sequential)
    time.sleep(20)
    pyautogui.click(*location_sequencial)
    pyautogui.hotkey('ctrl', 'c')


def change_sequential(sequential):
    sequential = int(sequential)
    sequential = sequential + 1
    return sequential


def valid_company(company):
    return company in ['1', '2']


if __name__ == '__main__':
    invoiced()
