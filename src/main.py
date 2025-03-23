import asyncio
import device_ble
import uuid
import constants

UUID= uuid.UUID('00001624-1212-efde-1623-785feabcd123')

##PREP_COMMAND= bytearray([0x0A, 0x00, 0x41, 0x01, 0x01, 0x01, 0x00, 0x00, 0x00, 0x01])
##START_COMMAND= bytearray([0x08, 0x00, 0x81, 0x00, 0x01, 0x51, 0x00, 0x9C])

async def main():
    device = device_ble.DeviceBle()
    try: 
        await device.connect()

        while True:
            print('Enter comand (speed int, sound or color):')
            x = input()
            await device.prep(UUID)
            await asyncio.sleep(1)
            if x.isdigit():
                print("speed:",x)
                await device.run(UUID,x)
            else:
                x=x.upper()
                if  x in constants.SOUND.keys():
                    print("sound:",x)
                    await device.sound(UUID, x)
                elif  x in constants.COLOR.keys():
                    print("color:",x)
                    await device.light(UUID,x)
                else: print("Invalid input")

        await device.disconnect()
    except Exception as e:
        print(e)
    
asyncio.run(main())