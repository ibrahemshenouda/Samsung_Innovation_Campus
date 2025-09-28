import paho.mqtt.client as mqtt
import time
import random

#using online broker hivemq instedof mosquitto
broker = "broker.hivemq.com"  

#default port for MQTT
port = 1883

#create temprature TOPIC
topic = "test/random_temperature"

#create mqtt client object to be publisher
client = mqtt.Client()         
  
#connect to broker at port 1883, waiting time 60s 
client.connect(broker, port, 60)  

while True:
#create random value and store in temp var
    temperature = round(random.uniform(20.0, 30.0), 2)  
    #publish this value at temp topic then print in terminal every 2 sec
    client.publish(topic, temperature)                 
    print(f"published: {temperature} C")               
    time.sleep(2)                                     

