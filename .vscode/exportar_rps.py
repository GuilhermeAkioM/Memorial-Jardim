import pyautogui
import time
import subprocess

pyautogui.PAUSE = 0.3


def export():
    open_siac_invoiced
    open_banking_movement
    with open("geral.txt", "r") as file:
        for line in file:
            rps = line.split('|')[1]
            siac = (95, 220)
            confirmar = (1059, 129)
            movimentar = (1104, 440)
            pyautogui.write(rps)
            pyautogui.press('enter')
            pyautogui.click(*siac)
            time.sleep(0.5)
            pyautogui.click(172, 540)
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
            pyautogui.click(*confirmar)
            pyautogui.press('enter')
            pyautogui.click(*movimentar)
            pyautogui.press('enter')
            time.sleep(1.5)
        

def open_banking_movement():
    location_movimentacao = (108, 31)
    location_sub_movimentacao = (116, 54)
    pyautogui.click(*location_movimentacao)
    pyautogui.click(*location_sub_movimentacao)


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


if __name__ == "__main__":
    export()
