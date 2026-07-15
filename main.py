import core.menu_main
import modules.crack_modules.menu_crack
import modules.web_modules.menu_web
import os
from colorama import Fore
import time
def clear_screen():
    os.system("clear")

def main():
    while True:
        try:
            clear_screen()
            print(core.menu_main.banner_main)
            user_enter = int(input(Fore.RED + "~>"))
            if user_enter == 1:
                clear_screen()
                print(Fore.LIGHTBLUE_EX + "Please white...")
                time.sleep(0.60)
                modules.crack_modules.menu_crack.main.main_code()
                break
            elif user_enter == 2:
                clear_screen()
                print(Fore.LIGHTBLUE_EX + "Please white...")
                time.sleep(0.60)
                modules.web_modules.menu_web.main.main_code()
                break
            else:
                print(Fore.RED + "Not Number try again (ENTER)")
                input()
        except KeyboardInterrupt:
            print(Fore.LIGHTRED_EX + "\nEXIT\n")
            break
if __name__ == "__main__":
    main()