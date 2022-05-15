import ply.ply.lex as lex   # lexer -> tokens
import re
import argparse

# Obtener path de texto por terminal
argParser = argparse.ArgumentParser(description='Procesa strings a tokens de pseudocodigo.')
argParser.add_argument('-f', '-pathFile', nargs='?',type=str, help='especificar ruta de archivo de texto de entrada a analizar.')
argsParser = argParser.parse_args()
pathFile = argsParser.f

contadorErrores = 0

# Terminales
tokens = [
    # operadores
    'menorque',
    'mayorque',
    'igualque',
    
    # simbolos
    'comilla',
    'barra',
    'protocolo',
    'punto',
    'dospuntos',
    'question',
    'height',
    'width',
    'UTF8',
    'slash',
    
    # Simbolos URL
    'http',
    'https',
    'ftp',
    'ftps',

    # etiquetas
    'version',
    'encoding',
    'valor_encoding',
    'category',
    'description',
    'link',
    'title',
    'cerrartitle',
    'url',
    'channel',
    'rss',
    'xml',
    'image',
    'copyright',
    
    # Texto
    'contenido_texto'
]

# PLY detecta variables que empiecen con 't_'
# Terminos: 
# w = letras o numeros
# s = todo lo que sea espacios.
# S = contrario a 's'.
# d = digitos.
# * = 0 o más.
# + = 1 o más.
    
# Definición de símbolos atómicos #

def t_version(t): r'\bversion\b'; return (t)

def t_category(t): r'\bcategory\b'; return (t)

def t_description(t): r'\bdescription\b'; return (t)

def t_link(t): r'\blink\b'; return (t)
 
def t_title(t): r'\btitle\b'; return(t)
def t_cerrartitle(t): r'<\/title>'; return(t)

def t_url(t): r'\burl\b'; return(t)

def t_channel(t): r'\bchannel\b'; return(t)

def t_rss(t): r'\brss\b'; return(t)

def t_http(t): r'\bhttp\b'; return(t)

def t_https(t): r'\bhttps\b'; return(t)

def t_ftp(t): r'\bftp\b'; return(t)

def t_ftps(t): r'\bftps\b'; return(t)

def t_height(t): r'\bheight\b'; return(t)

def t_width(t): r'\bwidth\b'; return(t)

def t_image(t): r'\bimage\b'; return(t)

def t_copyright(t): r'\bcopyright\b'; return(t)

def t_xml(t): r'\bxml\b'; return(t)

def t_encoding(t): r'\bencoding\b'; return(t)

def t_UTF8(t): r'\butf-8\b'; return(t) # Está en minúscula p/ que funcione con IGNORECASE #

t_igualque = r'\='
t_menorque = r'\<'
t_mayorque = r'\>'
t_dospuntos = r'\:'
t_comilla = r'\"|\”' 
t_question = r'\?'
t_slash = r'\/'
t_punto = r'\.'

# PLY ignorará espacios, saltos de lineas y tabs.
t_ignore = ' \t'

def t_error(t):
    global contadorErrores
    print(f'Caracter ilegal! : \'{t.value[0]}\'.')
    print(f'En linea: {t.lineno}. Posición: {t.lexpos}')
    contadorErrores += 1
    t.lexer.skip(1)

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

t_contenido_texto = r'(\w|\d)+' # ; return (t)

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

    # Exportar TOKENS a un .txt 
    def exportarTokens(arrAnalizar):
        global contadorErrores
        from datetime import datetime 
        fileNameExport = f'tokens-analizados-{datetime.now().isoformat()}.txt'
        with open(fileNameExport, 'w', encoding='UTF8') as f:
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
        print('Para salir pulse: [ctrl] + [C] | O escriba _salir')
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