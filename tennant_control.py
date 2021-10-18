import paho.mqtt.client as mqtt 
from storage import *
import requests
import logging

client = mqtt.Client()
logging.basicConfig(filename='single_unit_control.log', format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p', level=logging.INFO)

ents = {
    '1': 'light.hue_white_lamp_1', 
    '2': 'light.hue_white_lamp_2', 
    '3': 'light.hue_white_lamp_3', 
    '4': 'light.hue_white_lamp_4', 
    '5': 'light.hue_white_lamp_5', 
    '6': 'light.hue_white_lamp_6', 
    '7': 'light.hue_white_lamp_7', 
    '8': 'light.hue_white_lamp_8', 
    '9': 'light.hue_white_lamp_9', 
    '10': 'light.hue_white_lamp_10', 
    '11': 'light.hue_white_lamp_11', 
    '12': 'light.hue_white_lamp_12', 
    '13': 'light.hue_white_lamp_13', 
    'color1': 'light.hue_color_lamp_1'
}

def on_message_lights(mosq, obj, msg):
    topic_entity = msg.topic[12:]
    target = ents.get(topic_entity)
    logging.info(target + str(msg.payload.decode("utf-8")))

    def control_ent():
        turn_off = 'http://192.168.0.51:8123/api/services/light/turn_off'
        turn_on = 'http://192.168.0.51:8123/api/services/light/turn_on'
        headers = {
            "Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiI3MzVhYTM3NjBjNDk0MGViYTI3YTk0ZGRlMzk5NzI5NCIsImlhdCI6MTYyOTQ3OTYyMiwiZXhwIjoxOTQ0ODM5NjIyfQ.4AxQruD_7LWA5kT5SMNeWC2T1qPFe_0xTbBJDPJ9YdA",
            "content-type": "application/json",
            }
        url = "http://192.168.0.51:8123/api/states/%s" % (target)
        myobj = '{"entity_id": "%s"}' % target
        if str(msg.payload.decode("utf-8")) == 'off':
            response = requests.post(turn_off, data=myobj, headers=headers)
            logging.info('Device turned off')
        elif str(msg.payload.decode("utf-8")) == 'on':
            response = requests.post(turn_on, data=myobj, headers=headers)
            logging.info('Device turned on')
            
    control_ent()

if __name__ == '__main__':

    client.message_callback_add('unit/lights/1', on_message_lights)
    client.message_callback_add('unit/lights/2', on_message_lights)
    client.message_callback_add('unit/lights/3', on_message_lights)
    client.message_callback_add('unit/lights/4', on_message_lights)
    client.message_callback_add('unit/lights/5', on_message_lights)
    client.message_callback_add('unit/lights/6', on_message_lights)
    client.message_callback_add('unit/lights/7', on_message_lights)
    client.message_callback_add('unit/lights/8', on_message_lights)
    client.message_callback_add('unit/lights/9', on_message_lights)
    client.message_callback_add('unit/lights/10', on_message_lights)
    client.message_callback_add('unit/lights/11', on_message_lights)
    client.message_callback_add('unit/lights/12', on_message_lights)
    client.message_callback_add('unit/lights/13', on_message_lights)
    client.message_callback_add('unit/lights/color1', on_message_lights)

    client.connect("localhost", port=1883)
    client.subscribe('unit/#', 0)
    logging.info('Message received')
    client.loop_forever()    