# Variables para billetes a entregar
billetes_1000 = 10
billetes_500 = 10
billetes_200 = 10
billetes_100 = 10
billetes_50 = 10
billetes_20 = 10

# Variables para billetes a entregar
entregar_1000 = 0
entregar_500 = 0
entregar_200 = 0
entregar_100 = 0
entregar_50 = 0
entregar_20 = 0


# Iniciamos sistema
print("\n--- Dispensadora de Billetes ---")

# Solicitar monto
print("\nIngrese el monto a retirar (0 para salir): ")
entrada = input()

monto = int(entrada)
monto_restante = monto

# Mensaje al seleccionar salir (0)
if monto == 0:
    print("Gracias por usar este cajero automático, vuelva pronto.")

# Calculamos el total que hay dentro del cajero
else:
    total_caja = billetes_1000*1000 + billetes_500*500 + billetes_200 * \
        200 + billetes_100*100 + billetes_50*50 + billetes_20*20

    # Verificar que el monto sea valido
    if monto < 20 or monto % 10 != 0:
        print("Monto invalido (minimo $20 y debe ser multiplo de 10)")

    # Mensaje si el monto solicitado es mayor al monto disponible
    elif monto > total_caja:
        print("No hay suficiente efectivo en el cajero")

    # Usar la menor cantidad de billetes, tomando primero los billetes de mayor denominación
    else:
        while monto_restante >= 1000 and entregar_1000 < billetes_1000:
            entregar_1000 += 1
            monto_restante -= 1000
        while monto_restante >= 500 and entregar_500 < billetes_500:
            entregar_500 += 1
            monto_restante -= 500
        while monto_restante >= 200 and entregar_200 < billetes_200:
            entregar_200 += 1
            monto_restante -= 200
        while monto_restante >= 100 and entregar_100 < billetes_100:
            entregar_100 += 1
            monto_restante -= 100
        while monto_restante >= 50 and entregar_50 < billetes_50:
            entregar_50 += 1
            monto_restante -= 50
        while monto_restante >= 20 and entregar_20 < billetes_20:
            entregar_20 += 1
            monto_restante -= 20

        # Si no se puede dispensar el monto solicitado con el inventario disponible
        if monto_restante != 0:
            print("No se puede dispensar $", monto, "con el inventario acual.")

        # Mensaje del numero de billetes que se entrego de cada denominación
        else:
            print("\nSe entregarán: ")
            if entregar_1000:
                print(entregar_1000, " Billetes de $1000")
            if entregar_500:
                print(entregar_500, " Billetes de $500")
            if entregar_200:
                print(entregar_200, " Billetes de $200")
            if entregar_100:
                print(entregar_100, " Billetes de $100")
            if entregar_50:
                print(entregar_50, " Billetes de $50")
            if entregar_20:
                print(entregar_20, "Billetes de $20")

            # Mensaje del numero total de billetes entregados
            print("Total billetes:", entregar_1000+entregar_500 +
                  entregar_200+entregar_100+entregar_50+entregar_20)

            # Actualización de inventario
            billetes_1000 -= entregar_1000
            billetes_500 -= entregar_500
            billetes_200 -= entregar_200
            billetes_100 -= entregar_100
            billetes_50 -= entregar_50
            billetes_20 -= entregar_20

            print("Retiro exitoso. Inventario actualizado.")
