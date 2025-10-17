import time

def cyk_parse(tokens, grammar):
    n = len(tokens)
    table = [[set() for _ in range(n)] for _ in range(n)]
    back = [[dict() for _ in range(n)] for _ in range(n)]

    # Terminales
    for i, word in enumerate(tokens):
        for var, productions in grammar.items():
            for prod in productions:
                if len(prod) == 1 and prod[0] == word:
                    table[i][i].add(var)
                    back[i][i][var] = word

    # Subcadenas de longitud >1
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

def build_tree(back, i, j, symbol):
    if i == j:
        return symbol
    k, B, C = back[i][j][symbol]
    return (symbol, build_tree(back, i, k, B), build_tree(back, k+1, j, C))
