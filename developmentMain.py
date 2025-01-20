#Copy the code from the developmentMain.py into main.py on the ESP32 when ready to test

from micropyserver import MicroPyServer
from machine import Pin, PWM
import utils
''' wifi connection is in boot.py '''
frequency = 5000
''' LED's take a duty cycle value (brightness) 0 - 1024'''
red = PWM(Pin(5), frequency)
green = PWM(Pin(18), frequency)
blue = PWM(Pin(19), frequency)

def get_colors_from_params(request):
    ''' request handler '''
    params = utils.get_request_query_params(request)
    red_param = params["red"]
    green_param = params["green"]
    blue_param = params["blue"]
    red.duty(int(red_param))
    green.duty(int(green_param))
    blue.duty(int(blue_param))
    server.send(f"You have set the colors to \n Red: {red_param} \n Green: {green_param} \n Blue: {blue_param}.")

server = MicroPyServer()
''' add route '''
server.add_route("/", get_colors_from_params)
''' start server '''
server.start()
