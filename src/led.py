from machine import Pin



class Led(Pin):

    def __init__(self, id):
        super().__init__(id, Pin.OUT)

    def blink_on(self):
        self.on()
        print("Blink on")

    def blink_off(self):
        self.off()
        print("Blink off")