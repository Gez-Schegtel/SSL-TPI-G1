import re

def pedirRuta():
  # Pedir ruta del archivo por input
  pathFile = input('Ingrese la ruta del archivo a analizar: ')
  # Remover comillas
  pathClean = re.sub(
      r'\'|"',
      '',
      pathFile
  )
  return pathClean.strip()

# todo
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