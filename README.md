# SSL 2022 - Interprete de lenguaje RSS

Universidad Tecnológica Nacional - Regional Resistencia

Cátedra: Sintaxis y Semántica de los Lenguajes.

Hecho por:
- Arduña, Agustín.
- Schefer, Mauricio.
- Segnana, Juan.
- Velazco Gez Schegtel, Juan Ignacio.

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

## Graph

```mermaid
graph TD;
    A-->B;
    A-->C;
    B-->D;
    C-->D;
```