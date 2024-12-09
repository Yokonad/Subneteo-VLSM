import ipaddress

def validar_ip(ip):
    try:
        ipaddress.IPv4Address(ip)
        return True
    except ValueError:
        return False

def validar_prefijo(prefijo):
    return 1 <= prefijo <= 30

def calcular_vlsm(ip_base, prefijo_principal, prefijos_subredes):
    red_principal = ipaddress.ip_network(f"{ip_base}/{prefijo_principal}", strict=False)
    subredes_generadas = []
    red_actual = red_principal.network_address

    for i, prefijo in enumerate(prefijos_subredes):
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
            print(f"\033[1;34mSubred: {subred['Subred']}\033[0m")
            print(f"  \033[1;33mDirección de red:\033[0m {subred['Dirección de red']}")
            print(f"  \033[1;33mMáscara de red:\033[0m {subred['Máscara de red']}")
            print(f"  \033[1;33mPrefijo:\033[0m {subred['Prefijo']}")
            print(f"  \033[1;33mRango de hosts:\033[0m {subred['Rango de hosts']}")
            print(f"  \033[1;33mBroadcast:\033[0m {subred['Broadcast']}")
            print(f"  \033[1;33mHosts disponibles:\033[0m {subred['Hosts disponibles']}")
            print("-" * 60)

def main():
    while True:
        print("=" * 60)
        print("\033[1;32m          Calculadora de Subneteo VLSM\033[0m")
        print("=" * 60)
        
        ip_base = input("Ingrese la dirección IP base: ")
        if not validar_ip(ip_base):
            print("\033[1;31mError: La IP ingresada no es válida.\033[0m")
            continue
        
        while True:
            try:
                prefijo_principal = int(input("Ingrese el prefijo principal de la red: "))
                if validar_prefijo(prefijo_principal):
                    break
                else:
                    print("\033[1;31mError: El prefijo debe estar entre 1 y 30.\033[0m")
            except ValueError:
                print("\033[1;31mError: Ingrese un número entero válido.\033[0m")
        
        while True:
            try:
                cantidad_subredes = int(input("¿Cuántas subredes desea calcular?: "))
                if cantidad_subredes < 1:
                    print("\033[1;31mError: Debe ingresar al menos una subred.\033[0m")
                else:
                    break
            except ValueError:
                print("\033[1;31mError: Ingrese un número entero válido.\033[0m")
        
        prefijos_subredes = []
        for i in range(cantidad_subredes):
            while True:
                try:
                    prefijo = int(input(f"Ingrese el prefijo para la subred {i + 1}: "))
                    if validar_prefijo(prefijo):
                        prefijos_subredes.append(prefijo)
                        break
                    else:
                        print("\033[1;31mError: El prefijo debe estar entre 1 y 30.\033[0m")
                except ValueError:
                    print("\033[1;31mError: Ingrese un número entero válido.\033[0m")
        
        resultado = calcular_vlsm(ip_base, prefijo_principal, prefijos_subredes)
        imprimir_resultados(resultado)
        
        salir = input("\n¿Desea realizar otro cálculo? (c para continuar, s para salir): ")
        if salir.lower() == "s":
            print("\033[1;32mSaliendo del programa...\033[0m")
            break

if __name__ == "__main__":
    main()
