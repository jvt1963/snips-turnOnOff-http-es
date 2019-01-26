#!/usr/bin/env python2
from hermes_python.hermes import Hermes 
import requests
from dispositivos import dispositivo, dispositivoOn, dispositivoOff

MQTT_IP_ADDR = "localhost" 
MQTT_PORT = 1883 
MQTT_ADDR = "{}:{}".format(MQTT_IP_ADDR, str(MQTT_PORT)) 


def dispositivo_number(current_slot):
    for x in dispositivo:
        if x == current_slot:
            break
    return dispositivo.index(x)


def intent_received(hermes, intent_message):
    sentence = 'Me has pedido '
    dispositivo_name_slot = intent_message.slots.dispositivo_name.first()
    devnum = dispositivo_number(dispositivo_name_slot.value)

    if intent_message.intent.intent_name == 'jaimevegas:Encender':
        sentence += 'que encienda ' + dispositivo_name_slot.value
        r = requests.get(dispositivoOn[devnum])
        
    elif intent_message.intent.intent_name == 'jaimevegas:Apagar':
        sentence += 'que apague ' + dispositivo_name_slot.value
        r = requests.get(dispositivoOff[devnum])
        
    else:
        return
    
    hermes.publish_end_session(intent_message.session_id, sentence)
    
    
with Hermes(MQTT_ADDR) as h:
    h.subscribe_intents(intent_received).start()
