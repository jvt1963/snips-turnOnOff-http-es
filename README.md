# Snips - Acción para encender/apagar dispositivos mediante peticiones http get
[![MIT License](https://img.shields.io/badge/license-MIT-blue.svg)](https://raw.githubusercontent.com/jvt1963/snips-turnOnOff-http/master/LICENSE)

Acción programada en Python compatible con `snips-skill-server`.

## Instalación
### Prerrequisitos

Es necesario agregar la aplicación On-Off-http-es al asistente. La aplicación está disponible para los asistentes en español en la [consola de Snips](https://console.snips.ai)

### SAM (recomendado)
Para instalar la acción en el dispositivo, se puede utilizar [Sam](https://snips.gitbook.io/getting-started/installation)

`sam install action -g https://github.com/jvt1963/snips-turnOnOff-http.git`

### Manually

Copy it manually to the device to the folder `/var/lib/snips/skills/`
You'll need `snips-skill-server` installed on the pi

`sudo apt-get install snips-skill-server`

Stop snips-skill-server & generate the virtual environment
```
sudo systemctl stop snips-skill-server
cd /var/lib/snips/skills/snips-skill-weather-tts/
sh setup.sh
sudo systemctl start snips-skill-server
```

## How to trigger

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
