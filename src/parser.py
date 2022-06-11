import ply.ply.yacc as yacc # parser 
from lexer import tokens
import argparse

#Obtener path de texto por terminal
argParser = argparse.ArgumentParser(description='Procesa tokens de RSS.')
argParser.add_argument('-f', '-pathFile', nargs='?',type=str, help='especificar ruta de archivo de texto de entrada a analizar.')
argsParser = argParser.parse_args()
pathFile = argsParser.f

exportarTxt = list()
contadorErrores = 0

# Mayusculas = No Terminales; Minusculas = Terminales
def p_SIGMA (p):
    ''' SIGMA : xml RSS '''
    print("Ejecución completa!")
    exportarTxt.append(['Prod. Sigma -->', p.slice])

def p_RSS (p):
    '''RSS : rss CHANNEL cerrarrss
    '''
    exportarTxt.append(['Prod. RSS -->', p.slice])

def p_CHANNEL(p): 
    '''CHANNEL : channel ET_OBL ITEM_REC cerrarchannel'''
    exportarTxt.append(['Prod. CHANNEL -->', p.slice])
    
def p_ET_OBL(p): 
    '''ET_OBL : ET_TITLE ET_LINK ET_DESC ET_CATEGORY ET_COPYRIGHT CONT_IMG
    '''
    exportarTxt.append(['Prod. ET_OBL -->', p.slice])

def p_LAMBDA(p):
    'LAMBDA :'
    pass

# Juani
def p_ET_TITLE(p): 
    '''ET_TITLE : titulo CONT_TEXTO cerrartitulo
    '''
    exportarTxt.append(['Prod. ET_TITLE -->', p.slice])


def p_ET_LINK(p): 
    '''ET_LINK : link CONT_LINK cerrarlink
    '''
    exportarTxt.append(['Prod. ET_LINK -->', p.slice])

def p_ET_URL(p): 
    '''ET_URL : url CONT_LINK cerrarurl
    '''
    exportarTxt.append(['Prod. ET_URL -->', p.slice])

def p_ET_DESC(p): 
    '''ET_DESC : description CONT_TEXTO cerrardescription
    '''
    exportarTxt.append(['Prod. ET_DESC -->', p.slice])

def p_ET_CATEGORY(p): 
    '''ET_CATEGORY : category CONT_TEXTO cerrarcategory
                    | LAMBDA
    '''
    exportarTxt.append(['Prod. ET_CATEGORY -->', p.slice])

def p_ET_COPYRIGHT(p): 
    '''ET_COPYRIGHT : copyright CONT_TEXTO cerrarcopyright
                    | LAMBDA
    '''
    exportarTxt.append(['Prod. ET_COPYRIGHT -->', p.slice])

def p_CONT_TEXTO(p): 
    '''CONT_TEXTO : contenido_texto CONT_TEXTO
                | contenido_texto
    '''
    exportarTxt.append(['Prod. CONT_TEXTO -->', p.slice])

def p_CONT_IMG(p): 
    '''CONT_IMG : ET_IMG_OBL ET_IMG_OP 
                | ET_IMG_OBL 
                | LAMBDA
    '''
    exportarTxt.append(['Prod. CONT_IMG -->', p.slice])
# Agus
def p_ET_IMG_OBL (p): 
    '''ET_IMG_OBL  : ET_TITLE ET_LINK ET_URL
                   | ET_TITLE ET_URL ET_LINK
                   | ET_URL ET_TITLE ET_LINK
                   | ET_URL ET_LINK ET_TITLE
                   | ET_LINK ET_TITLE ET_URL
                   | ET_LINK ET_URL ET_TITLE
    '''
    exportarTxt.append(['Prod. ET_IMG_OBL  -->', p.slice])

def p_ET_IMG_OP (p): 
    '''ET_IMG_OP  : ET_HEIGHT ET_IMG_OP
                  | ET_WIDTH ET_IMG_OP
                  | ET_HEIGHT 
                  | ET_WIDTH
    '''
    exportarTxt.append(['Prod. ET_IMG_OP  -->', p.slice])

def p_ET_HEIGHT (p): 
    '''ET_HEIGHT : height digito cerrarheight
    '''
    exportarTxt.append(['Prod. ET_HEIGHT -->', p.slice])    

def p_ET_WIDTH (p):
    '''ET_WIDTH : width digito cerrarwidth
    '''
    exportarTxt.append(['Prod. ET_WIDTH -->', p.slice]) 

# Juan S
def p_CONT_LINK(p): 
    '''CONT_LINK : protocolo DOMINIO_GRAL FINAL_URL
                 | protocolo DOMINIO_GRAL
    '''
    exportarTxt.append(['Prod. CONT_LINK -->', p.slice])


def p_FINAL_URL(p): 
    '''FINAL_URL : slash RUTA numeral LOCALIZADOR
                 | slash RUTA
    '''
    exportarTxt.append(['Prod. CONT_LINK -->', p.slice])

def p_DOMINIO_GRAL(p): 
    '''DOMINIO_GRAL : DOMINIO dospuntos PUERTO
                    | DOMINIO
    '''
    exportarTxt.append(['Prod. DOMINIO_GRAL -->', p.slice])

def p_LOCALIZADOR(p): 
    '''LOCALIZADOR : contenido_texto
    '''
    exportarTxt.append(['Prod. LOCALIZADOR -->', p.slice])

def p_DOMINIO(p): 
    '''DOMINIO : contenido_texto
    '''
    exportarTxt.append(['Prod. DOMINIO -->', p.slice])

def p_RUTA(p): 
    '''RUTA : contenido_texto
    '''
    exportarTxt.append(['Prod. RUTA -->', p.slice])

def p_PUERTO(p): 
    '''PUERTO : digito
    '''
    exportarTxt.append(['Prod.  -->', p.slice])

# Mauri
def p_ITEM_REC(p): 
    '''ITEM_REC : ET_OBL_ITEM ITEM_REC
                | ET_OBL_ITEM
    '''
    exportarTxt.append(['Prod. ITEM_REC -->', p.slice])

# def p_ET_ITEM(p): 
#     '''ET_ITEM : ET_OBL_ITEM
#     '''
#     exportarTxt.append(['Prod. ET_ ITEM -->', p.slice])

def p_ET_OBL_ITEM(p): 
    '''ET_OBL_ITEM : ET_TITLE ET_DESC ET_LINK ET_CATEGORY 
                | ET_TITLE ET_DESC ET_CATEGORY ET_LINK
                | ET_TITLE  ET_CATEGORY  ET_DESC ET_LINK
                | ET_TITLE  ET_CATEGORY  ET_LINK ET_DESC
                | ET_TITLE ET_LINK ET_CATEGORY  ET_DESC
                | ET_TITLE ET_LINK  ET_DESC ET_CATEGORY
                | ET_DESC  ET_TITLE ET_LINK ET_CATEGORY 
                | ET_DESC  ET_TITLE ET_CATEGORY ET_LINK 
                | ET_DESC ET_CATEGORY ET_TITLE ET_LINK 
                | ET_DESC ET_CATEGORY ET_LINK ET_TITLE 
                | ET_DESC ET_LINK ET_CATEGORY ET_TITLE
                | ET_DESC ET_LINK  ET_TITLE ET_CATEGORY
                | ET_CATEGORY ET_DESC ET_TITLE ET_LINK 
                | ET_CATEGORY ET_TITLE ET_DESC  ET_LINK 
                | ET_CATEGORY ET_DESC  ET_LINK ET_TITLE 
                | ET_CATEGORY ET_LINK ET_TITLE ET_DESC  
                | ET_CATEGORY ET_LINK ET_DESC ET_TITLE 
                | ET_LINK ET_CATEGORY ET_TITLE ET_DESC 
                | ET_LINK ET_CATEGORY ET_DESC ET_TITLE 
                | ET_LINK ET_TITLE ET_DESC ET_CATEGORY 
                | ET_LINK ET_TITLE ET_CATEGORY ET_DESC 
                | ET_LINK ET_DESC ET_CATEGORY ET_TITLE 
                | ET_LINK ET_DESC ET_TITLE ET_CATEGORY
    '''
    exportarTxt.append(['Prod. ET_OBL_ITEM -->', p.slice])

def p_error (p):
    # p regresa como un objeto del Lexer.
    # p.__dict__ -> ver propiedades del objeto.
    global contadorErrores
    if (p):
        print(f'Error parser --> Tipo: {p.type} | Valor: {p.value}')
        print('Error sintáctico en LINEA:', p.lineno)
        exportarTxt.append(['Error parser -->', p])
    else:
        # print("error: falta fin_accion") TODO: BORRAR
        exportarTxt.append(['Error parser --> ??'])
    contadorErrores += 1

parser = yacc.yacc() # Ignorar warnings.
# errorlog=yacc.NullLogger()

# def exportarHtml (arregloHtml):

#     nombre = pathFile
#     nombre = nombre.replace('.rss', '')
    
#     nombreRecortado = ''
#     if nombre.__contains__('/'):
#         nombreRecortado = nombre.split('/')[-1]
#     elif nombre.__contains__('\\'):
#         nombreRecortado = nombre.split('\\')[-1]
#     else: nombreRecortado = nombre;

#     base = [
#         f'''<!DOCTYPE html>\n<html>\n<head>\n\t<meta charset="utf-8">\n\t<title>{nombreRecortado}</title>\n</head>\n<body>'''
#     ]
#
#     for line in arregloHtml:
#         line[1] = line[1].strip()
#         if line[0] == 'encabezado':
#             base.append('\n\t<h2>'+line[1]+'</h2>')
#         if line[0] == 'linea':
#             base.append('\n\t<p>'+line[1]+'</p>')
#         if line[0] == 'bloque':
#             base.append('\n\t<h4>'+line[1]+'</h4>')

#     base.append('\n</body>\n</html>')
#     with open(f'{nombre}.html', 'w', encoding='UTF8') as f:
#         for line in base:
#             f.write(line)
#     f.close()
# # fin de función exportar

print('Parser RSS | Grupo 1. SSL 2022.')
if not pathFile:
    # Ejecución "normal"
    print('Para interrumpir la ejecucion: [ctrl] + [C] | Para volver al menu principal: _salir')
    while True:
        s = input('>> ')
        if s == '_salir': break
        result = parser.parse(s)
        print(result)
else:
    # Ejecución "analisis de archivo de texto"
    try:
        file = open(pathFile,"r",encoding='utf8')
        strings = file.read()
        file.close()
        result = parser.parse(strings)
        from datetime import datetime

        with open(f'producciones-analizadas-{datetime.now().isoformat()}.txt', 'w', encoding='UTF8') as f:
            f.write('Producciones analizadas por el parser\n-----------------\n')
            contador = 0
            for line in exportarTxt:
                contador += 1
                f.write(f'{contador}) {line[0]} | {line[1]}\n')
                f.write('-------------\n')
            f.write('-------------\n')
            f.write(f'Total de tokens analizados: {contador}.\n')
        f.close()
        if contadorErrores > 0:
            print('(⨉) Ocurrió un error sintáctico.')
        else:
            print('test')
            # exportarHtml(arregloHtml)
            # print('(⩗) Sintácticamente correcto. Se exportó un .html con los comentarios.')
        print('(!) Se exportó un .txt con las producciones analizadas.')
    except IOError:
        print('Ocurrió un error leyendo archivo:', pathFile)
        