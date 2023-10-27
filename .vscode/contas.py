import subprocess
import pyautogui
import time

pyautogui.PAUSE = 0.2


def ticket():
    open_siac_tax()
    time.sleep(1)
    l_movimentacao = (206, 33)
    l_baixa = (184, 80)
    l_ok = (1021, 166)
    pyautogui.click(l_movimentacao)
    pyautogui.click(l_baixa)
    with open('geral.txt', 'r') as arquivo:
        for linha in arquivo:
            valor = linha.split('|')[-2]
            parcela = linha.split('|')[-3]
            registro = linha.split('|')[-5]
            data = linha.split('|')[2]
            pyautogui.write(registro)
            pyautogui.press('enter')
            pyautogui.write(parcela)
            time.sleep(0.2)
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
    ticket()
