secret_number = 92
game = 0


def magic_cycle(futile_try):
    if futile_try != secret_number:
        print("¡Halloween, Halloween! ¡Estás atrapado en mi ciclo!")
        return futile_try
    elif futile_try == secret_number:
        print("¡You're  great, ! Eres libre ahora")
        return futile_try


while game != secret_number:
    try:
        suffering = int(input("Adivina el número secreto! Ingresa un numero:"))
        game = magic_cycle(suffering)
    except Exception as neg:
            print("Error:", str(neg))
                  