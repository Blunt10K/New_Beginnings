from hue_controller import Controller

def connect():
    while True:
        try:
            cntrla = Controller()
            return cntrla
        except:
            pass

def main():   
    cntrla = connect()
    scene = cntrla.get_scene('coding')

    cntrla.control(scene)

if __name__ == "__main__":
    main()