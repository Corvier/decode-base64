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
import os
from base64 import decodebytes
from time import sleep
from colorama import Fore
from dotenv import load_dotenv

"""
    Obtengo el modulo que fue invocado
"""

module = GetParams("module")

try:
    if module == "decoder":
        base_path = ''
        data = GetParams("id_input_base64") # data
        variables = GetParams("id_output_base64") # vars
        load = GetParams("id_get_pms_base64")
        base_path = GetVar("base_pathP")
        print(load)
        if load != False:
            if base_path != '':
                cred_path = f"{base_path}credentials/cred.env"
                # print(cred_path)
                try:
                    load_dotenv(cred_path)
                    user = os.environ.get('user')
                    pwd = os.environ.get('password')
                    org = os.environ.get("organization")

                    if user != None and pwd != None:
                        SetVar("decoded_user", decodebytes(user.encode('utf-8')).decode())
                        SetVar("decoded_password", decodebytes(pwd.encode('utf-8')).decode())

                        if org is not None:
                            SetVar("decoded_organization", decodebytes(org.encode('utf-8')).decode())
                    
                    print(Fore.CYAN + f'\nObteniendo credenciales...')
                    sleep(1)
                    print(Fore.GREEN + f'>  Decodificacion existosa\n' + Fore.WHITE)

                except Exception as e:
                    print(Fore.CYAN + f'\n> Decodificacion incorrecta\n')
                    raise print(Fore.MAGENTA + f'Error: {e}' + Fore.WHITE)
        else:
            try:
                data = eval(data)
                variables =  variables.split(",")

                for i, var in enumerate(variables):
                    SetVar(var, decodebytes(data[i].encode('utf-8')).decode())
                
                print(Fore.GREEN + f'\n> Decodificacion exitosa\n' + Fore.WHITE)
            
            except Exception as e:
                print(Fore.CYAN + f'\n> Decodificacion incorrecta\n')
                raise print(Fore.MAGENTA + f'Error: {e}' + Fore.WHITE)

except Exception as e:
    raise print(Fore.MAGENTA + f'Error: {e}')