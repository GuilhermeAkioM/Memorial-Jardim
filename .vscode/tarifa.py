import pyautogui
import time
import subprocess

pyautogui.PAUSE = 0.3


def tax():
    registration = input("numero do registro: ")
    nf = input("nf: ")
    answer = input("(s/n) Quer colocar data? ").lower()

    if answer == "s":
        date = input("data: ")
    elif answer == 'n':
        print('ok')
    else:
        print("invalido!")
        tax()

    open_siac_tax()
    time.sleep(0.5)
    open_title_registration()
    time.sleep(0.5)

    with open('geral.txt', 'r') as file:
        for line in file:
            value = line.split('|')
            if answer == "n":
                date = value[0]
                monetary = value[1]
                modality = value[2]
                company = value[3]
            else:
                date = date  # só para tirar o amarelo
                monetary = value[0]
                modality = value[1]
                company = value[2]

            modality = modality.upper()
            company = company.upper()
            registration = change_registration(registration)
            pyautogui.write(str(registration))
            pyautogui.press('enter')
            pyautogui.press('enter')
            pyautogui.press('enter')
            pyautogui.write(nf)
            pyautogui.press('enter')
            pyautogui.press('enter')
            pyautogui.write(date)
            pyautogui.press('enter')
            pyautogui.write(date)
            pyautogui.press('enter')
            pyautogui.write(monetary)
            pyautogui.press('enter')
            pyautogui.write(number(modality))
            pyautogui.press('enter')
            name_modality(modality, company)
            pyautogui.write("237")
            pyautogui.press('enter')
            pyautogui.write("06022")
            pyautogui.press('enter')
            pyautogui.write("300P")
            pyautogui.press('enter')
            pyautogui.press('enter')
            pyautogui.press('enter')
            pyautogui.press('enter')
            pyautogui.press('enter')
            pyautogui.write(str(number_group(modality)))
            pyautogui.press('enter')
            pyautogui.write(str(number_sub(modality)))
            pyautogui.press('enter')
            pyautogui.press('enter')
            pyautogui.press('enter')
            pyautogui.press('enter')
            time.sleep(0.3)


def open_siac_tax():
    trajectory_tax = r'C:\Program Files (x86)\SIAC - Sist. Integrado Adm. Cemitério\UUMNUMBRCE03.exe'

    try:
        subprocess.Popen(trajectory_tax)
    except FileNotFoundError:
        print("O arquivo do siac não foi encontrado.")
    except Exception as e:
        print(f"Ocorreu um erro ao abrir o siac: {e}")


def open_title_registration():
    movimentacao = (181, 32)
    incluir = (195, 53)
    pyautogui.click(*movimentacao)
    pyautogui.click(*incluir)


def change_registration(initial_registration):
    initial_registration = int(initial_registration)
    initial_registration = initial_registration + 1
    return initial_registration


def number(modality):
    if modality in ['1', '2', '3']:
        return "403"
    elif modality == '4':
        return "404"
    else:
        return "1796"


def number_group(modality):
    if modality in ['1', '2', '3']:
        pyautogui.write('8')
    elif modality == '4':
        pyautogui.write('8')
    else:
        pyautogui.write('5')


def number_sub(modality):
    if modality in ['1', '2', '3']:
        pyautogui.write("2")
    elif modality == "4":
        pyautogui.write("9")
    else:
        pyautogui.write("15")


def name_modality(modality, company):
    if modality == '1':
        pyautogui.write('REF.TARIFA BANCARIA BAIXA SEM PAGAMENTO')
        pyautogui.press('enter')
    elif modality == '2':
        pyautogui.write('REF.TARIFA BANCARIA BAIXA POR PAGAMENTO')
        pyautogui.press('enter')
    elif modality == '3':
        pyautogui.write('REF.TARIFA BANCARIA BAIXA POR COMPENSACAO')
        pyautogui.press('enter')
    elif modality == '4':
        pyautogui.write('REF.TARIFA BANCARIA DOC/TED')
        pyautogui.press('enter')
    else:
        pyautogui.write('REF. TARIFA CARTAO {} {}'.format(company, modality))


if __name__ == '__main__':
    tax()
