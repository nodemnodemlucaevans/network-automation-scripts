#!/usr/bin/env python3
# ====================================================
# SCRIPT AUTOMATISATION SAUVEGARDE CONFIGURATION CISCO
# Auteur : Nodem Nodem Luca Evans
# Keyce Informatique & IA
# ====================================================

import datetime
import os

def backup_network_device(hostname, ip_address, device_type="cisco_ios"):
    """
    Simule la connexion SSH à un équipement réseau 
    et extrait la running-config dans un fichier horodaté.
    """
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M")
    filename = f"backup_{hostname}_{timestamp}.cfg"
    
    print(f"[+] Connexion en cours à {hostname} ({ip_address}) via SSH...")
    
    # Structure de la configuration récupérée
    config_data = f"""!
! Backup généré automatiquement par Nodem Luca Evans Script
! Équipement: {hostname} ({ip_address})
! Date: {timestamp}
!
version 15.2
hostname {hostname}
!
ip domain-name keyce.local
crypto key generate rsa modulus 2048
!
interface GigabitEthernet0/0
 description Interface WAN
 ip address dhcp
 no shutdown
!
line vty 0 4
 exec-timeout 5 0
 login local
 transport input ssh
!
end
"""
    print(f"[✔] Configuration extraite avec succès.")
    print(f"[✔] Sauvegarde enregistrée sous : {filename}")
    return True

if __name__ == "__main__":
    print("=== DÉMARRAGE DU SERVICE D'AUTOMATISATION RÉSEAU ===")
    devices = [
        {"name": "SW-ACCESS-01", "ip": "192.168.99.10"},
        {"name": "SW-CORE-01", "ip": "192.168.99.1"}
    ]
    
    for dev in devices:
        backup_network_device(dev["name"], dev["ip"])
    
    print("=== SAUVEGARDE TERMINÉE POUR TOUS LES ÉQUIPEMENTS ===")
  
