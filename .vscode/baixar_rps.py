import subprocess
import pyautogui
import time
import pyperclip

pyautogui.PAUSE = 0.1


def rps():
    answer = input('''Escolha um banco: (1/2)
    1. 237|1796|300P
    2. 999|9999|9999
    ''')
    open_geral()
    with open("geral.txt", "r") as file:
        for line in file:
            value = line.split('|')
            contrato = value[0]
            numero_rps = value[1]
            tipo = value[2]
            x = value[3]
            y = value[4]
            v_mes = value[6]
            v_ano = value[7]
            d_dia = value[8]
            d_mes = value[9]
            d_ano = value[10]
            valor = value[11]
            numero = value[12]

            historico = (850, 337)
            referencia_local = (360, 136)
            tipo_local = (541, 137)
            conta = (914, 435)
            confirmacao = (1010, 135)
            baixar = (1000, 237)

            pyautogui.write("{}{}{}".format(v_ano, v_mes, contrato))
            pyautogui.press('enter')
            pyautogui.write(tipo)
            pyautogui.press('enter')
            pyautogui.write(x)
            pyautogui.press('enter')
            pyautogui.write(y)
            pyautogui.press('enter')
            time.sleep(0.2)
            pyautogui.hotkey('ctrl', 'c')
            time.sleep(0.2)
            erro = pyperclip.paste()
            if 'Opção não permitida' in erro:
                with open('erro.txt', 'a') as arquivo:
                    arquivo.write(f'\n{numero_rps} - Opcao nao permitida ')
                    pyautogui.press('esc')
                    pyautogui.press('esc')
                    open_geral()
            elif "Não existe 'Contrato de Jazigo'." in erro:
                with open('erro.txt', 'a') as arquivo:
                    arquivo.write(f'\n{numero_rps} - Nao existe Contrato de Jazigo')
                    pyautogui.press('esc')
                    pyautogui.press('esc')
                    open_geral()
            elif 'SIAC - Sist. Integrado Adm. Cemitério' in erro:
                with open('erro.txt', 'a') as arquivo:
                    arquivo.write(f'\n{numero_rps} - ja baixado')
                    pyautogui.press('esc')
                    pyautogui.hotkey('shift', 'tab')
                    pyautogui.hotkey('shift', 'tab')
                    pyautogui.hotkey('shift', 'tab')
            else:
                pyautogui.press('enter')
                pyautogui.press('enter')
                pyautogui.press('enter')
                pyautogui.write("{}{}{}".format(d_dia, d_mes, d_ano))
                pyautogui.press('enter')
                pyautogui.press('enter')
                pyautogui.press('enter')
                pyautogui.write(valor)
                pyautogui.press('enter')

                if answer == '1':
                    pyautogui.write("237")
                    pyautogui.press("enter")
                    pyautogui.press("0")
                    pyautogui.press("1")
                    pyautogui.press("up")
                    pyautogui.press("enter")
                    pyautogui.press("0")
                    pyautogui.press("3")
                    pyautogui.press('enter')
                else:
                    pyautogui.write("999")
                    pyautogui.press("enter")
                    pyautogui.press("9")
                    pyautogui.press("enter")
                    pyautogui.press("9")
                    pyautogui.press('enter')

                pyautogui.click(*historico)

                if answer == '1':
                    pyautogui.write("PG VIA PIX - RPS:. {}".format(numero_rps))
                else:
                    pyautogui.write("MALOTE DIARIO: {} - RPS:. {}".format(numero, numero_rps))

                pyautogui.click(*conta)
                pyautogui.write("300P")
                pyautogui.click(*confirmacao)
                pyautogui.press('enter')
                time.sleep(0.2)
                pyautogui.click(*baixar)
                pyautogui.click(*baixar)
                time.sleep(0.2)
                pyautogui.press('enter')
                pyautogui.press('enter')
                time.sleep(0.3)
                pyautogui.click(*tipo_local)
                pyautogui.click(*referencia_local)


def open_siac_to_receive():
    # Caminho para o arquivo executável do aplicativo
    trajectory_tax = r'C:\Program Files (x86)\SIAC - Sist. Integrado Adm. Cemitério\UUMNUMBRCE01.exe'
    try:
        # Abre o aplicativo usando o caminho especificado
        subprocess.Popen(trajectory_tax)
    except FileNotFoundError:
        print("O arquivo do siac não foi encontrado.")
    except Exception as e:
        print(f"Ocorreu um erro ao abrir o siac: {e}")


def open_geral():
    open_siac_to_receive()
    time.sleep(1)
    l_mov = (338, 33)
    l_baixar = (364, 85)
    pyautogui.click(l_mov)
    pyautogui.click(l_baixar)


if __name__ == '__main__':
    rps()
