#!/usr/bin/env python2
from hermes_python.hermes import Hermes 
import requests
from devices import device, deviceOn, deviceOff

MQTT_IP_ADDR = "localhost" 
MQTT_PORT = 1883 
MQTT_ADDR = "{}:{}".format(MQTT_IP_ADDR, str(MQTT_PORT)) 


def device_number(current_slot):
    for x in device:
        if x == current_slot:
            break
    return device.index(x)


def intent_received(hermes, intent_message):
    sentence = 'Me has pedido '
    device_name_slot = intent_message.slots.device_name.first()
    devnum = device_number(device_name_slot.value)

    if intent_message.intent.intent_name == 'jaimevegas:Encender':
        sentence += 'que encienda ' + device_name_slot.value
        r = requests.get(deviceOn[devnum])
        
    elif intent_message.intent.intent_name == 'jaimevegas:Apagar':
        sentence += 'que apague ' + device_name_slot.value
        r = requests.get(deviceOff[devnum])
        
    else:
        return
    
    hermes.publish_end_session(intent_message.session_id, sentence)
    
    
with Hermes(MQTT_ADDR) as h:
    h.subscribe_intents(intent_received).start()
