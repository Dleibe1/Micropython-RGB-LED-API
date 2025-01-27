import esp
import network
import time
import ubinascii

wlan_id = "YOUR-LAN-IOD"
wlan_pass = "YOUR-LAN-PW"

mac = ubinascii.hexlify(network.WLAN().config('mac'),':').decode()
print("MAC: " + mac)

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
while wlan.status() is network.STAT_CONNECTING:
    time.sleep(1)
while not wlan.isconnected():
    wlan.connect(wlan_id, wlan_pass)
print("Connected... IP: " + wlan.ifconfig()[0])  
