# SSL 2022 - Interprete de lenguaje RSS

Universidad Tecnológica Nacional - Regional Resistencia

Cátedra: Sintaxis y Semántica de los Lenguajes.

Hecho por:
- Arduña, Agustín.
- Schefer, Mauricio.
- Segnana, Juan.
- Velazco, Juan.

## Lexer

Para correrlo con python (version 3):

```bash
python3 src/lexer.py -h
```

Para correrlo con ejecutable:

```bash
python3 src/lexer.py -f "src/ejemplos/planificacion2022.rss"
```

## Generar ejecutables

! Ir a carpeta `src/`

1. Instalar python


### Linux / Mac

```bash
pyinstaller --onefile lexer.py

```

### Windows

2. Instalar pip.

```bash
python -m PyInstaller --onefile lexer.py
```


## TODO
- [X] Terminar token de tipo `contenido_texto`. Hay que buscar que matchee todo menos las etiquetas `(<\w+> y <\/\w+>)`.
- [X] Ver `cerrar xml con `?>`.

- [X] Probar con archivos .txt
- [X] Probar que exporte archivo .txt cuando se analiza llamando desde terminal (argumento -f)

- [X] Cambiar gramatica para contenido texto y hacerla recursiva.
