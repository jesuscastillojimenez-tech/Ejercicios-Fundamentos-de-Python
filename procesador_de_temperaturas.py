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
    contador = 0  # variable para contar cuántas veces se llamó la función

    def wrapper():
        nonlocal contador   # permite modificar la variable contador externa
        contador += 1
        print(f"[auditar] Ejecutando {func.__name__} (llamada #{contador})")

        inicio = time.perf_counter()
        resultado = func()   # llamada directa sin pasar parámetros
        fin = time.perf_counter()

        print(f"[auditar] Duración: {fin - inicio:.6f} s")
        return resultado

    return wrapper



def filtrar_alertas(iterable):
    return filter(lambda t: t[1] >= 30, iterable)

def transformar_alertas(iterable):
    return map(lambda t: f"Alerta de calor en {t[0]}: {t[1]}°C", iterable)

def ordenar_descendente(seq):
    return sorted(seq, key=lambda t: t[1], reverse=True)

def promedio_temperaturas(seq):
    temps = [t[1] for t in seq]
    if not temps:
        return None
    suma = reduce(lambda a, b: a + b, temps, 0)
    return suma / len(temps)




@auditar_funcion
def procesar_alertas():
    gen = leer_temperaturas()
    filtrados = list(filtrar_alertas(gen))
    promedio = promedio_temperaturas(filtrados)
    ordenados = ordenar_descendente(filtrados)
    mensajes = list(transformar_alertas(ordenados))

    print("\nAlertas ordenadas:")
    for m in mensajes:
        print("-", m)

    if promedio is not None:
        print(f"\nTemperatura promedio de alertas: {promedio:.1f}°C")
    else:
        print("\nNo hay alertas para calcular promedio.")



if __name__ == "__main__":
    procesar_alertas()
