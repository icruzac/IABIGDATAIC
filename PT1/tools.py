from colorama import Fore, Style
import time
import os
import csv

# Función para leer palabras desde un archivo CSV
def leer_palabras_csv(archivo):
    """
    Lee las palabras de un archivo CSV y las devuelve en una lista.
    Si el archivo no se encuentra, se muestra un mensaje de error.

    :param archivo: Ruta del archivo CSV que contiene las palabras.
    :return: Lista de palabras leídas desde el archivo CSV.
    """
    palabras = []
    try:
        with open(archivo, mode='r', newline='') as file:
            reader = csv.reader(file)
            for fila in reader:
                palabra = fila[0].strip()  # Eliminamos espacios en blanco alrededor de la palabra
                if palabra:
                    palabras.append(palabra)  # Agregar palabra solo si no está vacía
    except FileNotFoundError:
        print(Fore.RED + "⚠️ Archivo no encontrado. Asegúrate de que el archivo CSV está en la ruta correcta. ⚠️")
    return palabras

# Función para mostrar una animación de carga
def loading_animation():
    """
    Muestra una animación de carga en la terminal con barras de progreso.
    """
    animation = [
        "[■□□□□□□□□□]", "[■■□□□□□□□□]", "[■■■□□□□□□□]", "[■■■■□□□□□□]",
        "[■■■■■□□□□□]", "[■■■■■■□□□□]", "[■■■■■■■□□□]", "[■■■■■■■■□□]",
        "[■■■■■■■■■□]", "[■■■■■■■■■■]"
    ]
    for frame in animation:
        time.sleep(0.1)  # Pausa para crear efecto de animación
        print("\r" + Fore.MAGENTA + frame, end="")  # Sobrescribe la línea actual
    print("\n")  # Salto de línea al finalizar

# Función para limpiar la pantalla
def limpiar_pantalla():
    """
    Limpia la pantalla de la terminal, compatible con Windows y Unix.
    """
    os.system('cls' if os.name == 'nt' else 'clear')

# Función para mostrar texto con efecto de escritura
def efecto_escritura(texto, velocidad=0.02):
    """
    Muestra texto en la terminal con un efecto de escritura, donde cada letra aparece con un retraso.

    :param texto: El texto que se va a mostrar.
    :param velocidad: Tiempo de retraso entre cada letra (en segundos).
    """
    for letra in texto:
        print(letra, end='', flush=True)
        time.sleep(velocidad)
    print()  # Salto de línea al finalizar

# Función para mostrar el menú principal
def mostrar_menu():
    """
    Muestra el menú principal del juego en la terminal con un diseño gráfico.
    """
    limpiar_pantalla()
    print(Fore.MAGENTA + "╔" + "═" * 40 + "╗")
    print(Fore.CYAN + Style.BRIGHT + "║ 🎮 Bienvenido al Juego de Aventura 🎮  ║")
    print(Fore.MAGENTA + "╚" + "═" * 40 + "╝")
    print(Fore.YELLOW + "║ 1. Adivina el Número                 ║")
    print(Fore.YELLOW + "║ 2. Piedra, Papel o Tijeras           ║")
    print(Fore.YELLOW + "║ 3. Ahorcado                          ║")
    print(Fore.YELLOW + "║ 4. Salir                             ║")
    print(Fore.MAGENTA + "╚" + "═" * 40 + "╝")
