import sys
from collections import defaultdict

# Leer la gramática del archivo
def leer_gramatica(texto):
    gramatica = defaultdict(list)
    lineas = texto.strip().split("\n")
    for l in lineas:
        if "->" not in l:
            continue
        izq, der = l.split("->")
        izq = izq.strip()
        producciones = der.split("|")
        for p in producciones:
            p = p.strip()
            if p == "e" or p == "ε":
                gramatica[izq].append(())
            else:
                gramatica[izq].append(tuple(p.split()))
    return gramatica

