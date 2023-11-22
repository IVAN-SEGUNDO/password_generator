import string
import secrets
import os

os.system("clear")


def contiene_mayusculas(password):
    for letra in password:
        if letra.isupper():
            return False


def contiene_simbolos(password) -> bool:
    for letra in password:
        if letra in string.punctuation:
            return True


def generar_password(longitud, tiene_simbolos, tiene_mayusculas) -> str:
    combinacion = string.ascii_lowercase + string.digits
    # Se quieren simbolos
    if tiene_simbolos:
        combinacion += string.punctuation
    # Se quieren mayusculas
    if tiene_mayusculas:
        combinacion += string.ascii_uppercase

    print("Contraseña: " + combinacion)
    newPassword = ""
    for _ in range(longitud):
        newPassword += combinacion[secrets.randbelow(longitud)]
    return newPassword

    print("Contraseña: " + combinacion)
    return ""


if __name__ == "__main__":
    nuevo = generar_password(longitud=2, tiene_simbolos=True, tiene_mayusculas=True)
    print("Nueva: ", nuevo)
