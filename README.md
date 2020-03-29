# Acortador URL

Este es un proyecto adaptado con reglas que he ido aprendido, gran parte del código original es del siguiente curso de Udemy: <https://www.udemy.com/course/curso-django-creando-un-acortador-url/>

Tener presente estos comandos para instalar y crear un entorno con Python3

```sh
$ sudo chmod 777 -R /webapp/acortador_url  # Permisos completos a la carpeta
$ sudo apt-get install python3-venv -y   #instala
python3 -m venv env_acortador    #crear entorno
```

## Tips

Hay una serie de comando en Linux que ayudaran bastante para evitar complicaciones **que son muy frecuentes**

```sh
sudo fuser -k 8050/tcp      # Liberar puerto en especifico
code .         # Abre el proyecto con visual code desde el Terminal
pip3 install -r requeriments.txt   # Instala las librerias que se encuentren en el a rchivo
```

```sh
django-admin startproject acortador     # Creamos la carpeta del proyecto
python3 manage.py startapp core           # Dentro del proyecto creamos el App 
```

## Guias

Vamos apoyarnos del siguente link para las vista basadas en clases:
<https://ccbv.co.uk/projects/Django/2.2/>
Para escribir el readme.md usaremos:
<https://stackedit.io/app#> y <https://dillinger.io/>

## Métodos Django

Cómo sobreescribir el método save():
<https://yo.toledano.org/desarrollo/como-sobreescribir-el-metodo-save-en-django.html>


