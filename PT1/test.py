import time
from colorama import Fore, init
import juegos as jg
import tools as tl

init(autoreset=True)

# Función principal
def main():
    while True:
        tl.loading_animation()
        tl.mostrar_menu()
        try:
            opcion = int(input(Fore.CYAN + "Selecciona una opción (1-4): "))

            if opcion == 1:
                tl.loading_animation()
                jg.adivina_el_numero()
            elif opcion == 2:
                tl.loading_animation()
                jg.piedra_papel_tijeras()
            elif opcion == 3:
                tl.loading_animation()
                jg.ahorcado()
            elif opcion == 4:
                print(Fore.GREEN + "¡Gracias por jugar! Hasta la próxima. 😊")
                break
            else:
                print(Fore.RED + "⚠️ Opción inválida. Por favor elige entre 1 y 4. ⚠️")
        
        except ValueError:
            print(Fore.RED + "⚠️ Por favor, ingresa un número válido. ⚠️")
            time.sleep(1)  # Pausa para que el usuario vea el mensaje

if __name__ == "__main__":
    main()

