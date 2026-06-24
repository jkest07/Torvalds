import subprocess


def ejecutar(comando):
    return subprocess.check_output(comando, text=True).strip()


# Commits desde el más antiguo al más reciente
commits = ejecutar(
    ["git", "rev-list", "--reverse", "HEAD"]
).splitlines()

llave = ""

for commit in commits:

    # Hash completo
    hash_completo = ejecutar(
        ["git", "rev-parse", commit]
    )

    # Contenido de nucleo.txt en ese commit
    contenido = ejecutar(
        ["git", "show", f"{commit}:nucleo.txt"]
    )

    # Primeros 6 caracteres del hash convertidos a decimal
    valor = int(hash_completo[:6], 16)

    if valor % 2 == 0:
        # Caso PAR

        caracter = contenido[0]

        cantidadn = sum(
            c.isdigit()
            for c in hash_completo
        )

        if caracter.isalpha():

            base = ord('A') if caracter.isupper() else ord('a')

            caracter = chr(
                (ord(caracter) - base + cantidadn) % 26
                + base
            )

        llave += caracter

    else:
        # Caso IMPAR

        caracter = contenido[-1]

        cantidadl = sum(
            c.lower() in "abcdef"
            for c in hash_completo
        )

        caracter = chr(
            ord(caracter) + cantidadl
        )

        llave += caracter

    # Detectar merge commit
    padres = ejecutar(
        ["git", "rev-list", "--parents", "-n", "1", commit]
    ).split()

    if len(padres) > 2:
        llave = llave[::-1]

print(llave)

#<XaROQTTeNVTPTN