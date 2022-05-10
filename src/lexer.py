import ply.ply.lex as lex   # lexer -> tokens
import re
import argparse

#Obtener path de texto por terminal
argParser = argparse.ArgumentParser(description='Procesa strings a tokens de pseudocodigo.')
argParser.add_argument('-f', '-pathFile', nargs='?',type=str, help='especificar ruta de archivo de texto de entrada a analizar.')
argsParser = argParser.parse_args()
pathFile = argsParser.f

contadorErrores = 0
arregloHtml = []

# /******
# <
# >
# /
# http
# https
# ftp
# ftps
# height
# width
# category
# image 
# copyright
# description
# link
# title
# url
# channel
# rss
# =
# “
# .
# ?
# xml
# version
# :
# encoding
# UTF-8
# *****/

# Terminales
tokens = [
    # operadores
    'menorque',
    'mayorque',
    'igualque',
    #
    'comilla',
    'barra',
    'protocolo',
    'punto',
    'prologo', # <?xml
    # 'dospuntos', # se ocupa en protocolo
    # 
    'imagen_alto',
    'imagen_ancho',
    # etiquetas
    'version',
    'encoding',
    'valor_encoding',
    'categoria',
    'descripcion',
    'link',
    'titulo',
    'url',
    'canal',
    'rss',
]

# ply detecta variables que empiecen con 't_'
# Terminos: 
# w = letras o numeros
# s = todo lo que sea espacios.
# S = contrario a 's'.
# d = digitos.
# * = 0 o más.
# + = 1 o más.

# def t_COMENTARIO_ENCABEZADO(t): 
#     r'\/\*\*[\s\S]*?\*\/';
#     if t.value.__contains__('\n'):
#         t.lexer.lineno += t.value.count('\n')
#         t.value= t.value.replace('\n', ' ')
#     if t.value.__contains__('\t'):
#         t.value= t.value.replace('\t', ' ')
#     cambio= t.value.replace('/**', '')
#     cambio= cambio.replace('*/','')
#     arregloHtml.append(['encabezado', cambio])
#     return t 

# def t_ES(t): r'\b(?:_es)\b'; return t
def t_comilla(t): r'\b(?:acci[oó]n)\b'; return t 

    # 'prologo', # <?xml
    # # 'dospuntos', # se ocupa en protocolo
    # # 
    # 'imagen_alto',
    # 'imagen_ancho',


t_igualque = r'\='
t_menorque = r'\<'
t_mayorque = r'\>'
# t_dospuntos = r'\:'
t_comilla = r''


def t_version(t): r'\bversion\b'; return t

def t_encoding(t): r'\bencoding\b'; return t

def t_valor_encoding(t): r'\bvalor_encoding\b'; return t

def 

    # 'version',
    # 'encoding',
    # 'valor_encoding',
    # 'categoria',
    # 'descripcion',
    # 'link',
    # 'titulo',
    # 'url',
    # 'canal',
    # 'rss',

# ply ignorará espacios, saltos de lineas y tabs.
t_ignore = ' \t;'

def t_IDENTIFICADOR(t):
    r'[_a-zA-Zñ][_a-zA-Zñ0-9]*'
    t.type = 'IDENTIFICADOR'
    if not(t.value[0].__contains__('_')) and not(t.value[-1].__contains__('_')) and not(t.value.__contains__('__')) and not(t.value.__contains__('"')):
        return t
    else: 
        print(f'Identificador ilegal! : \'{t.value}\'.')
        global contadorErrores
        contadorErrores += 1

def t_error(t):
    global contadorErrores
    print(f'Caracter ilegal! : \'{t.value[0]}\'.')
    print(f'En linea: {t.lineno}. Posición: {t.lexpos}')
    contadorErrores += 1
    t.lexer.skip(1)

def t_CADENA(t):
    r'\\?"(?:[^"\\]|\\.)*"?'
    if not(t.value[-1] == '"') or (t.value[0] == '\\') or (t.value[-2] == '\\'):
        print(f'Cadena ilegal! : \'{t.value}\'.')
        global contadorErrores
        contadorErrores += 1
    else:
        t.value= t.value.replace('"', '')
        if t.value.__contains__('\\'):
            t.value = t.value.replace('\\', '"')
        if t.value.__contains__('\n'):
            t.value= t.value.replace('\n', ' ')
        if t.value.__contains__('\t'):
            t.value= t.value.replace('\t', ' ')
        return t

def t_NUMERICO(t): # acepta . o , como decimal.
    r'([\d]+(,|\.)[\d]+|[\d]+)'
    if t.value.__contains__(','):
        t.value= t.value.replace(",", ".")
        t.value = float(t.value)
    elif t.value.__contains__('.'):
        t.value = float(t.value)
    else:
        t.value = int(t.value)
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

lexer = lex.lex(reflags=re.IGNORECASE) # Bandera para que ignore mayuscula/minuscula

# Solo si se ejecuta desde lexer.py hacer...
if __name__ == "__main__":
    print('Lexer Pseudocodigo | Grupo 1. SSL 2022.')
    def analizarTokens(modoEjecucion):
        global contadorErrores
        exportArray = []
        while True:
                tok = lexer.token()
                if not tok:
                    if (modoEjecucion == 'archivo'):
                        exportarTokens(exportArray)
                    break
                if (modoEjecucion == 'archivo'):
                    exportArray.append([tok.type,tok.value]);
                else: print(f'Tipo: {tok.type} | Valor: {tok.value}')

    # # Exportar a un txt 
    def exportarTokens(arrAnalizar):
        global contadorErrores
        with open('tokens-analizados.txt', 'w', encoding='UTF8') as f:
            f.write('TOKEN | VALOR\n')
            f.write('-------------\n')
            contador = 0
            for line in arrAnalizar:
                contador += 1
                f.write(f'{contador}- {line[0]}: {line[1]}')
                f.write('\n')
            f.write('-------------\n')
            f.write(f'Total de tokens válidos analizados: {contador}.\n')
            if (contadorErrores > 0):
                f.write(f'Total de tokens NO válidos: {contadorErrores}.')
        f.close()
        if (contadorErrores > 0):
            print('(⨉) El lexer NO acepta este archivo.')
        else:
            print('(⩗) El lexer ACEPTA este archivo.')
        print('(!) Se exportó un .txt con los tokens analizados.')

    if not pathFile:
        # Ejecución "normal"
        print('Pasa salir pulse: [ctrl] + [C] | O escriba _salir')
        while True:
            s = input('>> ')
            if s == '_salir': break
            lexer.input(s)
            analizarTokens('normal')
    else:
        # Ejecución "analisis de archivo de texto"
        try:
            file = open(pathFile,"r",encoding='utf8')
            strings = file.read()
            file.close()
            lexer.input(strings)
            analizarTokens('archivo')
        except IOError:
            print('Ocurrió un error leyendo archivo:', pathFile)