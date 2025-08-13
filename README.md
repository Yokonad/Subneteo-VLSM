# CALCULADORA DE REDES

## 1. DESCRIPCIÓN DEL PROYECTO

### 1.1 Objetivo
Herramienta para el cálculo de subredes VLSM y enlaces punto a punto entre routers, permitiendo una gestión eficiente de direcciones IP.

### 1.2 Características Principales
- Cálculo de subredes VLSM basado en hosts requeridos
- Cálculo de enlaces punto a punto entre routers
- Validación de direcciones IP y rangos
- Cálculo automático de máscaras y wildcards
- Presentación detallada de resultados

## 2. REQUISITOS TÉCNICOS

### 2.1 Entorno
- Python 3.7 o superior
- Módulos requeridos: 
  * ipaddress
  * math

### 2.2 Instalación
```
pip install ipaddress
```

## 3. FUNCIONALIDADES

### 3.1 Calculadora VLSM
- Cálculo de subredes basado en requerimientos de hosts
- Asignación óptima de direcciones
- Información detallada de cada subred
- Validación de rangos y direcciones

### 3.2 Calculadora de Enlaces
- Cálculo de subredes /30 para enlaces punto a punto
- Asignación secuencial de direcciones
- Información detallada de cada enlace
- Validación de rangos disponibles

## 4. ESTRUCTURA DEL CÓDIGO

### 4.1 Funciones Principales

#### Validación IP
```python
def validar_ip(ip):
    try:
        ipaddress.IPv4Address(ip)
        return True
    except ValueError:
        return False
```

#### Cálculo de Prefijo VLSM
```python
def calcular_prefijo_desde_hosts(num_hosts):
    return 32 - math.ceil(math.log2(num_hosts + 2))
```

#### Cálculo de Wildcard
```python
def calcular_wildcard(mascara):
    mascara_ip = ipaddress.IPv4Address(mascara)
    wildcard = ipaddress.IPv4Address(int(mascara_ip) ^ 0xFFFFFFFF)
    return str(wildcard)
```

## 5. MODO DE USO

### 5.1 Calculadora VLSM
1. Seleccionar opción 1 en el menú principal
2. Ingresar dirección IP base
3. Especificar prefijo de red principal
4. Indicar cantidad de subredes
5. Definir hosts necesarios por subred

### 5.2 Calculadora de Enlaces
1. Seleccionar opción 2 en el menú principal
2. Ingresar dirección IP base
3. Especificar prefijo de red principal
4. Indicar cantidad de enlaces

## 6. EJEMPLOS

### 6.1 Ejemplo VLSM
```
Ingrese la dirección IP base: 192.168.1.0
Ingrese el prefijo principal de la red: 24
¿Cuántas subredes desea calcular?: 2
Ingrese la cantidad de hosts para la subred 1: 100
Ingrese la cantidad de hosts para la subred 2: 50
```

### 6.2 Ejemplo Enlaces
```
Ingrese la dirección IP base: 10.0.0.0
Ingrese el prefijo principal de la red: 24
¿Cuántos enlaces entre routers necesita?: 3
```

## 7. LIMITACIONES

- Soporte exclusivo para IPv4
- Prefijos válidos: 1-30
- Enlaces punto a punto usando /30
- Procesamiento secuencial de subredes

## 8. DESARROLLADOR

Nombre: Dan Ramos Reynaldo

## 9. LICENCIA

Distribuido bajo Licencia MIT
