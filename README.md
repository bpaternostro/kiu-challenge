# kiw-challenge (Español & Ingles)

# Descripción del Proyecto

- La solución fue desarrollada con Python 3.10 (debería funcionar sin problemas con otras versiones 3.*).
- Se utilizaron las librerías core de Python para el desarrollo.

## Desarrollo y Supuestos:

- Aunque no es un framework (para cumplir con las instrucciones), evité utilizar librerías como "pandas" para la solución del challenge.
- No se agregó un módulo de registro porque se intentó mantener el código lo más simple posible.
- Para configurar la solución, utilizamos el archivo `.env`, donde definimos:
    - `INPUT_FILE`:
        - Denominación del archivo de entrada.
        - Se incorporó un ejemplo de `input_file` al proyecto. Este archivo cuenta con registros para el 2024-01-18 y 2024-01-17.
        - El proceso solo admite archivos con extensión ".txt".
    - `OUTPUT_FILE`:
        - Denominación del archivo de salida.
    - `RATE`:
        - Por cada paquete transportado.
    - `PROCESSING_DATE`:
        - Fecha que se utiliza para procesar el total. Esta fecha en el `input_file` se guarda como timestamp.
- El archivo de salida se genera en la raíz del proyecto e incluye:
    - Detalle de las órdenes procesadas con su respectivo subtotal. Excluye aquellas que no cumplen con el filtro de `PROCESSING_DATE`.
    - Total para la fecha especificada.
    - Se subió un ejemplo de resultado con la denominación: `result_sample.txt`.

## Pruebas Unitarias:

- Todas las pruebas se encuentran dentro de la ruta `src/test/test_package_controller.py`.
- Para las pruebas unitarias, se utilizó la librería "pytest". En la raíz del proyecto, hay un archivo Makefile para ejecutar todo el coverage: `make coverage`.

## Manejo de Dependencias:

- Para el manejo de dependencias (son solo para desarrollo), utilicé pipenv en mi local, pero también dejé preparado un archivo `requirements.txt`.

## Aclaraciones:

- Se subió el archivo `.env` a Git para que la persona encargada de revisar el desafío tenga una referencia de cómo configurar la solución.


# English

# Project Description

- The solution was developed with Python 3.10 (it should work without issues with other 3.* versions).
- Core Python libraries were used for development.

## Development and Assumptions:

- Although it's not a framework (to comply with the instructions), I avoided using libraries like "pandas" for the challenge solution.
- A logging module was not added because an effort was made to keep the code as simple as possible.
- To configure the solution, we use the `.env` file, where we define:
    - `INPUT_FILE`:
        - Denomination of the input file.
        - An example `input_file` is included in the project. This file contains records for 2024-01-18 and 2024-01-17.
        - The process only supports files with the ".txt" extension.
    - `OUTPUT_FILE`:
        - Denomination of the output file.
    - `RATE`:
        - For each transported package.
    - `PROCESSING_DATE`:
        - Date used to process the total. This date is stored as a timestamp in the `input_file`.
- The output file is generated in the project's root and includes:
    - Details of processed orders with their respective subtotal. Excludes those that do not meet the `PROCESSING_DATE` filter.
    - Total for the specified date.
    - An example result is uploaded with the designation: `result_sample.txt`.

## Unit Testing:

- All tests are located within the path `src/test/test_package_controller.py`.
- For unit testing, the "pytest" library was used. In the project's root, there's a Makefile to run full coverage: `make coverage`.

## Dependency Management:

- For dependency management (for development only), I used pipenv locally, but I also prepared a `requirements.txt` file.

## Clarifications:

- The `.env` file was uploaded to Git so that the person in charge of reviewing the challenge has a reference on how to configure the solution.
