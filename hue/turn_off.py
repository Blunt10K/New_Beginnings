from hue_controller import Controller

def connect():
    while True:
        try:
            cntrla = Controller()
            return cntrla
        except:
            pass
    
cntrla = connect()
scene = cntrla.get_scene('off')

cntrla.control(scene)