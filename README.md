# Proyecto 2 - Algoritmo CYK

## Descripción

Este proyecto implementa el algoritmo CYK (Cocke-Younger-Kasami) para determinar si una frase en inglés pertenece a un lenguaje definido por una gramática libre de contexto (CFG).
Se utiliza la Forma Normal de Chomsky (CNF) para la gramática y se construye el parse tree de manera jerárquica.

---

## Archivos

* `main.py`
  Programa principal. Lee la gramática (`eng.txt`), solicita la frase al usuario, ejecuta CYK y muestra resultados y parse tree.

* `yk_cnf.py`
  Funciones auxiliares:

  * `leer_gramatica_cnf`: carga la gramática en CNF.
  * `cyk_parse`: ejecuta el algoritmo CYK.
  * `build_tree`: reconstruye el parse tree.
  * `print_tree`: imprime el parse tree jerárquico.

* `eng.txt`
  Gramática en inglés para el proyecto.

---

## Uso

1. Ejecutar `main.py`:

```bash
python main.py
```

2. Ingresar la frase (tokens separados por espacios), por ejemplo:

```
she eats a cake with a fork
```

3. El programa mostrará:

   * Gramática cargada.
   * Resultado (SÍ / NO).
   * Tiempo de ejecución.
   * Parse tree completo.

---

## Ejemplos de prueba

### Frases válidas (SÍ):

* `she eats a cake with a fork`
* `the cat drinks the beer`
* `he cuts the meat`

### Frases inválidas (NO):

* `cat drinks she`
* `he drinks juice`

> Nota: El algoritmo valida **sintaxis**, no semántica. Por eso algunas frases sin sentido pueden ser aceptadas si cumplen la gramática.

---

## Tiempo de ejecución

El tiempo se mide usando `time.perf_counter()` y se muestra en segundos con precisión de microsegundos.

---

## Diseño de la aplicación

* Se carga la gramática desde un archivo de texto.
* Se aplica el algoritmo CYK usando programación dinámica.
* Se reconstruye el parse tree guardando los nodos intermedios.
* La salida incluye resultado, tiempo y árbol sintáctico.

---

## Discusión

* **Obstáculos encontrados**: Ajustar la gramática a CNF y manejar terminales y binarización.
* **Recomendaciones**: Siempre separar entrada y gramática para facilitar pruebas y modificaciones.

---