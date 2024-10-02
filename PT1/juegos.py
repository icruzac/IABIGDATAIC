from colorama import Fore, Style
import random
import time
import mansajes as msg  # Módulo con funciones para mensajes personalizados
import tools as tl  # Módulo para herramientas auxiliares (como leer CSV)

# Constantes
MAX_INTENTOS_ADIVINA = 3  # Máximo de intentos para el juego 'Adivina el Número'
RANGO_NUMERO_SECRETO = (1, 10)  # Rango del número secreto en el juego 'Adivina el Número'
PUNTOS_GANAR_PPT = 3  # Puntos necesarios para ganar en 'Piedra, Papel o Tijeras'

# Juego: Adivina el Número
def adivina_el_numero():
    numero_secreto = random.randint(*RANGO_NUMERO_SECRETO)  # Genera el número secreto
    intentos = MAX_INTENTOS_ADIVINA

    # Muestra el mensaje de bienvenida y las reglas del juego
    msg.mostrar_mensaje_bienvenida("'Adivina el Número'")
    print(Fore.YELLOW + f"👉 El número está entre {RANGO_NUMERO_SECRETO[0]} y {RANGO_NUMERO_SECRETO[1]}. 👈")
    print(Fore.CYAN + f"🔮 Tienes {MAX_INTENTOS_ADIVINA} intentos para adivinar el número secreto.🔮")

    # Bucle principal del juego
    while intentos > 0:
        try:
            # Muestra el número de intento actual
            print(f"\n🕵️ Intento {MAX_INTENTOS_ADIVINA + 1 - intentos}/{MAX_INTENTOS_ADIVINA} 🕵️")
            adivina = int(input(Fore.CYAN + "🔢 Adivina un número: "))

            # Valida si el número está dentro del rango permitido
            if adivina < RANGO_NUMERO_SECRETO[0] or adivina > RANGO_NUMERO_SECRETO[1]:
                msg.mostrar_error_numero_valido(RANGO_NUMERO_SECRETO[0], RANGO_NUMERO_SECRETO[1])
                continue

            # Verifica si el número adivinado es el correcto
            if adivina == numero_secreto:
                print(Fore.GREEN + Style.BRIGHT + f"🎉 ¡Correcto! Has adivinado el número {numero_secreto}. 🎉")
                msg.mostrar_mensaje_victoria()  # Mensaje de victoria
                break

            # Informa si el número es mayor o menor que el secreto
            msg.mostrar_mensaje_adivinanza(numero_secreto, adivina)
            intentos -= 1

            # Si no quedan intentos, el jugador pierde
            if intentos == 0:
                print(Fore.RED + f"❌ ¡Has perdido! El número secreto era: {numero_secreto}. ❌")
            else:
                msg.mostrar_intentos_restantes(intentos)  # Informa cuántos intentos quedan

        except ValueError:
            # Maneja la excepción cuando el jugador no ingresa un número válido
            print(Fore.RED + "❌ Por favor, ingresa un número válido. ❌")

# Juego: Piedra, Papel o Tijeras
def piedra_papel_tijeras():
    opciones = ['piedra', 'papel', 'tijeras']  # Opciones válidas del juego
    gana_a = {'piedra': 'tijeras', 'papel': 'piedra', 'tijeras': 'papel'}  # Relaciones de victoria
    puntos_jugador = 0
    puntos_computadora = 0

    # Muestra el mensaje de bienvenida y las reglas del juego
    msg.mostrar_mensaje_bienvenida("'Piedra, Papel o Tijeras'")
    print(Fore.YELLOW + f"🎯 El primer jugador en ganar {PUNTOS_GANAR_PPT} rondas será el ganador. 🎯")

    # Bucle principal del juego
    while puntos_jugador < PUNTOS_GANAR_PPT and puntos_computadora < PUNTOS_GANAR_PPT:
        print(Fore.CYAN + f"\n🌟 Puntuación - Tú: {puntos_jugador} | Computadora: {puntos_computadora} 🌟")
        jugador = input(Fore.CYAN + "🧐 Elige piedra, papel o tijeras: ").lower()

        # Valida la opción del jugador
        if jugador not in opciones:
            print(Fore.YELLOW + "⚠️ Opción inválida, por favor elige piedra, papel o tijeras. ⚠️")
            continue

        # Elección aleatoria de la computadora
        computadora = random.choice(opciones)
        print(Fore.CYAN + f"💻 La computadora elige: {computadora}")

        # Verifica el resultado de la ronda
        if jugador == computadora:
            print(Fore.YELLOW + "🤝 ¡Empate! Nadie gana esta ronda. 🤝")
        elif gana_a[jugador] == computadora:
            print(Fore.GREEN + Style.BRIGHT + f"🎉 ¡Ganaste esta ronda! {jugador.capitalize()} vence a {computadora}. 🎉")
            puntos_jugador += 1
        else:
            print(Fore.RED + f"💥 ¡La computadora ganó esta ronda! {computadora.capitalize()} vence a {jugador}. 💥")
            puntos_computadora += 1

        print("=" * 70)

    # Muestra el mensaje final según el ganador
    if puntos_jugador == PUNTOS_GANAR_PPT:
        time.sleep(2)
        msg.mostrar_mensaje_victoria()
    else:
        time.sleep(2)
        msg.mostrar_mensaje_derrota()

# Juego: Ahorcado
def ahorcado():
    palabras = tl.leer_palabras_csv('csv/palabras.csv')  # Lee las palabras desde un archivo CSV
    if not palabras:
        print(Fore.RED + "⚠️ No se encontraron palabras en el archivo CSV. Terminando el juego. ⚠️")
        return

    palabra = random.choice(palabras)  # Selecciona una palabra aleatoria
    intentos = len(palabra) * 2  # Calcula el número de intentos en función de la longitud de la palabra
    palabra_mostrada = ["❌"] * len(palabra)  # Palabra a mostrar (con letras ocultas)
    letras_adivinadas = set()  # Conjunto para rastrear letras ya adivinadas

    # Muestra el mensaje de bienvenida y las reglas del juego
    msg.mostrar_mensaje_bienvenida("Ahorcado")
    print(Fore.CYAN + f"🔮 Tienes {intentos} intentos para adivinar la palabra. 🔮")
    print("=" * 70)

    # Bucle principal del juego
    while intentos > 0 and "❌" in palabra_mostrada:
        print(Fore.YELLOW + "\nPalabra: " + " ".join(palabra_mostrada))
        letra = input(Fore.CYAN + "Adivina una letra: ").lower()
        print("=" * 70)

        # Valida si la entrada es una letra
        if len(letra) != 1 or not letra.isalpha():
            print(Fore.RED + "⚠️ Por favor, ingresa una sola letra válida. ⚠️")
            continue

        # Verifica si la letra ya fue adivinada
        if letra in letras_adivinadas:
            print(Fore.YELLOW + "⚠️ Ya has adivinado esa letra. Intenta con otra. ⚠️")
            continue

        letras_adivinadas.add(letra)

        # Verifica si la letra está en la palabra
        if letra in palabra:
            msg.mostrar_mensaje_palabra_adivinada(letra, palabra_mostrada)
            for idx, char in enumerate(palabra):
                if char == letra:
                    palabra_mostrada[idx] = letra
        else:
            intentos -= 1
            msg.mostrar_mensaje_palabra_incorrecta(letra, intentos)

        # Verifica si el jugador ha ganado o perdido
        if "❌" not in palabra_mostrada:
            msg.mostrar_mensaje_victoria()
            print(Fore.GREEN + f"🎉 ¡Felicidades! La palabra era: {palabra}. 🎉")
        elif intentos == 0:
            print(Fore.RED + f"❌ Has perdido. La palabra era: {palabra}. ❌")
