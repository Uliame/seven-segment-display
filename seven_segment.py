import time
import os
from datetime import datetime

segmentos = {
    0: [1, 1, 1, 0, 1, 1, 1],
    1: [0, 0, 1, 0, 0, 1, 0],
    2: [1, 0, 1, 1, 1, 0, 1],
    3: [1, 0, 1, 1, 0, 1, 1],
    4: [0, 1, 1, 1, 0, 1, 0],
    5: [1, 1, 0, 1, 0, 1, 1],
    6: [1, 1, 0, 1, 1, 1, 1],
    7: [1, 0, 1, 0, 0, 1, 0],
    8: [1, 1, 1, 1, 1, 1, 1],
    9: [1, 1, 1, 1, 0, 1, 1],
}

def exibirNumero(num):
    if num not in segmentos:
        return ["     ", "     ", "     ", "     ", "     "]

    seg = segmentos[num]

    linhas = [
        f"  {'─' if seg[0] else ' '}  ",
        f"{'|' if seg[1] else ' '}   {'|' if seg[2] else ' '}",
        f"  {'─' if seg[3] else ' '}  ",
        f"{'|' if seg[4] else ' '}   {'|' if seg[5] else ' '}",
        f"  {'─' if seg[6] else ' '}  "
    ]
    
    return linhas

def exibirRelogio():
    while True:
        now = datetime.now()
        hora, minuto, segundo = now.hour, now.minute, now.second

        h1, h2 = divmod(hora, 10)
        m1, m2 = divmod(minuto, 10)
        s1, s2 = divmod(segundo, 10)

        linhasH1 = exibirNumero(h1)
        linhasH2 = exibirNumero(h2)
        linhasM1 = exibirNumero(m1)
        linhasM2 = exibirNumero(m2)
        linhasS1 = exibirNumero(s1)
        linhasS2 = exibirNumero(s2)

        os.system("cls" if os.name == "nt" else "clear")

        largura = 47  
        print("╔" + "═" * largura + "╗")

        for i in range(5):

            separador1 = " : " if i == 2 else "   "  
            separador2 = " : " if i == 2 else "   " 

            linha = (
                "    " + linhasH1[i] + " " + linhasH2[i] + separador1 +
                linhasM1[i] + " " + linhasM2[i] + separador2 +
                linhasS1[i] + " " + linhasS2[i] + "    "
            )
            print(f"║{linha}║")  

        print("╚" + "═" * largura + "╝")

        time.sleep(1)

exibirRelogio()
