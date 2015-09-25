## El entorno de ejecución

El script emplea:
	1 La función PHP [strftime](http://php.net/manual/es/function.strftime.php) que basándose en los locale registrados en el sistema y a partir de un formato y timestamp dado retorna una cadena formateada al localismo establecido mediante [setlocale](http://php.net/manual/es/function.setlocale.php).
	2 Instancias de DateTime que se ven influidas por el date.timezone del archivo php.ini correspondiente.
	3 La nueva sintaxis para [declarar arrays](http://php.net/manual/es/language.types.array.php).
 
Por estos motivos y para lograr un entorno de ejecución valido, opte por emplear una caja Vagrant donde poder instalar PHP 5.6 y los locale necesarios.

El Vagrantfile adjunto se basa en [ubuntu/precise32](https://vagrantcloud.com/ubuntu/boxes/precise32)(vagrant init ubuntu/precise32) y emplea VirtualBox como proveedor. Se estableció un directorio compartido(config.vm.synced_folder "share_vagrant_host/", "/share_vagrant") para colocar el script y test.

Detallo los comandos empleados para preparar el entorno, instalar los locale y php 5.6, así como las referencias a las instrucciones originales.

```shell
vagrant up --provider virtualbox
```

```shell
vagrant ssh
```

```shell
sudo apt-get update
```

```shell
sudo locale-gen ru_RU
sudo locale-gen ru_RU.UTF-8
sudo locale-gen es_ES
sudo locale-gen es_ES.UTF-8
```
[How do I add locale to ubuntu server?](http://askubuntu.com/questions/76013/how-do-i-add-locale-to-ubuntu-server)

```shell
sudo apt-get install software-properties-common
sudo add-apt-repository ppa:ondrej/php5-5.6
sudo apt-get update
sudo apt-get upgrade
sudo apt-get install php5
```
[Upgrading Ubuntu to PHP 5.6.4](https://www.digitalocean.com/community/questions/upgrading-ubuntu-to-php-5-6-4)
La respuesta señalada por Andrew SB implica agregar al sistema un repositorio de [Ondřej Surý](https://launchpad.net/~ondrej) contribuyente del paquete php5 para Debian.
[software-properties-common](https://packages.debian.org/es/sid/admin/software-properties-common)
[ppa:ondrej/php5-5.6](https://launchpad.net/~ondrej/+archive/ubuntu/php5-5.6)

Como se señalo en el segundo numeral, el manejo de fechas se realiza mediante [DateTime](http://php.net/manual/es/datetime.construct.php), cabe aclarar que esta clase se ve influida por el apartado date.timezone del archivo php.ini correspondiente. Este valor puede ser modificado mediante [date_default_timezone_set](http://php.net/manual/es/function.date-default-timezone-set.php) o pasado un DateTimeZone concreto como argumento al constructor de DateTime.
El presente script no establece un timezone especifico ya que se espera que la maquina en que se ejecute disponga de un valor de date.timezone acorde en el archivo archivo php.ini correspondiente.

```php
// modificación general de [timezone](http://php.net/date.timezone)
date.timezone = America/Montevideo

// modificación en tiempo de ejecución
date_default_timezone_set('America/Montevideo');

// instancia concreta de DateTime con zona horaria de Montevideo
$fecha = new DateTime(null, new DateTimeZone('America/Montevideo'));
```

## El programa

Como se señalo anteriormente, el archivo Vagrantfile monta un directorio compartido donde se encuentra el programa.

```shell
cd /share_vagrant/
```

Para realizar la llamada al programa se le debe pasar el parámetro -a con el valor del año que se quiera consultar.

```shell
php vb256.php -a 2015
```

Tambien existe un script para realizar una serie de verificaciones referidas a locale, timezone y llamados al programa con la finalidad de verificar su respuestas.

```shell
php pruebas.php
```

#### Sobre la traducción

La traducción elegida fue realizada por Bing porque la conversión de RU a ES tanto en este traductor como Google fue interpretada con el mismo sentido.

La frase base fue "El día del programador en 2015 se celebró el sábado 13 de septiembre" y la traducción ofrecida "День разработчика в 2015 году был проведен в субботу, 13 сентября", al realizar la conversión RU-ES los resultados fueron: 
- Bing: "Día del Desarrollador en 2015, se llevó a cabo el sábado 13 de septiembre"
- Google: "Developer Day en 2015 se llevó a cabo el sábado, 13 de septiembre"

Nota: Tras la traducción de una serie de respuestas del programa, note que uno de los traductores realizo la misma conversión para todos los casos; mientras que el otro interpreto la frases de diferente modo señalando "se llevó", "se celebró" o "se realizará"; aparentemente las variaciones de los días influyo en las interpretaciones ofrecidas.


## Día de l[a&o]s Programador[a&e]s y otros materiales consultados

- [Día de los Programadores](https://es.wikipedia.org/w/index.php?title=D%C3%ADa_de_los_Programadores&oldid=85106363 "Día de los Programadores")
- [256day](http://www.256day.org/ "256day")

#### El problema de locale 
Me llevo una semana comprender cómo funcionaba, estos posts fueron de ayuda aunque en la implementación final no se emplean. Resolver este punto motivo el empleo de Vagrant para proporcionar un entorno de ejecución correcto y evitar los problemas que pueden producirse en sistemas que no poseen los locale necesarios. 
- [Локали и кодировки](http://anton-pribora.ru/articles/php/locales/ "Локали и кодировки")
- [cp1251 a utf-8](http://stackoverflow.com/questions/13508429/php-converting-from-cp1251-to-utf8 "cp1251 a utf-8")

