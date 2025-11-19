from collections import Counter

# 1. Clientes que compraron sin estar registrados


def obtener_clientes_nuevos(compras, registrados):
    return list(set(compras) - set(registrados))


# 2. Quitar duplicados manteniendo el orden
def eliminar_duplicados_orden(compras):
    unicos = {}
    for cliente in compras:
        if cliente not in unicos:
            unicos[cliente] = True
    return list(unicos.keys())


# 3. Contar cuántas veces compró cada cliente
def contar_compras(compras):
    return Counter(compras)


# 4. Crear resumen solo para quienes compraron más de una vez
def crear_resumen(conteo):
    return {
        cliente: f"Ha comprado {veces} veces"
        for cliente, veces in conteo.items()
        if veces > 1
    }


# 5. Mostrar los tres bloques de resultados
def imprimir_resultados(nuevos, unicos, resumen):
    print("=" * 40)
    print(" Clientes nuevos no registrados")
    print("-" * 40)
    print(nuevos)

    print("\n" + "=" * 40)
    print(" Lista de clientes únicos")
    print("-" * 40)
    print(unicos)

    print("\n" + "=" * 40)
    print(" Resumen de clientes frecuentes")
    print("-" * 40)
    for cliente, mensaje in resumen.items():
        print(f"{cliente}: {mensaje}")
    print("=" * 40)


# MAIN

def main():
    compras = [
        "Luis", "Ana", "Luis", "Carlos", "Marta", "Ana", "Sofía",
        "Elena", "Luis", "Carlos"
    ]
    registrados = ["Ana", "Carlos", "Marta", "Elena"]

    nuevos = obtener_clientes_nuevos(compras, registrados)
    unicos = eliminar_duplicados_orden(compras)
    conteo = contar_compras(compras)
    resumen = crear_resumen(conteo)

    imprimir_resultados(nuevos, unicos, resumen)


if __name__ == "__main__":
    main()
