import time

# Lectura de la gramática CNF
def leer_gramatica_cnf(ruta_archivo):
    grammar = {}
    with open(ruta_archivo, "r", encoding="utf-8") as f:
        for linea in f:
            linea = linea.strip()
            if not linea or linea.startswith("#"):
                continue
            if "->" not in linea:
                continue
            var, prods = linea.split("->")
            var = var.strip()
            prod_list = []
            for prod in prods.split("|"):
                prod_symbols = tuple(prod.strip().split())
                prod_list.append(prod_symbols)
            grammar[var] = prod_list
    return grammar
