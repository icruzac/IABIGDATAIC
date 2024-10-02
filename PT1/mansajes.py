from colorama import Fore, Style

# Muestra el mensaje de bienvenida con el nombre del juego
def mostrar_mensaje_bienvenida(juego):
    print(Fore.MAGENTA + Style.BRIGHT + "\n" + "="*70)  # Línea decorativa
    print(Fore.YELLOW + f"🎮 ¡Bienvenido a {juego}! 🎮")  # Mensaje de bienvenida
    print(Fore.MAGENTA + Style.BRIGHT + "="*70)  # Línea decorativa

# Muestra un mensaje de victoria cuando el jugador gana
def mostrar_mensaje_victoria():
    print(Fore.GREEN + Style.BRIGHT + "🏆 ¡Felicidades! Ganaste el juego. 🏆")  # Mensaje de victoria

# Muestra un mensaje de derrota cuando la computadora gana
def mostrar_mensaje_derrota():
    print(Fore.RED + Style.BRIGHT + "💻 ¡La computadora ganó el juego! 💻")  # Mensaje de derrota

# Informa al jugador cuántos intentos le quedan
def mostrar_intentos_restantes(intentos):
    print(Fore.CYAN + f"🔄 Te quedan {intentos} intentos. 🔄")  # Mensaje de intentos restantes

# Muestra un mensaje de error cuando el número ingresado está fuera del rango permitido
def mostrar_error_numero_valido(rango_min, rango_max):
    print(Fore.YELLOW + f"⚠️ Por favor, ingresa un número entre {rango_min} y {rango_max}. ⚠️")  # Advertencia de rango

# Informa si el número adivinado es mayor o menor que el número secreto
def mostrar_mensaje_adivinanza(numero_secreto, adivina):
    if adivina < numero_secreto:
        print(Fore.CYAN + "📈 El número secreto es mayor. 📈")  # El número secreto es mayor
    elif adivina > numero_secreto:
        print(Fore.RED + "📉 El número secreto es menor. 📉")  # El número secreto es menor

# Muestra un mensaje cuando el jugador adivina correctamente una letra en el juego de palabras
def mostrar_mensaje_palabra_adivinada(letra, palabra_mostrada):
    print(Fore.GREEN + f"🎉 ¡Bien hecho! La letra '{letra}' está en la palabra. 🎉")  # Acierto de la letra
    print(Fore.CYAN + "Palabra actual: " + " ".join(palabra_mostrada))  # Muestra la palabra con los aciertos

# Informa al jugador cuando la letra ingresada no está en la palabra y reduce los intentos
def mostrar_mensaje_palabra_incorrecta(letra, intentos):
    print(Fore.RED + f"❌ La letra '{letra}' no está en la palabra. ❌")  # Letra incorrecta
    print(Fore.CYAN + f"🔄 Intentos restantes: {intentos} 🔄")  # Muestra los intentos restantes
