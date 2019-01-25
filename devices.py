#!/usr/bin/env python2

device = list()
deviceOn = list()
deviceOff = list()

device.append("kitchen lights")
deviceOn.append("http://192.168.1.220:8080/json.htm?type=command&param=switchlight&idx=23&switchcmd=On")
deviceOff.append("http://192.168.1.220:8080/json.htm?type=command&param=switchlight&idx=23&switchcmd=Off")

device.append("bedroom lights")
deviceOn.append("http://192.168.1.220:8080/json.htm?type=command&param=switchlight&idx=19&switchcmd=On")
deviceOff.append("http://192.168.1.220:8080/json.htm?type=command&param=switchlight&idx=19&switchcmd=Off")

# Add new devices 
# device.append([device name, slot])
# deviceOn.append([url On])
# deviceOff.append([url Off])

