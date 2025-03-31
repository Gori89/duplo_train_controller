from machine import Pin

pin = Pin("LED", Pin.OUT)

def blink_on():
    pin.toggle()
    print("Blink on")

def blink_off():
    pin.off()
    print("Blink off")