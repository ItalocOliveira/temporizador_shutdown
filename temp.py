import time
import os

def temporizador_shutdown():
    temp = input("Quanto tempo terá o temporizador? \n")

    if temp.startswith("h "):
        horas = int(temp[2:])
        segundos = horas * 3600

    elif temp.startswith("m "):
        minutos = int(temp[2:])
        segundos = minutos * 60
    
    elif temp.startswith("s "):
        segundos = int(temp[2:])

    else:
        print("Formato inválido. Use 'h X', 'm X' ou 's X'")
            
    for _ in range(segundos):

        h = segundos // 3600
        m = (segundos % 3600) // 60
        s = segundos % 60
        


        print("O computador desligará em: {:02d}:{:02d}:{:02d}".format(h, m, s), end="\r")
        time.sleep(1)
        segundos -=1

        if segundos == 0:
            os.system("shutdown /s /t 1")

temporizador_shutdown()