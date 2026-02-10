import socket
import sys
from datetime import datetime

# ==========================================
# SCANNER DE PORTS BASIQUE (TCP)
# Auteur : Mouhamadou Diouf
# Usage : Outil éducatif pour tester la sécurité réseau
# ==========================================

def scan_target(target):
    try:
        # Résolution de l'adresse IP (si on donne un nom de domaine)
        ip = socket.gethostbyname(target)
    except socket.gaierror:
        print("\n[!] Erreur : Impossible de résoudre le nom de domaine.")
        sys.exit()

    # Affichage d'une bannière de démarrage
    print("-" * 50)
    print(f"Cible à scanner : {ip}")
    print(f"Démarrage du scan : {datetime.now()}")
    print("-" * 50)

    try:
        # On scanne les ports de 1 à 1024 (les ports standards)
        # Tu peux changer 1025 par 65535 pour tout scanner (mais c'est plus long)
        for port in range(1, 1025):
            # Création du socket (IPv4, TCP)
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            
            # Définition du timeout (0.5 seconde pour aller vite)
            socket.setdefaulttimeout(0.5)
            
            # Tentative de connexion (retourne 0 si le port est OUVERT)
            result = s.connect_ex((ip, port))
            
            if result == 0:
                print(f"[+] Port {port} est OUVERT")
            
            s.close()
            
    except KeyboardInterrupt:
        print("\n[!] Scan interrompu par l'utilisateur.")
        sys.exit()
        
    except socket.error:
        print("\n[!] Impossible de se connecter au serveur.")
        sys.exit()

# Lancement du script
if __name__ == "__main__":
    # Demande à l'utilisateur d'entrer une IP ou un site
    target_input = input("Entrez l'adresse IP ou le domaine à scanner (ex: 127.0.0.1) : ")
    scan_target(target_input)
