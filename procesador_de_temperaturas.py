from functools import reduce
import time



def leer_temperaturas():
    datos = [
        ("CDMX", 26),
        ("Monterrey", 34),
        ("Toluca", 19),
        ("Cancún", 38),
        ("Guadalajara", 31),
        ("Puebla", 29),
        ("Mérida", 36),
    ]
    for registro in datos:
        yield registro



def auditar_funcion(func):
    contador = 0

    def wrapper():
        nonlocal contador
        contador += 1
        print(f"[auditar] Ejecutando {func.__name__} (llamada #{contador})")
        inicio = time.perf_counter()
        resultado = func()
        fin = time.perf_counter()
        print(f"[auditar] Duración: {fin - inicio:.6f} s")
        return resultado

    return wrapper

def medir_tiempo(func):
    def wrapper():
        inicio = time.time()
        resultado = func()
        fin = time.time()
        print(f"[tiempo] Duración: {fin - inicio:.4f} segundos")
        return resultado
    return wrapper



def filtrar_alertas():
    return list(filter(lambda t: t[1] >= 30, leer_temperaturas()))

def transformar_alertas():
    filtrados = filtrar_alertas()
    return list(map(lambda t: f"Alerta de calor en {t[0]}: {t[1]}°C", filtrados))

def ordenar_descendente():
    filtrados = filtrar_alertas()
    return sorted(filtrados, key=lambda t: t[1], reverse=True)

def promedio_temperaturas():
    filtrados = filtrar_alertas()
    temps = [t[1] for t in filtrados]
    if not temps:
        return None
    suma = reduce(lambda a, b: a + b, temps, 0)
    return suma / len(temps)




@medir_tiempo
@auditar_funcion
def procesar_alertas():
    mensajes = transformar_alertas()
    ordenados = ordenar_descendente()
    promedio = promedio_temperaturas()

    print("\nAlertas ordenadas:")
    for m in mensajes:
        print("-", m)

    if promedio is not None:
        print(f"\nTemperatura promedio de alertas: {promedio:.1f}°C")
    else:
        print("\nNo hay alertas para calcular promedio.")




if __name__ == "__main__":

    print("\n== DATOS DEL GENERADOR ==")
    for ciudad, temp in leer_temperaturas():
        print("-", ciudad, temp)

    print("\n== FILTRADAS (>=30°C) ==")
    for ciudad, temp in filtrar_alertas():
        print("-", ciudad, temp)

    print("\n== TRANSFORMADAS (map + lambda) ==")
    for m in transformar_alertas():
        print("-", m)

    print("\n== ORDENADAS (sorted) ==")
    for ciudad, temp in ordenar_descendente():
        print("-", ciudad, temp)

    print("\n== PROMEDIO (reduce) ==")
    print("Promedio:", promedio_temperaturas())

    print("\n== FUNCIÓN PRINCIPAL CON DECORADORES ==")
    procesar_alertas()