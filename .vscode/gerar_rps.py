import subprocess
import pyautogui
import time
import pyperclip

pyautogui.PAUSE = 0.15


def gerar_rps():
    banco = (352, 532)
    funcionario = (677, 627)
    confirmar = (1050, 190)
    tomador = (306, 220)
    forma = (469, 223)
    pix = (880, 401)
    tipo_local = (643, 254)
    imprimir = (1052, 411)
    rps_local = (377, 134)
    contrato_local = (670, 132)

    open_siac_rps()
    time.sleep(1)
    pyautogui.click(295, 31)
    pyautogui.click(329, 75)
    pyautogui.click(314, 101)
    time.sleep(30)
    pyautogui.click(377, 134)
    pyautogui.hotkey('ctrl', 'c')
    rps = pyperclip.paste()
    with open("geral.txt", "r") as file:
        for line in file:
            value = line.split('|')
            contrato = value[0]
            v_dia = value[5]
            v_mes = value[6]
            v_ano = value[7]
            valor = value[11]
            total = value[12]
            condicao = value[13]

            if int(condicao) == 0:
                rps = int(rps) + 1
                pyautogui.write(str(rps))
                pyautogui.press('enter')
                pyautogui.write(contrato)
                pyautogui.press('enter')
                pyautogui.click(*banco)
                pyautogui.press('2')
                pyautogui.press('2')
                pyautogui.press('2')
                pyautogui.press('enter')
                pyautogui.press('1')
                pyautogui.press('up')
                pyautogui.press('enter')
                pyautogui.press('0')
                pyautogui.press('3')
                pyautogui.click(*funcionario)
                pyautogui.press('c')
                pyautogui.press('enter')
                pyautogui.press('enter')
                pyautogui.press('enter')
                time.sleep(0.3)
                pyautogui.click(*tipo_local)
                pyautogui.press('g')
                pyautogui.press('enter')
                pyautogui.press('enter')
                pyautogui.write('22')
                pyautogui.press('enter')
                pyautogui.write('{}{}{}'.format(v_dia, v_mes, v_ano))
                pyautogui.press('enter')
                pyautogui.press('enter')
                pyautogui.write(valor)
                pyautogui.click(*confirmar)
                pyautogui.press('enter')
                pyautogui.click(*forma)
                pyautogui.click(*pix)
                pyautogui.write(valor)
                pyautogui.click(*confirmar)
                pyautogui.press('enter')
                pyautogui.click(*imprimir)
                pyautogui.press('s')
                pyautogui.press('down')
                pyautogui.press('enter')
                pyautogui.press('enter')
                time.sleep(1)
                pyautogui.press('enter')
                time.sleep(1)
                pyautogui.click(*tomador)
                time.sleep(1)
                pyautogui.click(*contrato_local)
                pyautogui.click(*rps_local)

            elif int(condicao) == 1:
                rps = int(rps) + 1
                pyautogui.write(str(rps))
                pyautogui.press('enter')
                pyautogui.write(contrato)
                pyautogui.press('enter')
                pyautogui.click(*banco)
                pyautogui.press('2')
                pyautogui.press('2')
                pyautogui.press('2')
                pyautogui.press('enter')
                pyautogui.press('1')
                pyautogui.press('up')
                pyautogui.press('enter')
                pyautogui.press('0')
                pyautogui.press('3')
                pyautogui.click(*funcionario)
                pyautogui.press('c')
                pyautogui.press('enter')
                pyautogui.press('enter')
                pyautogui.press('enter')
                time.sleep(0.3)
                pyautogui.click(*tipo_local)
                pyautogui.press('g')
                pyautogui.press('enter')
                pyautogui.press('enter')
                pyautogui.write('22')
                pyautogui.press('enter')
                pyautogui.write('{}{}{}'.format(v_dia, v_mes, v_ano))
                pyautogui.press('enter')
                pyautogui.press('enter')
                pyautogui.write(valor)
                pyautogui.press('enter')

            elif int(condicao) == 2:
                pyautogui.write('22')
                pyautogui.press('enter')
                pyautogui.write('{}{}{}'.format(v_dia, v_mes, v_ano))
                pyautogui.press('enter')
                pyautogui.press('enter')
                pyautogui.write(valor)
                pyautogui.press('enter')

            elif int(condicao) == 3:
                pyautogui.press('g')
                pyautogui.press('enter')
                pyautogui.press('enter')
                pyautogui.write('22')
                pyautogui.press('enter')
                pyautogui.write('{}{}{}'.format(v_dia, v_mes, v_ano))
                pyautogui.press('enter')
                pyautogui.press('enter')
                pyautogui.write(valor)
                pyautogui.click(*confirmar)
                pyautogui.press('enter')
                pyautogui.click(*forma)
                pyautogui.click(*pix)
                pyautogui.write(total)
                pyautogui.click(*confirmar)
                pyautogui.press('enter')
                pyautogui.click(*imprimir)
                pyautogui.press('s')
                pyautogui.press('down')
                pyautogui.press('enter')
                pyautogui.press('enter')
                time.sleep(1)
                pyautogui.press('enter')
                time.sleep(1)
                pyautogui.click(*tomador)
                time.sleep(1)
                pyautogui.click(*contrato_local)
                pyautogui.click(*rps_local)

            else:
                print('ok')


def open_siac_rps():
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
    gerar_rps()
