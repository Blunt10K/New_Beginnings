import requests
import json

class Lights:
    def __init__(self, login):
        self.lights = login + 'lights/'
        self.state = requests.get(self.lights,timeout=1).json()
    
    def updated_state(self):
        return requests.get(self.lights).json()
    
    def get_light_keys(self):
        return self.state.keys()

    def turn_on(self, scenes):
        self.state = requests.get(self.lights).json()

        for light in scenes:
            current_state = self.state[light]["state"]["on"]
            desired_state = scenes[light]["on"]

            if(current_state and desired_state):
                del scenes[light]['on']

            address = self.lights+light+'/state/'
            data = json.dumps(scenes[light])
            response = requests.put(address,data = data)

            # print(response.json())
