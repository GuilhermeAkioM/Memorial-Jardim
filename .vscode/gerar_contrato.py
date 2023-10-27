import subprocess
import time

import pyautogui

pyautogui.PAUSE = 0.3


def recibo():
    numero_recibo = int(input('recibo: '))
    open_siac_contrato()
    time.sleep(1)
    pyautogui.click(295, 31)
    pyautogui.click(326, 158)
    with open("geral.txt", "r") as file:
        for line in file:
            contrato = line.split('|')[0]
            x = line.split('|')[3]
            y = line.split('|')[4]
            vdia = line.split('|')[5]
            vmes = line.split('|')[6]
            vano = line.split('|')[7]
            dia = line.split('|')[8]
            mes = line.split('|')[9]
            ano = line.split('|')[10]
            valort = line.split('|')[12]

            linha = (464, 325)
            funcionario = (399, 578)
            banco = (393, 641)
            formas = (344, 220)
            pix = (786, 450)
            cliente = (234, 223)
            recibo_local = (300, 166)
            l_carregar_titulos = (928,259)
            pyautogui.write(str(numero_recibo))
            pyautogui.press('enter')
            pyautogui.write('{}{}{}'.format(dia, mes, ano))
            pyautogui.press('enter')
            pyautogui.write(contrato)
            pyautogui.click(*linha)
            pyautogui.write('PARCELA: {}/{}'.format(x, y))
            pyautogui.press('enter')
            pyautogui.write('VENCIMENTO: {}/{}/{}'.format(vdia, vmes, vano))
            pyautogui.press('enter')
            pyautogui.write('TRANSFERÊNCIA BANCÁRIA')
            pyautogui.click(*funcionario)
            pyautogui.press('c')
            pyautogui.press('enter')
            pyautogui.press('enter')
            pyautogui.press('enter')
            pyautogui.click(*l_carregar_titulos)
            pyautogui.click(*banco)
            pyautogui.press('2')
            pyautogui.press('2')
            pyautogui.press('2')
            pyautogui.press('enter')
            pyautogui.press('1')
            pyautogui.press('up')
            pyautogui.press('enter')
            pyautogui.press('3')
            pyautogui.press('enter')
            pyautogui.press('enter')
            pyautogui.press('enter')
            pyautogui.click(*formas)
            pyautogui.click(*pix)
            pyautogui.write(valort)
            pyautogui.press('enter')
            pyautogui.press('enter')
            pyautogui.press('enter')
            pyautogui.click(*cliente)
            pyautogui.click(*recibo_local)
            numero_recibo = int(numero_recibo + 1)


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


if __name__ == '__main__':
    recibo()
