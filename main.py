from yk_cnf import leer_gramatica_cnf, cyk_parse, build_tree, print_tree
import time

def main():
    ruta_gramatica = "data/eng.txt"
    grammar = leer_gramatica_cnf(ruta_gramatica)

    print("Gramática cargada:")
    for A in grammar:
        print(A, "->", " | ".join(" ".join(p) for p in grammar[A]))

    sentence = input("\nIngrese la frase: ").strip().lower()
    words = sentence.split()

    start_time = time.perf_counter()
    table, back = cyk_parse(words, grammar)
    end_time = time.perf_counter()

    accepted = "S" in table[0][len(words)-1] if words else False
    print("\nResultado:", "SÍ" if accepted else "NO")
    print(f"Tiempo: {end_time - start_time:.8f} segundos")

    if accepted:
        print("\nParse tree completo: ")
        tree = build_tree(back, 0, len(words)-1, "S")
        print_tree(tree)

if __name__ == "__main__":
    main()
