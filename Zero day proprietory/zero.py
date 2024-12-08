import sys,os
from colorama import Fore

print(Fore.MAGENTA+"""
――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――
 _______  _______  _______  _______         _______ __________________ _______  _______  _        _______  ______    
/ ___   )(  ____ \(  ____ )(  ___  )       (  ___  )\__   __/\__   __/(  ___  )(  ____ \| \    /\(  ____ \(  ____ )  
\/   )  || (    \/| (    )|| (   ) |       | (   ) |   ) (      ) (   | (   ) || (    \/|  \  / /| (    \/| (    )|  
    /   )| (__    | (____)|| |   | | _____ | (___) |   | |      | |   | (___) || |      |  (_/ / | (__    | (____)|
   /   / |  __)   |     __)| |   | |(_____)|  ___  |   | |      | |   |  ___  || |      |   _ (  |  __)   |     __)
  /   /  | (      | (\ (   | |   | |       | (   ) |   | |      | |   | (   ) || |      |  ( \ \ | (      | (\ (   
 /   (_/\| (____/\| ) \ \__| (___) |       | )   ( |   | |      | |   | )   ( || (____/\|  /  \ \| (____/\| ) \ \__
(_______/(_______/|/   \__/(_______)       |/     \|   )_(      )_(   |/     \|(_______/|_/    \/(_______/|/   \__/
                                                                                                                   
――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――
                                                                 
BY: Scynrays and Asjad
""")

def display_menu():
    print(Fore.GREEN + """
    1: Zero-Tool (Hacking Tools)      
    """)

def execute_command(command):
    if command == '1':
        os.system('cmd /k "python Zero-Tool/zero-tool.py"' if os.name == 'nt' else 'python Zero-Tool/zero-tool.py')
    else:
        print('Invalid option! Just Press one dude its not that hard')

while True:
    display_menu()
    command = input('> ')

    if command.lower() == 'exit':
        break

    execute_command(command)
