# Snips - Acción para encender/apagar dispositivos mediante peticiones http get
[![MIT License](https://img.shields.io/badge/license-MIT-blue.svg)](https://raw.githubusercontent.com/jvt1963/snips-turnOnOff-http/master/LICENSE)

Acción programada en Python compatible con `snips-skill-server`.

## Instalación
### Prerrequisitos

Es necesario agregar la aplicación On-Off-http-es al asistente. La aplicación está disponible para los asistentes en español en la [consola de Snips](https://console.snips.ai)

### Instalación con SAM (recomendado)
Para instalar la acción en el dispositivo, se puede utilizar [Sam](https://snips.gitbook.io/getting-started/installation)

`sam install action -g https://github.com/jvt1963/snips-turnOnOff-http-es.git`

### Instalación manual

Copiar los archivos de la acción en una carpeta dentro de la ruta `/var/lib/snips/skills/`
Es necesario que esté instalado en la RPi `snips-skill-server`

`sudo apt-get install snips-skill-server`

Parar el 'snips-skill-server' y generar el entorno virtual
```
sudo systemctl stop snips-skill-server
cd /var/lib/snips/skills/snips-turnOnOff-http-es/
sh setup.sh
sudo systemctl start snips-skill-server
```

## Configurar los comandos

Supongamos, por ejemplo, que tenemos una lámpara que se enciende y se apaga con las siguientes peticiones http:
Encendido: http://192.168.1.125/lamparaOn.htm
Apagado: http://192.168.1.125/lamparaOff.htm

Para que Snips encienda y apague la lámpara hay que seguir los siguientes pasos:

1) Editar la aplicación en la consola de Snips para añadir al Slot "dispositivo" de los "intents" "Encender" y "Apagar" un nuevo valor con el nombre que queramos dar al dispositivo (en este caso añadiríamos el valor "Lámpara", por ejemplo).

Tras realizar esta operación, hay que actualizar el asistente. 

Con SAM, se actualizaría con el siguiente comando:

  $ sam update-assistant

2) Editar el archivo dispositivos.py
Puede hacerse con nano:
  $ sudo nano /var/lib/snips/skills/snips-turnOnOff-http-es/dispositivos.py

En este archivo se puede configurar el mensaje de respuesta que dirá Snips al ejecutar la orden. Este mensaje se configura editando la siguiente línea:

  respuesta = ['vale','de acuerdo','como desees','tú mandas','ahora mismo']

Al ejecutar una orden, Snips seleccionará aleatoriamente uno de los textos de la lista anterior. Para personalizar los mensajes basta con sustituir los que vienen por defecto, o añadir cualquier otro mensaje a la lista.

En el archivo dispositivos.py hay que indicar también las peticiones http que debe ejecutar Snips cuando se le ordena encender o apagar un dispositivo. Para ello hay que añadir tres líneas de código, siguiendo el modelo siguiente (con los datos del ejemplo):

  dispositivo.append("Lampara")
  dispositivoOn.append("http://192.168.1.125/lamparaOn.htm")
  dispositivoOff.append("http://192.168.1.125/lamparaOn.htm")

Una vez salvados los cambios en el archivo dispositivos.py, hay que reiniciar el 'snips-skill-server'

Se puede hacer con el siguiente comando, que reinicia todas las funciones de Snips:

  $ sudo systemctl restart 'snips-*'

## Uso de la aplicación

Para pedir a Snips que encienda o apague la lámpara, se puede utilizar cualquiera de las frases añadidas a los intentos "Encender" y "Apagar", utilizando el nombre que hayamos dado al dispositivo de que se trate. Siguiendo con el ejemplo, podría ser:

  "Hey Snips, enciende la lámpara"
  "Hey Snips, apaga la lámpara"
  "Hey Snips, conecta la lámpara"
  "Hey Snips, desconecta la lámpara"
  
Se pueden ver todas las frases añadidas a los intentos (y añadir otras frases, si se quiere) editando la aplicación con la consola de Snips.

## Integración con Domoticz

Esta aplicación facilita la el uso de Snips con Domoticz mediante la API JSON de Domoticz.

https://www.domoticz.com/wiki/Domoticz_API/JSON_URL's

