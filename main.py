import ipaddress
import math

def validar_ip(ip):
    try:
        ipaddress.IPv4Address(ip)
        return True
    except ValueError:
        return False

def validar_prefijo(prefijo):
    return 1 <= prefijo <= 30

def calcular_prefijo_desde_hosts(num_hosts):
    return 32 - math.ceil(math.log2(num_hosts + 2))

def calcular_wildcard(mascara):
    mascara_ip = ipaddress.IPv4Address(mascara)
    wildcard = ipaddress.IPv4Address(int(mascara_ip) ^ 0xFFFFFFFF)
    return str(wildcard)

def calcular_vlsm(ip_base, prefijo_principal, hosts_subredes):
    red_principal = ipaddress.ip_network(f"{ip_base}/{prefijo_principal}", strict=False)
    subredes_generadas = []
    red_actual = ip_base

    hosts_subredes_ordenados = sorted(hosts_subredes, reverse=True)

    for i, num_hosts in enumerate(hosts_subredes_ordenados):
        prefijo = calcular_prefijo_desde_hosts(num_hosts)

        try:
            subred = ipaddress.ip_network(f"{red_actual}/{prefijo}", strict=False)
        except ValueError:
            return f"Error: No se puede crear una subred válida desde {red_actual} con prefijo /{prefijo}."
        
        if not subred.subnet_of(red_principal):
            return f"Error: La subred {subred} no está dentro de la red principal {red_principal}."

        subredes_generadas.append({
            "Subred": f"Subred {i + 1}",
            "Dirección de red": str(subred.network_address),
            "Máscara de red": str(subred.netmask),
            "Wildcard mask": calcular_wildcard(subred.netmask),
            "Prefijo": f"/{subred.prefixlen}",
            "Rango de hosts": f"{list(subred.hosts())[0]} - {list(subred.hosts())[-1]}",
            "Broadcast": str(subred.broadcast_address),
            "Hosts necesarios": num_hosts,
            "Hosts disponibles": (2 ** (32 - prefijo)) - 2
        })
        
        red_actual = str(subred.broadcast_address + 1)

    return subredes_generadas

def imprimir_resultados(resultado):
    if isinstance(resultado, str):
        print("\n", resultado)
    else:
        print("\nResultados de la Calculadora de Subneteo VLSM")
        for subred in resultado:
            print(f"Subred: {subred['Subred']}")
            print(f"  Dirección de red: {subred['Dirección de red']}")
            print(f"  Máscara de red: {subred['Máscara de red']}")
            print(f"  Wildcard mask: {subred['Wildcard mask']}")
            print(f"  Prefijo: {subred['Prefijo']}")
            print(f"  Rango de hosts: {subred['Rango de hosts']}")
            print(f"  Broadcast: {subred['Broadcast']}")
            print(f"  Hosts necesarios: {subred['Hosts necesarios']}")
            print(f"  Hosts disponibles: {subred['Hosts disponibles']}")

def calcular_enlaces_router(ip_base, prefijo_principal, num_enlaces):
    red_principal = ipaddress.ip_network(f"{ip_base}/{prefijo_principal}", strict=False)
    enlaces_generados = []
    red_actual = red_principal.network_address

    for i in range(num_enlaces):
        try:
            subred = ipaddress.ip_network(f"{red_actual}/30", strict=False)
        except ValueError:
            return f"Error: No se puede crear un enlace válido desde {red_actual}."
        
        if not subred.subnet_of(red_principal):
            return f"Error: El enlace {subred} no está dentro de la red principal {red_principal}."

        enlaces_generados.append({
            "Enlace": f"Enlace {i + 1}",
            "Dirección de red": str(subred.network_address),
            "Máscara de red": str(subred.netmask),
            "Wildcard mask": calcular_wildcard(subred.netmask),
            "Prefijo": "/30",
            "IPs utilizables": f"{list(subred.hosts())[0]} - {list(subred.hosts())[1]}",
            "Broadcast": str(subred.broadcast_address)
        })
        
        red_actual = subred.broadcast_address + 1

    return enlaces_generados

def imprimir_enlaces(resultado):
    if isinstance(resultado, str):
        print("\n", resultado)
    else:
        print("\nResultados de la Calculadora de Enlaces de Router")
        for enlace in resultado:
            print(f"Enlace: {enlace['Enlace']}")
            print(f"  Dirección de red: {enlace['Dirección de red']}")
            print(f"  Máscara de red: {enlace['Máscara de red']}")
            print(f"  Wildcard mask: {enlace['Wildcard mask']}")
            print(f"  Prefijo: {enlace['Prefijo']}")
            print(f"  IPs utilizables: {enlace['IPs utilizables']}")
            print(f"  Broadcast: {enlace['Broadcast']}")

def menu_vlsm():
    while True:
        print("\nCalculadora de Subneteo VLSM")
        
        ip_base = input("Ingrese la dirección IP base: ")
        if not validar_ip(ip_base):
            print("Error: La IP ingresada no es válida.")
            continue
        
        while True:
            try:
                prefijo_principal = int(input("Ingrese el prefijo principal de la red: "))
                if validar_prefijo(prefijo_principal):
                    break
                else:
                    print("Error: El prefijo debe estar entre 1 y 30.")
            except ValueError:
                print("Error: Ingrese un número entero válido.")
        
        while True:
            try:
                cantidad_subredes = int(input("¿Cuántas subredes desea calcular?: "))
                if cantidad_subredes < 1:
                    print("Error: Debe ingresar al menos una subred.")
                else:
                    break
            except ValueError:
                print("Error: Ingrese un número entero válido.")
        
        hosts_subredes = []
        for i in range(cantidad_subredes):
            while True: 
                try:
                    num_hosts = int(input(f"Ingrese la cantidad de hosts para la subred {i + 1}: "))
                    if num_hosts > 0:
                        hosts_subredes.append(num_hosts)
                        break
                    else:
                        print("Error: La cantidad de hosts debe ser mayor a 0.")
                except ValueError:
                    print("Error: Ingrese un número entero válido.")
        
        resultado = calcular_vlsm(ip_base, prefijo_principal, hosts_subredes)
        imprimir_resultados(resultado)
        
        calc_enlaces = input("\n¿Desea calcular enlaces de routers? s/n: ")
        if calc_enlaces.lower() == 's':
            menu_enlaces()
        
        salir = input("\n¿Desea realizar otro cálculo VLSM? s/n: ")
        if salir.lower() == 'n':
            break

def menu_enlaces():
    primera_vez = True
    while True:
        if primera_vez:
            print("\nCalculadora de Enlaces de Router")
            primera_vez = False
        
        ip_base = input("Ingrese la dirección IP base: ")
        if not validar_ip(ip_base):
            print("Error: La IP ingresada no es válida.")
            continue
        
        while True:
            try:
                prefijo_principal = int(input("Ingrese el prefijo principal de la red: "))
                if validar_prefijo(prefijo_principal):
                    break
                else:
                    print("Error: El prefijo debe estar entre 1 y 30.")
            except ValueError:
                print("Error: Ingrese un número entero válido.")
        
        while True:
            try:
                num_enlaces = int(input("¿Cuántos enlaces entre routers necesita?: "))
                if num_enlaces < 1:
                    print("Error: Debe ingresar al menos un enlace.")
                else:
                    break
            except ValueError:
                print("Error: Ingrese un número entero válido.")
        
        resultado = calcular_enlaces_router(ip_base, prefijo_principal, num_enlaces)
        imprimir_enlaces(resultado)
        
        salir = input("\n¿Desea realizar otro cálculo? s/n: ")
        if salir.lower() == 'n':
            break

def main():
    while True:
        print("\nCALCULADORA DE REDES")
        print("1. Calculadora de Subneteo VLSM")
        print("2. Calculadora de Enlaces de Router")
        print("3. Salir")
        
        opcion = input("\nSeleccione una opción: ")
        
        if opcion == "1":
            menu_vlsm()
        elif opcion == "2":
            menu_enlaces()
        elif opcion == "3":
            print("Saliendo...")
            break
        else:
            print("Opción no válida")

if __name__ == "__main__":
    main()
