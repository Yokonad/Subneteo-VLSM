# Calculadora de Subneteo VLSM en Python
![Logo](https://i.imgur.com/4Yi4QWM.png)

## Descripción

Este proyecto es una calculadora de subneteo utilizando VLSM (Variable Length Subnet Masking) en Python. El programa permite calcular subredes a partir de una red base con un prefijo principal y subredes con prefijos variables. El objetivo es obtener detalles de las subredes generadas, como la dirección de red, máscara de red, rango de hosts, y más.

## Funciones

### 1. Validación de IP
Valida si la dirección IP proporcionada es válida.

```python
def validar_ip(ip):
    try:
        ipaddress.IPv4Address(ip)
        return True
    except ValueError:
        return False
