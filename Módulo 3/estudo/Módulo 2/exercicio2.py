'''
* Agendamento de Desligamento do PC
-> Crie duas funções em Python para agendar o desligamento do computador
em uma hora e meia hora.
** Extra
-> Crie uma função que permita cancelar o desligamento do computador
'''

import os

# 1 - Desligar o computador
# os.system("shutdown /s") # desliga o pc em 1 minuto
# os.system("shutdown /s /t 0") desliga agora o pc

# 2 - Cancelar desligamento
# os.system("shutdown /a")

def turn_off_one_hour():
    os.system("shutdown /s /t 3600")

def turn_off_half_an_hour():
    os.system("shutdown /s /t 1800")

def cancel_shutdown():
    os.system("shutdown /a")
