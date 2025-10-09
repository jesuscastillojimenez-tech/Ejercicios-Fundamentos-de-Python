# Credenciales válidas (como variables individuales)
usuario_correcto = "admin"
clave_correcta = "1234"

# Número de intentos
intentos = 3

print("\n--- Sistema de Inicio de Sesión ---")

# Ciclo para intentos
while intentos > 0:
    print(f"Intentos restantes: {intentos}")

    # Solicitar credenciales
    print("Usuario: ")
    usuario = input()
    print("Contraseña: ")
    clave = input()

    # Verificar si usuario o clave estan vacios
    if usuario == "" or clave == "":
        print("Error de acceso, no puedes dejar campos vacios.")

    # Verificar si las credenciales son correctas
    elif usuario == usuario_correcto and clave == clave_correcta:
        print("\nInicio de Sesión Correcto. ¡Bienvenid@!")

        # Salir del ciclo si las credenciales son correctas
        break

    # Si el usuario o la clave son incorrectos
    else:
        print("Usuario o contraseña incorrectos, vuelve a intentarlo")

    # Restar intento
    intentos -= 1

# Mensaje si se terminan todos los intentos
if intentos == 0:
    print("\nHas llegado al limite de intentos. Acceso bloqueado.")
