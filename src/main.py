import asyncio
import device_ble
import constants

async def main():
    device = device_ble.DeviceBle()
    try: 
        await device.connect()

        await device.prep()
        await asyncio.sleep(4)
        
        print( "SPEED 100")
        await device.send_command("SPEED", 100)
        await asyncio.sleep(4)

        print( "SPEED -100")
        await device.send_command("SPEED", -100)
        await asyncio.sleep(4)

        print( "SPEED 300")
        await device.send_command("SPEED", 300)
        await asyncio.sleep(4)

        print( "SPEED -300")
        await device.send_command("SPEED", -300)
        await asyncio.sleep(4)

        print( "Sound Horn")
        await device.send_command("SOUND", "HORN")
        await asyncio.sleep(4)

        print( "Sound BRAKE")
        await device.send_command("SOUND", "BRAKE")
        await asyncio.sleep(4)

        print( "Color Pink")
        await device.send_command("LIGHT", "PINK")
        await asyncio.sleep(4)

        print( "Color PURPLE")
        await device.send_command("LIGHT", "PURPLE")
        await asyncio.sleep(4)

        print( "Color RED")
        await device.send_command("LIGHT", "RED")
        await asyncio.sleep(4)

        print( "Color WHITE")
        await device.send_command("LIGHT", "WHITE")
        await asyncio.sleep(4)

        print( "Color OFF")
        await device.send_command("LIGHT", "OFF")
        await asyncio.sleep(4)


        await device.disconnect()

    except Exception as e:
        print(e)
    
asyncio.run(main())