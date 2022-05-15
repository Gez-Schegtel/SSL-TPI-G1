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

```

## TODO
[] - Terminar token de tipo `contenido_texto`. Hay que buscar que matchee todo menos las etiquetas `(<\w+> y <\/\w+>)`.
[] - Probar con archivos .txt
[] - Probar que exporte archivo .txt cuando se analiza llamando desde terminal (argumento -f).