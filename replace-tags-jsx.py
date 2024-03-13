import os

extensions = {"jsx"}
my_path = '/media/raul/d1964fe0-512e-4389-b8f7-b1bd04e82961/raul/Storage/Projects/Emilito/my-app/src'

def walk (path = my_path):
    '''
    Recorre cada uno de los archivos del arbol de la carpeta y subcarpetas contenidas en esta
    '''
    for dirpath, dirnames, filenames in os.walk(path):
        # print(f"Ruta actual: {dirpath}")
        for filename in filenames:
            if len(filename) > 3 and filename[-3:] in extensions:
                code = open(dirpath + "/"+filename, 'r+').read()
                code = full_replace(code)
                open(dirpath + "/"+filename, 'w').write(code)
    
    

def replace (code, from_ = "<a ", to = "<Link " ):
    '''
    Reemplaza la cadena `from_` por el string `to` en string `code`.
    '''
    return code.replace(from_,to)


def full_replace(code):
    '''
    modifica esta funcion a conveniencia
    '''
    return a_to_link(code)    

def a_to_link(code):
    code = replace(code=code, from_ = "<a ", to = "<Link ")
    code = replace(code=code, from_= "<a\n", to = "<Link\n")
    code = replace(code=code, from_= "a>", to = "Link>")
    code = replace(code=code, from_= "href", to = "to")
    return code

walk()