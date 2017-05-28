#!/usr/bin/env/python

import os
import paho.mqtt.client as mqtt
from time import sleep
import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

SleepTimeL = 0.2

pinList = [2,3,4,17,27,22,10,9]

for i in pinList:
	GPIO.setup(i, GPIO.OUT)
	GPIO.output(i, GPIO.HIGH)

# The callback for when the client receives a CONNACK response from the server.
def main():

  def on_connect(client, userdata, flags, rc):
	client.subscribe("home/office/relay/#")

  def on_message(client, userdata, msg):
	if msg.topic == "home/office/relay/1" :
		if msg.payload == "ON" :
			GPIO.output(2, GPIO.LOW)
			time.sleep(SleepTimeL);
			#print "Outlet 1 ON"
		if msg.payload == "OFF" :
			GPIO.output(2, GPIO.HIGH)
			time.sleep(SleepTimeL);
			#print "Outlet 1 OFF"
	if msg.topic == "home/office/relay/2" :
		if msg.payload == "ON" :
			GPIO.output(3, GPIO.LOW)
			time.sleep(SleepTimeL);
			#print "Outlet 2 On"
		if msg.payload == "OFF" :
			GPIO.output(3, GPIO.HIGH)
			time.sleep(SleepTimeL);
			#print "Outlet 2 Off"
	if msg.topic == "home/office/relay/3" :
		if msg.payload == "ON" :
			GPIO.output(4, GPIO.LOW)
			time.sleep(SleepTimeL);
			#print "Outlet 3 ON"
		if msg.payload == "OFF" :
			GPIO.output(4, GPIO.HIGH)
			time.sleep(SleepTimeL);
			#print "Outlet 3 OFF"
	if msg.topic == "home/office/relay/4" :
		if msg.payload == "ON" :
			GPIO.output(17, GPIO.LOW)
			time.sleep(SleepTimeL);
			#print "Outlet 4 ON"
		if msg.payload == "OFF" :
			GPIO.output(17, GPIO.HIGH)
			time.sleep(SleepTimeL);
			#print "Outlet 4 OFF"
	if msg.topic == "home/office/relay/5" :
		if msg.payload == "ON" :
			GPIO.output(27, GPIO.LOW)
			time.sleep(SleepTimeL);
			#print "Outlet 5 ON"
		if msg.payload == "OFF" :
			GPIO.output(27, GPIO.HIGH)
			time.sleep(SleepTimeL);
			#print "Outlet 5 OFF"
	if msg.topic == "home/office/relay/6" :
		if msg.payload == "ON" :
			GPIO.output(22, GPIO.LOW)
			time.sleep(SleepTimeL);
			#print "Outlet 6 ON"
		if msg.payload == "OFF" :
			GPIO.output(22, GPIO.HIGH)
			time.sleep(SleepTimeL);
			#print "Outlet 6 OFF"
	if msg.topic == "home/office/relay/7" :
		if msg.payload == "ON" :
			GPIO.output(10, GPIO.LOW)
			time.sleep(SleepTimeL);
			#print "Outlet 7 ON"
		if msg.payload == "OFF" :
			GPIO.output(10, GPIO.HIGH)
			time.sleep(SleepTimeL);
			#print "Outlet 7 OFF"
	if msg.topic == "home/office/relay/8" :
		if msg.payload == "ON" :
			GPIO.output(9, GPIO.LOW)
			time.sleep(SleepTimeL);
			#print "Outlet 8 ON"
		if msg.payload == "OFF" :
			GPIO.output(9, GPIO.HIGH)
			time.sleep(SleepTimeL);
			#print "Outlet 8 OFF"

	
  client = mqtt.Client()
  client.on_connect = on_connect
  client.on_message = on_message

  client.connect("mosquitto", 1883, 60)

  client.loop_forever()

if __name__ == '__main__':
	try:
	  	main()
	except KeyboardInterrupt:
		GPIO.cleanup()