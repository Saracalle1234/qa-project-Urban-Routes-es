Urban Routes - Pruebas Automatizadas

Que es este proyecto?
Este proyecto automatiza pruebas en la app web Urban Routes, que sirve para pedir transporte. Las pruebas se hicieron con Selenium WebDriver y Pytest

Que pruebas hace?
El script automatiza los siguientes pasos:
-Selecciona direccion de origen y destino
-Elige la tarifa Comfort
-Ingresa numero de telefono
-Introduce el codigo SMS
-Agrega tarjeta de credito
-Escribe un mensaje para el conductor
-Pide mata y panuelo
-Ordena dos helados
-Confirma el viaje
-Espera que aparezca la informacion del conducto

Estructura del proyecto
qa-project-urban-routes-es/
-data.py # Datos como URL, telefono, tarjeta
-urban_routes_page.py # Funciones y selectorees de la app
-test_urban_routes.py # Pruegas automatizadas con pytest
-retrieve_code
-README.md # Descripcion del proyecto

Requisitos
-Python 3.9 o superior
-Google Chrome
-ChromeDriver

Como ejecutar las pruebas
-En archivo test_urban_router.py, current file, dar click en RUN
-PyChar ejecutara todas las pruebas y mostrara los resulatados en la consola inferior
Importante: Actualizar la URL. en data.py con el que da Tripleten para que pueda funcionar la prueba

Herramientas usadas
-Pycharm
-Selenim WebDriver
-Pytest