import json
import requests
from lights import Lights

class Controller:
    def __init__(self):
        self.root = "http://192.168.0.101/api/"
        self.usr = "Cmwss66OU62BGRIuwy8RE5FX3mDvfktlYszlJMlP/"
        self.login = self.root+ self.usr
        self.room = Lights(self.login)

    def get_scene(self, scene):
        filepath = './scenes/'+scene+'.json'

        with open(filepath) as json_file:
            settings = json.load(json_file)
        
        return settings

    def observe_lights(self):
        return self.room.updated_state()
    
    def control(self,scene):
        self.room.turn_on(scene)
