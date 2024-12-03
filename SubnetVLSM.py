import ipaddress

# Validar si una dirección IP es válida
def validar_ip(ip):
    try:
        ipaddress.ip_network(ip, strict=False)
        return True
    except ValueError:
        return False

# Ajustar la dirección IP al inicio del bloque necesario según el prefijo
def ajustar_direccion(ip_actual, prefijo):
    ip_red = ipaddress.ip_network(f"{ip_actual}/{prefijo}", strict=False)
    return ip_red.network_address

# Calcular las subredes según el método VLSM
def calcular_vlsm(ip_red, prefijos_subredes):
    red_principal = ipaddress.ip_network(ip_red, strict=False)
    subredes_generadas = []
    red_actual = red_principal.network_address

    for i, prefijo in enumerate(prefijos_subredes):
        try:
            subred = ipaddress.ip_network(f"{red_actual}/{prefijo}", strict=False)
        except ValueError:
            return f"Error: No se puede crear una subred válida desde {red_actual} con prefijo /{prefijo}."
        
        # Verificar que la subred está contenida en la red principal
        if not subred.subnet_of(red_principal):
            return f"Error: La subred {subred} no está dentro de la red principal {red_principal}."

        # Agregar subred a la lista
        subredes_generadas.append({
            "Subred": f"Subred {i + 1}",
            "Dirección de red": str(subred.network_address),
            "Máscara de red": str(subred.netmask),
            "Prefijo": f"/{subred.prefixlen}",
            "Rango de hosts": f"{list(subred.hosts())[0]} - {list(subred.hosts())[-1]}",
            "Broadcast": str(subred.broadcast_address),
            "Hosts disponibles": (2 ** (32 - prefijo)) - 2
        })
        
        # Calcular la siguiente red inicial: Continuidad garantizada
        red_actual = subred.broadcast_address + 1

    return subredes_generadas

# Imprimir los resultados de forma estética
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

# Menú principal
def main():
    print("=" * 60)
    print("\033[1;32m          Calculadora de Subneteo VLSM\033[0m")
    print("=" * 60)
    while True:
        ip_red = input("Ingrese la IP inicial para el subneteo VLSM con el prefijo (ejemplo: 192.168.1.0/24): ")
        if validar_ip(ip_red):
            break
        else:
            print("\033[1;31mError: La IP ingresada no es válida.\033[0m")
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
                prefijo = int(input(f"Ingrese el prefijo de la subred {i + 1} (ejemplo: 25): "))
                if prefijo < 1 or prefijo > 30:
                    print("\033[1;31mError: El prefijo debe estar entre 1 y 30.\033[0m")
                else:
                    prefijos_subredes.append(prefijo)
                    break
            except ValueError:
                print("\033[1;31mError: Ingrese un número entero válido.\033[0m")
    resultado = calcular_vlsm(ip_red, prefijos_subredes)
    imprimir_resultados(resultado)

if __name__ == "__main__":
    main()
