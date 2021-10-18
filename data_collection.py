import json
from requests import get
import sqlite3
from contextlib import closing
import paho.mqtt.client as mqtt 
import time
from storage import *
import logging

logger = logging.getLogger(__name__)  # use module name
logging.basicConfig(filename='multi_install_data_collection.log', format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p', level=logging.INFO)


client = mqtt.Client()
client.connect("localhost", port=1883)

def dataCollection():
    logging.info('Data Collection Starting')
    while True:
        for key in ip_dict.keys():
            logging.info('IP' + key)
            for i in ents:
                getState(key, ip_dict.get(key), i)
        logging.info('Data Collection Cycle Complete')
        time.sleep(5)

def getState(arg1, arg2, arg3):
    state_values = []
    url = "http://%s:8123/api/states/%s" % (arg1, arg3)
    logging.info(url)
    headers = {
        "Authorization": "Bearer %s" % arg2,
        "content-type": "application/json",
        }
    response = get(url, headers=headers)
    state_data = response.json()
    connection = sqlite3.connect("%s.db" % arg1)
    cursor = connection.cursor()
    try:
        cursor.execute("CREATE TABLE home_assistant_data (entity_id TEXT, state TEXT, last_changed TEXT)")
    except:
        pass

    state_values.extend([state_data["entity_id"], state_data["state"], state_data["last_changed"]])
    cursor.execute("INSERT INTO home_assistant_data VALUES ('%s', '%s', '%s')" % (state_values[0], state_values[1], state_values[2]))
    connection.commit()
    client.publish("%s/%s" % (arg1, state_values[0]), state_values[1])

if __name__ == '__main__':
    dataCollection()
