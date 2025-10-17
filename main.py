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


# Eliminar epsilon-producciones
def eliminar_epsilon(gramatica, inicio):
    anulables = set()
    cambio = True
    while cambio:
        cambio = False
        for A in gramatica:
            for prod in gramatica[A]:
                if len(prod) == 0 or all(x in anulables for x in prod):
                    if A not in anulables:
                        anulables.add(A)
                        cambio = True
    nueva = defaultdict(list)
    for A in gramatica:
        for prod in gramatica[A]:
            if len(prod) == 0:
                continue
            partes = [i for i, x in enumerate(prod) if x in anulables]
            for m in range(1 << len(partes)):
                nueva_prod = [prod[i] for i in range(len(prod)) if i not in partes or not (m >> partes.index(i)) & 1]
                nueva[A].append(tuple(nueva_prod))
    if inicio in anulables:
        nueva[inicio].append(())
    return nueva


# Eliminar producciones unitarias
def eliminar_unitarias(gramatica):
    unidades = defaultdict(set)
    for A in gramatica:
        for prod in gramatica[A]:
            if len(prod) == 1 and prod[0] in gramatica:
                unidades[A].add(prod[0])
    cambio = True
    while cambio:
        cambio = False
        for A in list(unidades.keys()):
            nuevas = set()
            for B in unidades[A]:
                nuevas |= unidades.get(B, set())
            antes = len(unidades[A])
            unidades[A] |= nuevas
            if len(unidades[A]) > antes:
                cambio = True
    nueva = defaultdict(list)
    for A in gramatica:
        for prod in gramatica[A]:
            if not (len(prod) == 1 and prod[0] in gramatica):
                nueva[A].append(prod)
        for B in unidades[A]:
            for prod in gramatica[B]:
                if not (len(prod) == 1 and prod[0] in gramatica):
                    nueva[A].append(prod)
    return nueva

# Reemplazar terminales y binarizar
contador = 1
def nuevo_simbolo(prefijo="X"):
    global contador
    s = f"{prefijo}{contador}"
    contador += 1
    return s

def preparar_cnf(gramatica):
    nueva = defaultdict(list)
    reemplazos = {}
    for A in gramatica:
        for prod in gramatica[A]:
            if len(prod) > 2:
                simbolos = list(prod)
                temp = nuevo_simbolo()
                nueva[A].append((simbolos[0], temp))
                for i in range(1, len(simbolos) - 2):
                    sig = nuevo_simbolo()
                    nueva[temp].append((simbolos[i], sig))
                    temp = sig
                nueva[temp].append(tuple(simbolos[-2:]))
            elif len(prod) == 2:
                nueva[A].append(prod)
            elif len(prod) == 1:
                x = prod[0]
                if x not in gramatica:
                    if x not in reemplazos:
                        var = nuevo_simbolo("T")
                        reemplazos[x] = var
                    nueva[A].append((reemplazos[x],))
                else:
                    nueva[A].append(prod)
    for t, v in reemplazos.items():
        nueva[v].append((t,))
    return nueva
