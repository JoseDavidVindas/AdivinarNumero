import random


def jugar_adivina_numero():
    print("¡Bienvenido al juego de adivinar el número!")
    numero_secreto = random.randint(1, 100)
    intentos_realizados = 0

    while True:
        intento = int(input("Introduce tu suposición (entre 1 y 100): "))
        intentos_realizados += 1

        if intento < numero_secreto:
            print("El número secreto es mayor que tu suposición.")
        elif intento > numero_secreto:
            print("El número secreto es menor que tu suposición.")
        else:
            print(f"¡Felicidades! ¡Has adivinado el número secreto en {intentos_realizados} intentos!")
            break

    jugar_nuevamente = input("¿Quieres jugar de nuevo? (sí/no): ")
    if jugar_nuevamente.lower() == 'sí':
        jugar_adivina_numero()
    else:
        print("¡Gracias por jugar!")


if __name__ == "__main__":
    jugar_adivina_numero()
