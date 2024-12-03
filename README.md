🌐 Calculadora VLSM
Una herramienta en Python que permite dividir una red principal en subredes más pequeñas utilizando VLSM (Variable Length Subnet Masking). Optimiza el uso de direcciones IP, garantizando que las subredes sean contiguas.

🚀 Características
🔹 Divide redes IP en subredes personalizadas.
🔹 Calcula rangos de hosts, máscaras y direcciones de broadcast.
🔹 Optimiza el uso de direcciones IP, eliminando desperdicio.
🔹 Interfaz simple e interactiva.
🛠️ Requisitos
Python 3.6+
📦 Instalación
Clona el repositorio:
bash

Copiar código
git clone https://github.com/Yokonad/calculadora-vlsm.git
Navega al directorio del proyecto:
bash

Copiar código
cd calculadora-vlsm
Ejecuta el programa:
bash

Copiar código
python vlsm_calculator.py
🧮 Ejemplo de Uso
Ingresa la red principal (ejemplo: 192.168.1.0/24).
Define cuántas subredes deseas y sus prefijos (ejemplo: /26, /27).
🖥️ Ejemplo de Salida
plaintext

Copiar código
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
📜 Licencia
Este proyecto está licenciado bajo la MIT License. Consulta el archivo LICENSE para más detalles.

✨ Autor
Creado con ❤️ por Yokonad

¡Contribuciones y sugerencias son bienvenidas! Si encuentras algún problema o tienes una idea para mejorar la calculadora, no dudes en abrir un issue o enviar un pull request.
