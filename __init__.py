# coding: utf-8
"""
Base para desarrollo de modulos externos.
Para obtener el modulo/Funcion que se esta llamando:
     GetParams("module")

Para obtener las variables enviadas desde formulario/comando Rocketbot:
    var = GetParams(variable)
    Las "variable" se define en forms del archivo package.json

Para modificar la variable de Rocketbot:
    SetVar(Variable_Rocketbot, "dato")

Para obtener una variable de Rocketbot:
    var = GetVar(Variable_Rocketbot)

Para obtener la Opcion seleccionada:
    opcion = GetParams("option")


Para instalar librerias se debe ingresar por terminal a la carpeta "libs"
    
    pip install <package> -t .

"""
from base64 import decodebytes
from colorama import Fore

"""
    Obtengo el modulo que fue invocado
"""

module = GetParams("module")

try:
    if module == "decoder":
        data = GetParams("id_input_base64") # data
        variables = GetParams("id_output_base64") # vars

        try:
            data = eval(data)
            variables =  variables.split(",")

            for i, var in enumerate(variables):
                SetVar(var, decodebytes(data[i].encode('utf-8')).decode())
            
            print(Fore.GREEN + f'\n> Decodificacion exitosa\n')
        
        except Exception as e:
            print(Fore.CYAN + f'\n> Decodificacion incorrecta\n')
            raise print(Fore.MAGENTA + f'Error: {e}')

except Exception as e:
    raise print(Fore.MAGENTA + f'Error: {e}')