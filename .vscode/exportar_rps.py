import pyautogui
import time
import subprocess

pyautogui.PAUSE = 0.1


def export():
    open_siac_receive()
    time.sleep(1)
    open_banking_movement()
    time.sleep(1)
    with open("geral.txt", "r") as file:
        for line in file:
            rps = line.split('|')[1]
            l_rps = (359, 129)
            l_confirmar = (1056, 129)
            l_movimentar = (1076, 436)
            l_banco = (364, 533)
            l_servico = (283, 212)
            l_contrato = (708, 130)
            pyautogui.write(rps)
            pyautogui.press('enter')
            time.sleep(0.5)
            pyautogui.click(*l_banco)
            pyautogui.press("0")
            pyautogui.press("2")
            pyautogui.press("2")
            pyautogui.press("2")
            pyautogui.press("enter")
            pyautogui.press("0")
            pyautogui.press("1")
            pyautogui.press("up")
            pyautogui.press("enter")
            pyautogui.press("0")
            pyautogui.press("3")
            pyautogui.press("enter")
            pyautogui.click(*l_confirmar)
            pyautogui.press('enter')
            pyautogui.click(*l_movimentar)
            pyautogui.press('enter')
            time.sleep(1.5)
            pyautogui.click(*l_servico)
            pyautogui.click(*l_contrato)
            pyautogui.click(*l_rps)


def open_banking_movement():
    l_especiais = (599, 32)
    l_rps = (645, 100)
    pyautogui.click(*l_especiais)
    pyautogui.click(*l_rps)


def open_siac_receive():
    # Caminho para o arquivo executável do aplicativo
    trajectory_invoiced = r'C:\Program Files (x86)\SIAC - Sist. Integrado Adm. Cemitério\UUMNUMBRCE01.exe'

    try:
        # Abre o aplicativo usando o caminho especificado
        subprocess.Popen(trajectory_invoiced)
    except FileNotFoundError:
        print("O arquivo do siac não foi encontrado.")
    except Exception as e:
        print(f"Ocorreu um erro ao abrir o siac: {e}")


if __name__ == "__main__":
    export()
