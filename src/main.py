import asyncio
import device_ble
import constants

async def main():
    device = device_ble.DeviceBle()
    try: 
        await device.connect()

        while x != "OUT":
            print('Enter comand (speed int, sound or color):')
            x = input()
            await device.prep()
            await asyncio.sleep(1)
            if x.isdigit():
                print("speed:",x)
                await device.send_command("SPEED", x)
            else:
                x=x.upper()
                if  x in constants.SOUND.keys():
                    print("sound:",x)
                    await device.send_command("SOUND", x)
                elif  x in constants.COLOR.keys():
                    print("color:",x)
                    await device.send_command("LIGHT",x)
                elif x=="OUT":
                    device.disconnect()
                else: print("Invalid input")
    except Exception as e:
        print(e)
    
asyncio.run(main())