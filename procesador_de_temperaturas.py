

from functools import wraps, reduce

# Generador: produce pares (ciudad, temperatura)


def leer_temperaturas():
    """
    Generador 'yield' registros uno a uno.
    Simula una fuente de datos sin cargar todo en memoria.
    """
    datos = [
        ("CDMX", 26),
        ("Monterrey", 34),
        ("Toluca", 19),
        ("Cancún", 38),
        ("Guadalajara", 31),
        ("Puebla", 29),
        ("Mérida", 36),
    ]
    # Iteramos sobre la lista y devolvemos cada elemento con yield
    for registro in datos:
        yield registro


# Decorador: auditar llamadas y opcionalmente medir tiempo


def auditar_funcion(medir=False):

    # Devuelve un decorador que envuelve la función original.

    def decorator(func):
        contador = {"calls": 0}  # mutable closure para contar llamadas

        @wraps(func)
        def wrapper(*args, **kwargs):
            contador["calls"] += 1
            print(
                f"[auditar] Ejecutando '{func.__name__}' (llamada #{contador['calls']})")
            if medir:
                import time
                inicio = time.perf_counter()
                resultado = func(*args, **kwargs)
                fin = time.perf_counter()
                print(f"[auditar] Duración: {fin - inicio:.6f} s")
            else:
                resultado = func(*args, **kwargs)
            return resultado

        # Exponer el contador desde fuera
        wrapper.calls = contador
        return wrapper
    return decorator


# Funciones de procesamiento funcional (filter, map, sorted, reduce)


def filtrar_alertas(iterable):

    return filter(lambda t: t[1] >= 30, iterable)


def transformar_alertas(iterable):
    """Convierte tuplas a mensajes de texto usando map + lambda."""
    return map(lambda t: f"Alerta de calor en {t[0]}: {t[1]}°C", iterable)


def ordenar_descendente(seq):
    """Ordena una secuencia de tuplas (ciudad, temp) por temperatura descendente."""
    return sorted(seq, key=lambda t: t[1], reverse=True)


def promedio_temperaturas(seq):
    """Calcula el promedio de temperaturas usando reduce(). Devuelve None si no hay datos."""
    temps = [t[1] for t in seq]
    if not temps:
        return None
    suma = reduce(lambda a, b: a + b, temps, 0)
    return suma / len(temps)


# Función principal


@auditar_funcion(medir=True)
def procesar_alertas():
    # 1) Usar el generador (no carga todo en memoria al inicio)
    gen = leer_temperaturas()

    # 2) Filtrar (filter + lambda) — devuelve un iterator
    iter_filtrados = filtrar_alertas(gen)

    # 3) Materializar en lista para poder ordenar y calcular promedio
    lista_filtrados = list(iter_filtrados)

    # 4) Calcular promedio con reduce()
    promedio = promedio_temperaturas(lista_filtrados)

    # 5) Ordenar descendentemente
    ordenados = ordenar_descendente(lista_filtrados)

    # 6) Transformar a mensajes con map() + lambda
    mensajes = list(transformar_alertas(ordenados))

    # 7) Imprimir resultados
    print("\nAlertas ordenadas:")
    for m in mensajes:
        print("-", m)

    if promedio is not None:
        print(f"\nTemperatura promedio de alertas: {promedio:.1f}°C")
    else:
        print("\nNo hay alertas para calcular promedio.")


# Punto de entrada
if __name__ == "__main__":
    procesar_alertas()
