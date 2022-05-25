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

## TODO
[x] - Terminar token de tipo `contenido_texto`. Hay que buscar que matchee todo menos las etiquetas `(<\w+> y <\/\w+>)`.
[x] - Ver `cerrar xml con `?>`.

[x] - Probar con archivos .txt
[x] - Probar que exporte archivo .txt cuando se analiza llamando desde terminal (argumento -f)

[x] - Cambiar gramatica para contenido texto y hacerla recursiva.