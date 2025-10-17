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

#Implementación CYK
def cyk_parse(words, grammar):
    n = len(words)
    table = [[set() for _ in range(n)] for _ in range(n)]
    back = [[dict() for _ in range(n)] for _ in range(n)]

    for i, word in enumerate(words):
        for var, productions in grammar.items():
            for prod in productions:
                if len(prod) == 1 and prod[0] == word:
                    table[i][i].add(var)
                    back[i][i][var] = word

    for l in range(2, n+1):
        for i in range(n - l + 1):
            j = i + l - 1
            for k in range(i, j):
                for var, productions in grammar.items():
                    for prod in productions:
                        if len(prod) == 2:
                            B, C = prod
                            if B in table[i][k] and C in table[k+1][j]:
                                table[i][j].add(var)
                                back[i][j][var] = (k, B, C)

    return table, back