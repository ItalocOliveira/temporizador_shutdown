import time
import os

def temporizador_shutdown():
    minutos = int(input("Quantos minutos terá o contador? \n"))
    segundos = minutos * 60

    for _ in range(segundos):
        q = segundos // 60
        r = segundos % 60

        print("Computador desligando em: {:02d}:{:02d}".format(q,r), end="\r" )
        time.sleep(1)
        segundos -= 1

        if segundos == 0:
            os.system("shutdown /s /t 1")

temporizador_shutdown()