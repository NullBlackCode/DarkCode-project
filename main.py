import core.menu_main
import modules.crack_modules.menu_crack
import os
from colorama import Fore
import time
def main():
    while True:
        try:
            os.system("clear" or "cls")
            print(core.menu_main.banner_main)
            user_enter = int(input(Fore.RED + "~>"))
            if user_enter == 1:
                os.system("clear" or "cls")
                print(Fore.LIGHTBLUE_EX + "Please white...")
                time.sleep(2)
                modules.crack_modules.menu_crack.main.main_code()
                break
            else:
                print(Fore.RED + "Not Number try again (ENTER)")
                input()
        except KeyboardInterrupt:
            print(Fore.LIGHTRED_EX + "\nEXIT\n")
            break
if __name__ == "__main__":
    main()