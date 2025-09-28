import paho.mqtt.client as mqtt

#using online broker hivemq instedof mosquitto
broker = "broker.hivemq.com"  

#default port for MQTT
port = 1883

#create temprature TOPIC
topic = "test/random_temperature"

#callback function when reciveing new message 
#converting date from bytes to string by payload.decode() function then print to terminal
def convert_message(client, userdata, msg):
    print(f"received: {msg.payload.decode()} C")


#creat new mqtt client object to be listener
client = mqtt.Client()

#create connection between client and callback function when recive new bytes ---> go to convert_message function to convert data
client.on_message = convert_message

#client connect to the same broker and port publisher used
client.connect(broker, port, 60)

#lestin to temp topic
client.subscribe(topic)

#if all above rigth subscriber start to listen to publisher 
print("listening for temperature values")
#loop to lestin while program inturrupted ------> crl+c
client.loop_forever()

