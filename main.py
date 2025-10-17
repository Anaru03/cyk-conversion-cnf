from yk_cnf import cyk_parse, build_tree
from collections import defaultdict

def leer_gramatica_archivo(ruta):
    """
    Lee la gramática desde un archivo .txt
    Formato esperado:
        S -> NP VP | Det N
    """
    gramatica = defaultdict(list)
    with open(ruta, "r", encoding="utf-8") as f:
        for linea in f:
            linea = linea.strip()
            if not linea or "->" not in linea:
                continue
            izq, der = linea.split("->")
            izq = izq.strip()
            for prod in der.split("|"):
                gramatica[izq].append(tuple(prod.strip().split()))
    return gramatica

def imprimir_arbol(tree, nivel=0):
    """
    Imprime el parse tree jerárquicamente
    """
    if isinstance(tree, str):
        print("  " * nivel + tree)
    else:
        print("  " * nivel + tree[0])
        imprimir_arbol(tree[1], nivel+1)
        imprimir_arbol(tree[2], nivel+1)

def main():
    ruta_gramatica = "data/eng.txt"  # tu archivo de gramática
    gramatica = leer_gramatica_archivo(ruta_gramatica)

    print("Gramática cargada:")
    for A in gramatica:
        print(A, "->", " | ".join(" ".join(p) for p in gramatica[A]))

    frase = input("\nIngrese la frase (tokens separados por espacios): ").strip().lower()
    tokens = frase.split()

    import time
    t0 = time.time()
    tabla, back = cyk_parse(tokens, gramatica)
    t1 = time.time()

    aceptada = "S" in tabla[0][len(tokens)-1] if tokens else False
    print("\nResultado:", "SÍ" if aceptada else "NO")
    print(f"Tiempo: {t1 - t0:.6f} segundos")

    if aceptada:
        tree = build_tree(back, 0, len(tokens)-1, "S")
        print("\nParse tree completo:")
        imprimir_arbol(tree)

if __name__ == "__main__":
    main()
