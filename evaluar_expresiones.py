
import time

def mostrar_pila(pila):
    print("\n--- PILA ---")
    if len(pila) == 0:
        print("| vacia |")
    else:
        for elemento in reversed(pila):
            print("|", elemento, "|")
    print("-----------")


def evaluar_posfija(expresion):
    pila = []

    print("\nEvaluando expresion posfija")
    print("Expresion:", expresion)

    for elemento in expresion.split():
        print("\nElemento:", elemento)

        if elemento.lstrip("-").isdigit():
            pila.append(float(elemento))
            print("Se agrega a la pila:", elemento)
        else:
            if len(pila) < 2:
                raise ValueError("Expresion incorrecta")

            b = pila.pop()
            a = pila.pop()

            if elemento == "+":
                resultado = a + b
            elif elemento == "-":
                resultado = a - b
            elif elemento == "*":
                resultado = a * b
            elif elemento == "/":
                if b == 0:
                    raise ValueError("Division entre cero")
                resultado = a / b
            else:
                raise ValueError("Operador invalido")

            pila.append(resultado)
            print("Operacion:", a, elemento, b, "=", resultado)

        mostrar_pila(pila)

    if len(pila) != 1:
        raise ValueError("Expresion incorrecta")

    return pila.pop()


def evaluar_prefija(expresion):
    pila = []
    elementos = expresion.split()[::-1]

    print("\nEvaluando expresion prefija")
    print("Expresion:", expresion)

    for elemento in elementos:
        print("\nElemento:", elemento)

        if elemento.lstrip("-").isdigit():
            pila.append(float(elemento))
            print("Se agrega a la pila:", elemento)
        else:
            if len(pila) < 2:
                raise ValueError("Expresion incorrecta")

            a = pila.pop()
            b = pila.pop()

            if elemento == "+":
                resultado = a + b
            elif elemento == "-":
                resultado = a - b
            elif elemento == "*":
                resultado = a * b
            elif elemento == "/":
                if b == 0:
                    raise ValueError("Division entre cero")
                resultado = a / b
            else:
                raise ValueError("Operador invalido")

            pila.append(resultado)
            print("Operacion:", a, elemento, b, "=", resultado)

        mostrar_pila(pila)

    if len(pila) != 1:
        raise ValueError("Expresion incorrecta")

    return pila.pop()


def main():
    inicio_programa = time.perf_counter()

    print("EVALUADOR DE EXPRESIONES")
    print("Escribe FIN para terminar")

    while True:
        print("\n1. Evaluar expresion posfija")
        print("2. Evaluar expresion prefija")
        print("FIN. Terminar programa")

        opcion = input("Elige una opcion: ").strip().upper()

        if opcion == "FIN":
            break

        if opcion not in ["1", "2"]:
            print("Opcion invalida")
            continue

        expresion = input("Ingresa la expresion: ").strip()

        if expresion.upper() == "FIN":
            break

        inicio_evaluacion = time.perf_counter()

        try:
            if opcion == "1":
                resultado = evaluar_posfija(expresion)
            else:
                resultado = evaluar_prefija(expresion)

            print("\nResultado final:", resultado)

        except (ValueError, ZeroDivisionError):
            print("Error: expresion incorrecta")

        fin_evaluacion = time.perf_counter()

        print("Tiempo de evaluacion:",
              format(fin_evaluacion - inicio_evaluacion, ".9f"),
              "segundos")

    inicio_final = time.perf_counter()
    print("\nPrograma finalizado")
    print("Finalizando programa...")
    fin_final = time.perf_counter()

    print("Tiempo final del programa:",
          format(fin_final - inicio_final, ".9f"), "segundos")

    fin_programa = time.perf_counter()
    tiempo_total = fin_programa - inicio_programa

    print("Tiempo total de ejecucion:",
          format(tiempo_total, ".9f"), "segundos")

    print("Fin del programa")


if __name__ == "__main__":
    main()
