# Snips - Acción para encender/apagar dispositivos mediante peticiones http get
[![MIT License](https://img.shields.io/badge/license-MIT-blue.svg)](https://raw.githubusercontent.com/jvt1963/snips-turnOnOff-http/master/LICENSE)

Acción programada en Python compatible con `snips-skill-server`.

## Instalación
### Prerrequisitos

Es necesario agregar la aplicación On-Off-http-es al asistente. La aplicación está disponible para los asistentes en español en la [consola de Snips](https://console.snips.ai)

### SAM (recomendado)
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

2) Editar el archivo dispositivos.py
Puede hacerse con nano:
  # sudo nano /var/lib/snips/skills/snips-turnOnOff-http-es/dispositivos.py


`Hey Snips`

`Turn on kitchen lights`

## Logs
Show snips-skill-server logs with sam:

`sam service log snips-skill-server`

Or on the device:

`journalctl -f -u snips-skill-server`

Check general platform logs:

`sam watch`

Or on the device:

`snips-watch`
