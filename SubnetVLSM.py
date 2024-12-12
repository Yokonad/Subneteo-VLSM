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

def calcular_vlsm(ip_base, prefijo_principal, hosts_subredes):
    red_principal = ipaddress.ip_network(f"{ip_base}/{prefijo_principal}", strict=False)
    subredes_generadas = []
    red_actual = red_principal.network_address

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
            "Prefijo": f"/{subred.prefixlen}",
            "Rango de hosts": f"{list(subred.hosts())[0]} - {list(subred.hosts())[-1]}",
            "Broadcast": str(subred.broadcast_address),
            "Hosts necesarios": num_hosts,
            "Hosts disponibles": (2 ** (32 - prefijo)) - 2
        })
        
        red_actual = subred.broadcast_address + 1

    return subredes_generadas

def imprimir_resultados(resultado):
    if isinstance(resultado, str):
        print("\n", resultado)
    else:
        print("\nResultados de la Calculadora de Subneteo VLSM:")
        print("=" * 60)
        for subred in resultado:
            print(f"Subred: {subred['Subred']}")
            print(f"  Dirección de red: {subred['Dirección de red']}")
            print(f"  Máscara de red: {subred['Máscara de red']}")
            print(f"  Prefijo: {subred['Prefijo']}")
            print(f"  Rango de hosts: {subred['Rango de hosts']}")
            print(f"  Broadcast: {subred['Broadcast']}")
            print(f"  Hosts necesarios: {subred['Hosts necesarios']}")
            print(f"  Hosts disponibles: {subred['Hosts disponibles']}")
            print("-" * 60)

def main():
    while True:
        print("=" * 60)
        print("          Calculadora de Subneteo VLSM")
        print("=" * 60)
        
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
        
        salir = input("\n¿Desea realizar otro cálculo? (c para continuar, s para salir): ")
        if salir.lower() == "s":
            print("Saliendo del programa...")
            break

if __name__ == "__main__":
    main()
