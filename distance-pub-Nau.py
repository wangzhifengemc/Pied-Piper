#!/usr/bin/env python
import RPi.GPIO as GPIO
import time
#import json
import paho.mqtt.client as mqtt

# initialize GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setup(16,GPIO.OUT,initial=GPIO.LOW)
GPIO.setup(18,GPIO.IN)

broker_address="192.168.43.246"
broker_port="443"
broker_topic="FIDELITY.ADS"
print("creating new instance")
client = mqtt.Client("pub5") #create new instance
ID="3"
print("connecting to broker")
client.connect(broker_address, broker_port) #connect to broker

def checkdist():
        GPIO.output(16, GPIO.HIGH)
        time.sleep(0.000015)
        GPIO.output(16, GPIO.LOW)
        while not GPIO.input(18):
                pass
        t1 = time.time()
        while GPIO.input(18):
                pass
        t2 = time.time()
        return (t2-t1)*340/2


def loop():
	while True:
            d = checkdist()
            t3 = time.strftime("%-m/%-d/%Y %H:%M:%S",time.localtime())
#            df = "ID:%s,Distance,%0.2f" %(ID,d)
            df = "{\"id\":\"%s\",\"time\":\"%s\",\"value\":\"%0.2f\"}" %(ID,t3,d)
            print df
#            print 'Distance: ' + df
#            print json.dumps(df)
#            client.publish("Wzf001",json.dumps(df))
            client.publish(broker_topic,df)
            time.sleep(1)

if __name__ == '__main__':

	try:
		loop()
	except KeyboardInterrupt: 
                GPIO.cleanup()
		print 'The end !'
