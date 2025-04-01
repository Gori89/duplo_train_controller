async def connection(device, conn_led):
    if device.is_connected:
        print("disconn")
        await device.disconnect()
        conn_led.blink_off()
    else:
        print("Conn")
        print(device)
        await device.connect()
        print(conn_led)
        conn_led.blink_on()

async def brake(device):
    await device.send_command("SOUND", "BRAKE")
    await device.send_command("SPEED", 0)
    
async def station(device):
    await device.send_command("SOUND", "STATION")

async def water(device):
    await device.send_command("SOUND", "WATER")

async def horn(device):
    await device.send_command("SOUND", "HORN")

async def depart(device):
    await device.send_command("SOUND", "DEPART")

async def light_switch(device):
    await device.send_command("LIGHT", "OFF")

async def light_color(device, color):
    await device.send_command("LIGHT", color)

async def speed(device, speed):
    await device.send_command("SPEED", speed)
