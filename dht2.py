import machine
import network
import Wifi_credential
from umqtt.simple import MQTTClient
import dht
import time

led = machine.Pin(2,machine.Pin.OUT)
d= dht.DHT11(machine.pin(2))

sta = network.WLAN(network.STA_IF)
if not sta.isconnected():
    print('connecting to network')
    sta.active(True)
    sta.connect(Wifi_credential.ssid, Wifi_credential.password)
    while not sta.isconnected():
        pass
print('network config:', sta.ifconfig())

SERVER = "mqtt.thingspeak.com"
Client = MQTTClient("umqtt_client",SERVER)
CHANNEL_ID = "1970485"
WRITE_API_KEY = "9GAOMPHN92S6LG44"
topic = "channels"+CHANNEL_ID+"/publish/"+WRITE_API_KEY
UPDATE_TIME_INTERVAL = 5000
last_update = time.ticks_ms()

while True :
    if time.ticks_ms() - last_update >= UPDATE_TIME_INTERVAL
    d.measure()
    t=d.temperature()
    h=d.humidity()
    payload = "field1={}&field2={}" .format(str(t), str(h))
    client.connect()
    client.disconnect()
    print(payload)
    led.value(not led.value())
    last_update = time.ticks_ms()
                    