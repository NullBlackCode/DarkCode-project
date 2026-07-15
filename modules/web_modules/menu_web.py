import os
from colorama import Fore
import time

class main:
    def clear_screen():
        os.system("clear")

    def show_banner():
        banner = f"""{Fore.LIGHTMAGENTA_EX}
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠛⣿⠛⠉⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣈⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀(1) > XSS (Cross site scripting) auto scanner
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⡁⠀⠀⠀⠀⠀⠀⠀⠀⠀(2) > SQLi (SQL injection) auto
⠀⠀⠀⠀⣴⣤⡀⠀⠀⠀⠀⣭⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀(3) > Fuzzer web auto scanner
⠀⠀⠀⠀⢸⡀⠈⠳⣄⠀⠀⠼⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀(4) > Subdomain auto scanner
⠀⢠⠀⠀⠀⢳⠀⠀⠈⠢⡀⠶⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀(5) > LFI/RFI (File Inclusion) Scanner
⠉⢻⠉⢀⠀⠀⢣⠀⠀⠀⠈⢼⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀(6) > CSRF (Cross Site Request Forgery) Tester
⠀⠀⠀⠺⠃⠀⠀⠡⠀⠀⠀⣸⠐⡀⠀⠀⠀⠀⠀⠀⠀⠀(7) > SSTI (Server Side Template Injection) Scanner
⠀⠀⠀⠀⠀⠀⠀⠀⠱⡀⠀⣿⡀⢈⡄⠀⠀⠀⠀⠀⠀⠀(8) > XXE (XML External Entity) Scanner
⠀⠀⠀⠀⠀⠀⠀⠀⣀⣹⣾⣿⣷⣏⣀⠀⠀⠀⠀⠀⠀⠀(9) > Open Redirect Checker
⠀⠀⠀⠉⠉⠉⠉⠙⠛⢻⣿⣶⣿⡟⠛⠋⠉⠉⠉⠉⠁⠀(10) >  WAF Detector
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠞⠹⣿⢏⠳⡄⠀⠀⠀⠀⠀⠀⠀(11) > Headers & Security Analyzer
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⠀⠢⠀⠀⠀⠰⡧⠀⠀⠀(12) > SSL/TLS Scanner
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⡀⢸⠀⠀⠡⡀⠀⠀⠀⠤⣾⠤(13) > CloudFlare Bypass Checker
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢬⠀⠀⠀⠱⡀⠀⠀⠀⠘⠀(14) > Admin Login Bruteforce
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠑⢄⠀⠀⢣⠀⠀⠀⠀⠀(15) > Web Cache Poisoning Tester
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠶⠀⠀⠓⢤⣀⡇⠀⠀⠀⠀(16) > JWT Token Cracker
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠶⠀⠀⠀⠀⠈⠁⠀⠀⠀⠀(17) > Host Header Injection Scanner
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣛⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀(18) > Web Cache Deception Scanner
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⡁⠀⠀⠀⠀⠀⠀⠀⠀⠀(19) > Web Server & Version Fingerprinting
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢩⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀(20) > 403/401 Bypass Auto
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⣤⣿⣤⣀⠀⠀⠀⠀⠀⠀⠀⠀(21) > WebSocket Security Scanner
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡻⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀(0) EXIT
"""
        print(banner)
    def user_entry():
            main.clear_screen()
            main.show_banner()
            user = int(input("~/> "))
            if user == 1:
                pass
            elif user == 2:
                 pass
            elif user == 3:
                 pass
            elif user == 4:
                 pass
            elif user == 5:
                 pass
            elif user == 6:
                 pass
            elif user == 7:
                 pass
            elif user == 8:
                 pass
            elif user == 9:
                 pass
            elif user == 10:
                 pass
            elif user == 11:
                 pass
            elif user == 12:
                 pass
            elif user == 13:
                 pass
            elif user == 14:
                 pass
            elif user == 15:
                 pass
            elif user == 16:
                 pass
            elif user == 17:
                 pass
            elif user == 18:
                 pass
            elif user == 19:
                 pass
            elif user == 20:
                 pass
            elif user == 21:
                 pass
            elif user == 0:
                 print(Fore.RED + "\nEXIT\n")
                 exit()
            else:
                print(Fore.RED + "Not option, try again")
                time.sleep(2)
                main.main_code()
    def main_code():
         while True:
              main.clear_screen()
              main.show_banner()
              main.user_entry()
if __name__ == "__main__":
    main.main_code()