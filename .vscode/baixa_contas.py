import subprocess
import time
import pyautogui

pyautogui.PAUSE = 0.2


def baixa():
    res_inicial = input("Escreva o registro inicial: ")
    open_siac_tax()
    time.sleep(1)
    l_movimentacao = (206, 33)
    l_baixa = (184, 80)
    l_ok = (1021, 166)
    pyautogui.click(l_movimentacao)
    pyautogui.click(l_baixa)
    with open('geral.txt', 'r') as file:
        for line in file:
            data = line.split('|')[0]
            valor = line.split('|')[1]
            pyautogui.write(str(res_inicial))
            pyautogui.press('enter')
            pyautogui.press('enter')
            pyautogui.press('enter')
            pyautogui.press('enter')
            pyautogui.press('enter')
            pyautogui.write(data)
            pyautogui.press('enter')
            pyautogui.press('enter')
            pyautogui.press('enter')
            pyautogui.write(valor)
            pyautogui.doubleClick(*l_ok)
            pyautogui.press('enter')
            res_inicial = int(res_inicial)
            res_inicial = res_inicial + 1


def open_siac_tax():
    # Caminho para o arquivo executável do aplicativo
    trajectory_tax = r'C:\Program Files (x86)\SIAC - Sist. Integrado Adm. Cemitério\UUMNUMBRCE03.exe'

    try:
        # Abre o aplicativo usando o caminho especificado
        subprocess.Popen(trajectory_tax)
    except FileNotFoundError:
        print("O arquivo do siac não foi encontrado.")
    except Exception as e:
        print(f"Ocorreu um erro ao abrir o siac: {e}")


if __name__ == '__main__':
    baixa()
