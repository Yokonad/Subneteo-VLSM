# CALCULADORA DE SUBNETEO VLSM

## 1. DESCRIPCIÓN DEL PROYECTO

### 1.1 Objetivo
Herramienta de subneteo VLSM (Variable Length Subnet Mask) que permite dividir redes IP de manera eficiente, calculando subredes automáticamente basadas en el número de hosts requeridos.

### 1.2 Características Principales
- Cálculo automático de prefijos
- Validación de direcciones IP
- División de redes con subredes de tamaños variables
- Presentación detallada de información de subredes

## 2. REQUISITOS TÉCNICOS

### 2.1 Entorno
- Python 3.7 o superior
- Módulos requeridos: 
  * ipaddress
  * math

### 2.2 Dependencias
Instalar las dependencias con:
```
pip install ipaddress
```

## 3. ESTRUCTURA DEL CÓDIGO

### 3.1 Funciones Principales

#### 3.1.1 Validación de IP
```python
def validar_ip(ip):
    try:
        ipaddress.IPv4Address(ip)
        return True
    except ValueError:
        return False
```

#### 3.1.2 Cálculo de Prefijo
```python
def calcular_prefijo_desde_hosts(num_hosts):
    return 32 - math.ceil(math.log2(num_hosts + 2))
```

#### 3.1.3 Cálculo VLSM
```python
def calcular_vlsm(ip_base, prefijo_principal, hosts_subredes):
```

## 4. MODO DE USO

### 4.1 Pasos para Usar la Calculadora

1. Ejecutar el script Python
2. Ingresar dirección IP base
3. Introducir prefijo principal de la red
4. Especificar cantidad de subredes
5. Indicar número de hosts para cada subred

### 4.2 Ejemplo de Ejecución

```
Ingrese la dirección IP base: 192.168.1.0
Ingrese el prefijo principal de la red: 24
¿Cuántas subredes desea calcular?: 3
Ingrese la cantidad de hosts para la subred 1: 50
Ingrese la cantidad de hosts para la subred 2: 20
Ingrese la cantidad de hosts para la subred 3: 10
```

## 5. DETALLES TÉCNICOS

### 5.1 Algoritmo de Subneteo
- Ordena subredes de mayor a menor número de hosts
- Calcula prefijos automáticamente
- Asigna direcciones de red secuencialmente
- Optimiza uso de espacio de direcciones IP

### 5.2 Validaciones
- Rango de prefijos: 1 a 30
- Direcciones IPv4 válidas
- Número de hosts mayor a 0

## 6. LIMITACIONES

- Funciona solo con redes IPv4
- Prefijos válidos entre 1 y 30
- Calcula subredes de manera secuencial

## 7. EJEMPLOS DE SALIDA

```
Resultados de la Calculadora de Subneteo VLSM:
============================================================
Subred: Subred 1
  Dirección de red: 192.168.1.0
  Máscara de red: 255.255.255.192
  Prefijo: /26
  Rango de hosts: 192.168.1.1 - 192.168.1.62
  Broadcast: 192.168.1.63
  Hosts necesarios: 50
  Hosts disponibles: 62
------------------------------------------------------------
```

## 8. DESARROLLADOR

Nombre: Dan Ramos Reynaldo

## 9. LICENCIA

Distribuido bajo Licencia MIT.

¡GRACIAS POR USAR LA CALCULADORA VLSM! 🌐🖥️
