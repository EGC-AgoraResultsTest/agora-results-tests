# agora-results-tests

En este repositorio, se irá almacenando todas la codificación relacionada con la creación de tests unitarios para las funcionalidades del módulo Agora-Results del proyecto open soure Agora-Voting.


## A tener en cuenta - Entorno virtual

Para que funcionen los tests se debe de estar seguro que se está en el entorno virtual de Agora Results.

Este entorno virtual se puede instalar desde la guía documentada en la propia Agora Results de Agora Voting

## A tener en cuenta - PyBuilder

Se usa PyBuilder para ejecutar los tests automáticamente, además de construir la aplicación y tener en cuenta las dependencias.

Para tener implementado esta tecnologia se debe de instalar y posteriormente, desde la ruta donde se encuentra el archivo build.py, instalar las depedencias que hubiese.

```sh
$ pip install pybuilder
$ pyb install_dependencies
```


## Uso

Para ejecutar los test se debe de usar el siguiente comando

```sh
$ pyb
```

Para poder visualizar mejor los errores que pudieran haber se usa el siguiente comando

```sh
$ pyb -v
```
