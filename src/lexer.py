import ply.ply.lex as lex   # lexer -> tokens
import re
import argparse

# Obtener path de texto por terminal
argParser = argparse.ArgumentParser(description='Procesa strings a tokens de RSS.')
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
    'cerrarheight',
    'width',
    'cerrarwidth',
    'UTF8',
    'slash',
    
    # Simbolos URL
    # 'http',
    # 'https',
    # 'ftp',
    # 'ftps',
    # 'protocolo'

    # etiquetas
    'version',
    'category',
    'cerrarcategory',
    'description',
    'cerrardescription',
    'link',
    'cerrarlink',
    'titulo',
    'cerrartitulo',
    'url',
    'cerrarurl',
    'channel',
    'cerrarchannel',
    'rss',
    'cerrarrss',
    'xml',
    # 'cerrarxml',
    'image',
    'cerrarimage',
    'copyright',
    'cerrarcopyright',
    'item',
    'cerraritem',
    #
    # Texto
    'contenido_texto',
    'digito',
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

# Etiquetas

# def t_version(t): r'version'; return (t)

def t_category(t): r'<category>'; return (t)
def t_cerrarcategory(t): r'<\/category>'; return (t)

def t_description(t): r'<description>'; return (t)
def t_cerrardescription(t): r'<\/description>'; return (t)

def t_link(t): r'<link>'; return (t)
def t_cerrarlink(t): r'<\/link>'; return (t)
 
def t_titulo(t): 
    r'<title>'
    return t; 
def t_cerrartitulo(t): r'<\/title>'; return(t)

def t_url(t): r'<url>'; return(t)
def t_cerrarurl(t): r'<\/url\>'; return(t)

def t_channel(t): r'<channel>'; return(t)
def t_cerrarchannel(t): r'<\/channel>'; return(t)

def t_item(t): r'<item>'; return(t)
def t_cerraritem(t): r'<\/item>'; return(t)

def t_rss(t): r'<rss\s*version="2.0"\s*>'; return(t)
def t_cerrarrss(t): r'<\/rss>'; return(t)

# Protocolos
def t_protocolo(t): r'(https|http|ftps|ftp):\/\/'; return (t)

# Etiquetas opcionales

def t_height(t): r'<height>'; return(t)
def t_cerrarheight(t): r'<\/height>'; return(t)

def t_width(t): r'<width>'; return(t)
def t_cerrarwidth(t): r'<\/width>'; return(t)

def t_image(t): r'<image>'; return(t)
def t_cerrarimage(t): r'<\/image>'; return(t)

def t_copyright(t): r'<copyright>'; return(t)
def t_cerrarcopyright(t): r'<\/copyright>'; return(t)


def t_xml(t): r'<\?xml\s+version="1\.0"\s+encoding="UTF-8"\s*\?>'; return(t)
# def t_cerrarxml(t): r'\?\>'; return(t)

# Resto

t_digito = r'\d+'
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

t_contenido_texto = r'(.)+(?=<\/\w+>)' # ; return (t)

lexer = lex.lex(reflags=re.IGNORECASE) # Bandera para que ignore mayuscula/minuscula

# Solo si se ejecuta desde lexer.py hacer...
if __name__ == "__main__":
    print('Lexer de RSS | Grupo 1. SSL 2022.')
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