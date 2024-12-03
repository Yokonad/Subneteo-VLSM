# 🌐 Calculadora VLSM

Herramienta en Python para dividir una red principal en subredes optimizando el uso de direcciones IP mediante **VLSM**.

---

## 🚀 Características

- Divide redes en subredes personalizadas.
- Calcula rangos de hosts, máscaras y direcciones de broadcast.
  
---

## 🛠️ Requisitos

- **Python 3.6+**

---

## 📦 Instalación

1. Clona el repositorio:
   ````bash
   git clone https://github.com/Yokonad/calculadora-vlsm.git
Entra en el directorio:

bash
Copiar código
cd calculadora-vlsm
Ejecuta el programa:

bash

python vlsm_calculator.py
🧮 Ejemplo de Uso
Ingresa la red principal (ejemplo: 192.168.1.0/24).
Define el número de subredes y sus prefijos (ejemplo: /26, /27).
🖥️ Ejemplo de Salida
Resultados de la Calculadora de Subneteo VLSM:
============================================================
Subred: Subred 1
  Dirección de red: 192.168.1.0
  Máscara de red: 255.255.255.192
  Prefijo: /26
  Hosts disponibles: 62
------------------------------------------------------------
Subred: Subred 2
  Dirección de red: 192.168.1.64
  Máscara de red: 255.255.255.224
  Prefijo: /27
  Hosts disponibles: 30
------------------------------------------------------------
