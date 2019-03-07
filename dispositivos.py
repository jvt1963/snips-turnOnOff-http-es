#!/usr/bin/env python3

respuesta = ['vale','de acuerdo','como desees','tú mandas','ahora mismo']

dispositivo = list()
dispositivoOn = list()
dispositivoOff = list()

dispositivo.append("luz de la cocina")
dispositivoOn.append("http://192.168.1.220:8080/json.htm?type=command&param=switchlight&idx=23&switchcmd=On")
dispositivoOff.append("http://192.168.1.220:8080/json.htm?type=command&param=switchlight&idx=23&switchcmd=Off")

dispositivo.append("luz del dormitorio")
dispositivoOn.append("http://192.168.1.220:8080/json.htm?type=command&param=switchlight&idx=19&switchcmd=On")
dispositivoOff.append("http://192.168.1.220:8080/json.htm?type=command&param=switchlight&idx=19&switchcmd=Off")

# Add new dispositivos 
# dispositivo.append([dispositivo name, slot])
# dispositivoOn.append([url On])
# dispositivoOff.append([url Off])

