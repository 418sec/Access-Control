#!/~/.pyenv/versions/3.9.1/bin/python
# -*- coding: <utf-8> -*-

import requests

class Controller:
    def __init__(self, ip):
        self.__ip_address = str(ip)
        self.__digital_output = "rest/output/"
        self.__digital_input = "rest/input/"

    
    def construct_uri(self):
        uri = f"http://{self.__ip_address}:8080/{self.__digital_output}1_01"
        return uri 


    def turn_switch_on(self):
        response = requests.post(Controller.construct_uri(self), data={"value": 1, "mode": "Simple"})
        
    
    def turn_switch_off(self):
        response = requests.post(Controller.construct_uri(self), data={"value": 0, "mode": "Simple"})

        return 1
