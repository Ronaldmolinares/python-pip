import random


def configuracion():
    print(":::::::::::::::Piedra Papel o Tijera:::::::::::::::\n")

    numero_victorias = None
    while numero_victorias is None:
        try:
            entrada = input("Escriba el numero de juegos: ")
            numero_victorias = int(entrada)
            if numero_victorias <= 0:
                print("Debe ser un número mayor que 0.")
                numero_victorias = None
            else:
                print(f"Que gane el mejor de {numero_victorias} juegos.")
        except ValueError:
            print("Intente de nuevo. Debe ingresar un número válido.")

    name_user = input("Nombre: ")

    return numero_victorias, name_user


def solicitar_datos():
    armas = ["piedra", "papel", "tijera"]
    usuario = input("Escriba con que va a jugar: ")
    option_pc = random.randint(1, len(armas))

    for arma in armas:
        if arma == usuario.lower():
            option_pc = armas[option_pc - 1]
            return usuario.lower(), option_pc

    else:
        raise "Opción invalida, intente de nuevo"


def juego():
    juegos, name_user = configuracion()
    victorias_user = 0
    victorias_pc = 0
    rounds = 1
    while True:
        try:
            resultado = solicitar_datos()
            print(resultado)
            match resultado:
                case ("piedra", "piedra") | ("papel", "papel") | ("tijera", "tijera"):
                    print("Empate")
                    rounds += 1
                case ("piedra", "tijera") | ("papel", "piedra") | ("tijera", "papel"):
                    print("Usuario Gana.")
                    victorias_user += 1
                    rounds += 1
                    if victorias_user == juegos:
                        print(f"Felicidades el usuario {name_user} a ganado.")
                        break
                case _:
                    print("La computadora Gana")
                    victorias_pc += 1
                    rounds += 1
                    if victorias_pc == juegos:
                        print("La computadora te ha derrotado.")
                        break
            print(
                f"Rounds: {rounds}, Victorias del usuario {name_user}: {victorias_user}, Victorias PC: {victorias_pc}, "
            )

        except Exception as e:
            print(e)


juego()