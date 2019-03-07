#!/usr/bin/env python3
from hermes_python.hermes import Hermes 
import requests
from dispositivos import dispositivo, dispositivoOn, dispositivoOff, respuesta
import random

MQTT_IP_ADDR = "localhost" 
MQTT_PORT = 1883 
MQTT_ADDR = "{}:{}".format(MQTT_IP_ADDR, str(MQTT_PORT)) 


def dispositivo_number(current_slot):
    for x in dispositivo:
        if x == current_slot:
            break
    return dispositivo.index(x)


def intent_received(hermes, intent_message):
    sentence = random.choice(respuesta)
    dispositivo_slot = intent_message.slots.dispositivo.first()
    devnum = dispositivo_number(dispositivo_slot.value)

    if intent_message.intent.intent_name == 'jaimevegas:Encender':
        r = requests.get(dispositivoOn[devnum])
        
    elif intent_message.intent.intent_name == 'jaimevegas:Apagar':
        r = requests.get(dispositivoOff[devnum])
        
    else:
        return
    
    hermes.publish_end_session(intent_message.session_id, sentence)
    
    
with Hermes(MQTT_ADDR) as h:
    h.subscribe_intents(intent_received).start()

