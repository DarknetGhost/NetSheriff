import socket
import sys
import time
import os

print("[!]La herramienta puede demorar un poco su uso por la iteracion y verificacion de las IPs\n")
print("Instalando dependencias por favor espere...")
os.system("pip3 install socket > /dev/null 2>&1")
os.system("clear")
menu = """

███╗   ██╗███████╗████████╗███████╗██╗  ██╗███████╗██████╗ ██╗███████╗███████╗
████╗  ██║██╔════╝╚══██╔══╝██╔════╝██║  ██║██╔════╝██╔══██╗██║██╔════╝██╔════╝
██╔██╗ ██║█████╗     ██║   ███████╗███████║█████╗  ██████╔╝██║█████╗  █████╗  
██║╚██╗██║██╔══╝     ██║   ╚════██║██╔══██║██╔══╝  ██╔══██╗██║██╔══╝  ██╔══╝  
██║ ╚████║███████╗   ██║   ███████║██║  ██║███████╗██║  ██║██║██║     ██║     
╚═╝  ╚═══╝╚══════╝   ╚═╝   ╚══════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚═╝╚═╝     ╚═╝     
                                                                              

                            Bienvenido
                Herramienta creada por DarknetGhost
"""

def scan_ports(ip, ports):
    for port in ports:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)
            result = sock.connect_ex((ip, port))
            if result  == 0:
                print(f"Puerto {port} esta abierto en {ip}")
            sock.close()
        except socket.error:
            print("Ocurrio un error mientras conectaba")



print(menu)
print("")

direccion_de_red = input("[+]Ingresar mascara de subred ejemplo 192.168.1: ")
puertos = [21, 22, 23, 25, 53, 80, 101, 110, 443, 3306, 8080]
print("[+]Escaneando las redes, ten paciencia por favor....")

for i in range(1, 255):
    local_ip = f"{direccion_de_red}.{i}"
    scan_ports(local_ip, puertos)

