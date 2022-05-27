# decode-base64 versión 1.1

***Este módulo sirve para decodificar cadenas de texto codificadas en base64***

## Estado del comando ✅

* [X] Estable

## Comandos 🛠

1. Decodificar base-64 🔨

   ```
   Proposito del comando:
       Este comando fue desarrollado con el propósito de decodificar o convertir las credenciales
       de los PMS, que previamente son extraídas del archivo cred.env, o cualquier otra cadena de
       texto en base64 que se le pase directamente.

   Características del comando:
       La principal característica es que podemos decodificar y asignar múltiples variables o cadenas
       de texto en base64.

   USO:
   1. Entrada de datos en base-64:
       Aquí se debe ingresar la cadena / cadenas codificadas en base-64, si tiene mas de
       una cadena insertarla de la siguiente manera -> ['cadena-codificada-1','cadena-codificada-2'],
       tambien puede proporcinar los datos desde una variable entre llaves o mas variables de la
       siguiente manera -> ['{variable-con-cadena-codificada-1}','{variable-con-cadena-codificada-2}']

   2. Resultados:
       Aquí debe ingresar las variables donde desea retornar el resultado decodificado de la cadena
       para esto debe usar escribir las variables sin llaves y separadas por coma, segun el orden de
       entrada de los datos.
       Ejemplo: ['entrada-codificada-1','entrada-codificada-2'] -> resultado-entrada-codificada-1,resultado-entrada-codificada-2

   3. Obtener credenciales: NEW OPTION 2020-05-27
       Marque esta casilla, para obtener las credenciales desde el archivo .env, solamente asegurese de tener
       las variables decoded_username, decoded_password y opcional decoded_organization en el robot donde este
       usando este comando.

   ```

## Autor ✒️

* Víctor Ruiz
