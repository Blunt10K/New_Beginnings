import json
from start_up import connect

def get_desired_keys(state):
    keys = ("on","bri","hue","sat")
    settings = {k: state[k] for k in keys}

    return settings

cntrla = connect()

state = cntrla.observe_lights()

scene = {}
for key in state.keys():
    scene.update({str(key):get_desired_keys(state[key]["state"])})

print(scene)
scene_name = input("Scene name?")
filepath = "./scenes/"+scene_name+".json"

with open(filepath,'w') as json_file:
    json.dump(scene,json_file)