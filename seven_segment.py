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

def exibir_numero(num):
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

def exibir_relogio():
    while True:
        agora = datetime.now()
        hora, minuto, segundo = agora.hour, agora.minute, agora.second

        h1, h2 = divmod(hora, 10)
        m1, m2 = divmod(minuto, 10)
        s1, s2 = divmod(segundo, 10)

        linhas_h1 = exibir_numero(h1)
        linhas_h2 = exibir_numero(h2)
        linhas_m1 = exibir_numero(m1)
        linhas_m2 = exibir_numero(m2)
        linhas_s1 = exibir_numero(s1)
        linhas_s2 = exibir_numero(s2)

        os.system("cls" if os.name == "nt" else "clear")

        largura = 47  
        print("╔" + "═" * largura + "╗")

        for i in range(5):

            separador1 = " : " if i == 2 else "   "  
            separador2 = " : " if i == 2 else "   " 

            linha = (
                "    " + linhas_h1[i] + " " + linhas_h2[i] + separador1 +
                linhas_m1[i] + " " + linhas_m2[i] + separador2 +
                linhas_s1[i] + " " + linhas_s2[i] + "    "
            )
            print(f"║{linha}║")  

        print("╚" + "═" * largura + "╝")

        time.sleep(1)

exibir_relogio()
