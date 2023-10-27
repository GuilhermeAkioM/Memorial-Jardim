import subprocess
import time
import pyautogui

pyautogui.PAUSE = 0.2


def conciliar():
    data = input("data: ")
    mov_inicial = int(input("mov inicial: "))
    mov_final = int(input("mov final: "))
    open_siac_invoiced()
    open_banking_movement()
    for num in range(mov_inicial, mov_final + 1):
        pyautogui.write(str(num))
        pyautogui.press('enter')
        pyautogui.write(data)
        pyautogui.press('enter')
        pyautogui.press('enter')
        pyautogui.press('enter')
        pyautogui.press('s')
        pyautogui.press('enter')
        pyautogui.write(data)
        pyautogui.doubleClick(996, 195)
        pyautogui.press('enter')
        time.sleep(0.2)


def conciliar_sem_alterar():
    data = input("data: ")
    mov_inicial = int(input("mov inicial: "))
    mov_final = int(input("mov final: "))
    open_siac_invoiced()
    open_banking_movement()
    for num in range(mov_inicial, mov_final + 1):
        pyautogui.write(str(num))
        pyautogui.press('enter')
        pyautogui.press('enter')
        pyautogui.press('enter')
        pyautogui.press('enter')
        pyautogui.press('s')
        pyautogui.press('enter')
        pyautogui.write(data)
        pyautogui.doubleClick(996, 195)
        pyautogui.press('enter')
        time.sleep(0.2)


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
    answer = input('''Escolha um número:
    1 - conciliar com alteração da data
    2 - consiliar sem alteração da data
    ''')
    if int(answer) == 1:
        conciliar()
    elif int(answer) == 2:
        conciliar_sem_alterar()
    else:
        print('Invalido!!!')
