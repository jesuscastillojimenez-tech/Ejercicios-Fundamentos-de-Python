# main.py
from Proyecto_final import Calculadora
from analizador import interpretar_expresion, aplicar_operador


def main():
    calc = Calculadora(0, 0, 0)
    print("=== Calculadora modular (3 números) ===")
    print("Formato: a op b op c  (ej: 2 + 3 ^ 2)")
    print("Operadores: +  -  *  /  ^  (^ = potencia)")
    print("Comandos: 'historial', 'salir'\n")

    while True:
        entrada = input("Ingresa la operación: ").strip()
        if entrada == "":
            continue
        if entrada.lower() == "salir":
            print("¡Hasta pronto!")
            break
        if entrada.lower() == "historial":
            calc.ver_historial()
            continue

        parsed = interpretar_expresion(entrada)
        if not parsed:
            print(
                "Expresión no válida. Usa: número operador número operador número (ej. 2 + 3 + 4)\n")
            continue

        num1, num2, num3, op1, op2 = parsed

        try:
            calc.numero1 = num1
            calc.numero2 = num2
            calc.numero3 = num3
        except ValueError as e:
            print("Error en valores:", e)
            continue

        # Evaluación izquierda a derecha: (num1 op1 num2) op2 num3
        temp = aplicar_operador(num1, num2, op1)
        if isinstance(temp, str) and temp.startswith("Error"):
            print(temp)
            continue

        resultado = aplicar_operador(temp, num3, op2)
        if isinstance(resultado, str) and resultado.startswith("Error"):
            print(resultado)
            continue

        expr = f"{num1} {op1} {num2} {op2} {num3}"
        calc.agregar_a_historial(f"{expr} = {resultado}")
        print("Resultado:", resultado, "\n")


if __name__ == "__main__":
    main()
