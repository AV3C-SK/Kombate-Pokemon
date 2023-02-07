from random import randint
import os

vida_inicial_pikachu = 100
vida_inicial_squirtle = 120

vida_pikachu = vida_inicial_pikachu
vida_squirtle = vida_inicial_squirtle



titulo = "Bienvenido a KOMBATE POKEMON!"
print("\n" + titulo + "\n" + "-" * len(titulo))


while vida_pikachu > 0 and vida_squirtle > 0:
    #Esto son los turnos del combate
    #Turno de Pikachu
    print("\nTurno de pikachu\n")
    ataque_pikachu = randint(1,2)
    if ataque_pikachu == 1:
        print("Pikachu ataca con Bola Trueno (-10)")
        vida_squirtle -= 10
    else:
        print("Pikachu ataca con InpacTrueno (-12)")
        vida_squirtle -= 12
    if vida_pikachu < 0:
        vida_squirtle = 0

    if vida_squirtle < 0:
        vida_pikachu = 0

    barrapikachu = int(vida_pikachu * 10 / vida_inicial_pikachu)

    print("Pikachu   [{}{}] ({}\{})".format("*" * barrapikachu, " " * (10 - barrapikachu),
                                            vida_pikachu, vida_inicial_pikachu))

    barrasquirtle = int(vida_squirtle * 10 / vida_inicial_squirtle)

    print("Squirtle  [{}{}] ({}\{})".format("*" * barrasquirtle, " " * (10 - barrasquirtle),
                                            vida_squirtle, vida_inicial_squirtle))
    #Turno de Squirtle

    input("\nEnter para continuar.....")
    os.system("cls")

    print("\nTurno Squirtle")
    ataque_esquirtle = input("Que ataque prefieres?\n"
                             "A) Bomba de Agua\n"
                             "B) Burbujas\n"
                             "Eligo la opcion: ")
    if ataque_esquirtle == "A":
        print("\nAtacas con Bomba de agua (-8)")
        vida_pikachu -= 8
    else:
        print("\nAtacas con Burbujas (-10)")
        vida_pikachu -= 10

    if vida_pikachu < 0:
        vida_squirtle = 0

    if vida_squirtle < 0:
        vida_pikachu = 0

        print("Pikachu    [{}{}] ({}\{})".format("*" * barrapikachu, " " * (10 - barrapikachu),
                                                 vida_pikachu, vida_inicial_pikachu))

        barrasquirtle = int(vida_squirtle * 10 / vida_inicial_squirtle)

        print("Squirtle   [{}{}] ({}\{})".format("*" * barrasquirtle, " " * (10 - barrasquirtle),
                                                 vida_squirtle, vida_inicial_squirtle))

    input("\nEnter para continuar........")
    os.system("cls")

if vida_pikachu > vida_squirtle:
    print("Pikachu es el ganador!")

else:
    print("ERES EL GANADOR, felicidades, lograste pasar el desafio!")