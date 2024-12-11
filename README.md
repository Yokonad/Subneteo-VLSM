
# 🖥️ **Calculadora de Subneteo VLSM en Python** 🌐

## 📜 Descripción

Este proyecto es una **calculadora de subneteo VLSM (Variable Length Subnet Mask)** implementada en **Python**. La herramienta permite realizar cálculos detallados para dividir una red principal en subredes más pequeñas, de manera eficiente y adaptada a los requerimientos de cada caso.

**Características principales**:
- Validación de direcciones IP y prefijos.
- Cálculo dinámico de subredes con tamaños variados.
- Presentación clara de los resultados, incluyendo rangos de hosts, máscaras de red, direcciones de red, y más.

## 🧑‍💻 **¿Qué hace el código?**

El programa realiza los siguientes pasos:
1. **Validación de IP**: Verifica que la IP ingresada sea válida (dirección IPv4).
2. **Validación de Prefijo**: Asegura que el prefijo (máscara de red) esté dentro del rango permitido (1 a 30).
3. **Cálculo de Subredes**: Calcula las subredes necesarias con el prefijo proporcionado y las subdivide en base a los requerimientos de cada subred.
4. **Resultados**: Muestra información sobre cada subred generada, incluyendo:
    - Dirección de red
    - Máscara de red
    - Rango de hosts
    - Dirección de broadcast
    - Hosts disponibles

## 📝 **Código Puntual**

### 1. Validación de la dirección IP

```python
def validar_ip(ip):
    try:
        ipaddress.IPv4Address(ip)
        return True
    except ValueError:
        return False
```

> Esta función verifica si la dirección IP proporcionada es válida (IPv4).

### 2. Validación del Prefijo

```python
def validar_prefijo(prefijo):
    return 1 <= prefijo <= 30
```

> Valida que el prefijo esté entre 1 y 30, que es el rango permitido en IPv4.

### 3. Cálculo de Subredes

```python
def calcular_vlsm(ip_base, prefijo_principal, prefijos_subredes):
    red_principal = ipaddress.ip_network(f"{ip_base}/{prefijo_principal}", strict=False)
    subredes_generadas = []
    red_actual = red_principal.network_address
    ...
```

> Aquí se calculan las subredes con base en la red principal y los prefijos de las subredes solicitadas.

### 4. Impresión de Resultados

```python
def imprimir_resultados(resultado):
    if isinstance(resultado, str):
        print("
", resultado)
    else:
        print("
Resultados de la Calculadora de Subneteo VLSM:")
        print("=" * 60)
        for subred in resultado:
            print(f"Subred: {subred['Subred']}")
            print(f"  Dirección de red: {subred['Dirección de red']}")
            ...
```

> Muestra los resultados en un formato claro y fácil de entender.

## 💡 **Cómo Usarlo**

1. **Paso 1**: Ingresar la dirección IP base.
2. **Paso 2**: Introducir el prefijo principal (máscara de red) para la red.
3. **Paso 3**: Definir la cantidad de subredes y sus respectivos prefijos.
4. **Paso 4**: El programa calculará y mostrará la información de las subredes generadas.

## 🚀 **Licencia**

Este proyecto se distribuye bajo la licencia [MIT](https://choosealicense.com/licenses/mit/).

---

👨‍💻 **Hecho por**: [Tu nombre o tu equipo] ✨

¡Disfruta del uso de esta calculadora de subneteo VLSM! 🚀
