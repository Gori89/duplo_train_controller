##https://getwavecake.com/blog/getting-started-with-bluetooth-and-python-part-2/
import asyncio
import constants as const
import uuid
from bleak import BleakScanner, BleakClient


class DeviceBle():
    
    def __init__(self):
        self.client = None
        uuid = uuid.UUID(const.UUID)

    async def discover(self):
        devices = await BleakScanner.discover(const.BT_DISCOVERY_TIME, return_adv=True)
        for device in devices:
            advertisement_data = devices[device][1]
            if(advertisement_data.local_name == const.MODEL_NAME):
                print(advertisement_data)
                self.device = devices[device]
                return device
    
    async def connect(self):
        address = await self.discover()
        if address is not None:
            try:
                print("Found device at address: %s" % (address))
                print("Attempting to connect...")
                self.client = BleakClient(address)
                await self.client.connect()
                print("Connected")
            except:
                raise Exception("Failed to connect")
        else:
            raise Exception("Did not find available devices")
    
    async def disconnect(self):
        try:
            print("Disconnecting...")
            await self.client.disconnect()
            print("Disconnected!")
        except:
            raise Exception("Warning: Failed to disconnect. Check for hanging connection")



    async def send_command(self, type, value):

        match type.upper():
            case const.COMMAND_TYPE.SPEED:
                await self._run(value)
            case const.COMMAND_TYPE.SPEED:
                await self._sound(value)
            case const.COMMAND_TYPE.SPEED:
                await self._light(value)
            case _:
                print("Invalid type")
    
    async def send_message(self,  messeage):
        await self.client.write_gatt_char(self.uuid, bytearray(messeage))
        print ("Message sended")

    async def _prep(self):
        messeage = [0x0A, 0x00, 0x41, 0x01, 0x01, 0x01, 0x00, 0x00, 0x00, 0x01]
        await self.send_message(messeage)

    async def _run(self, speed):
        ##speed=max(min(const.MAX_SPEED, int(speed)), const.MIN_SPEED)
        messeage = bytearray([0x08, 0x00, 0x81, 0x00, 0x01, 0x51, 0x00, int(speed)])
        await self.send_message(messeage)

    async def _sound(self, uuid, sound):
        messeage =  bytearray([0x08, 0x00, 0x81, 0x01, 0x11, 0x51, 0x01, const.SOUND.get(sound)])
        await self.send_message(messeage)

    async def _light(self, color):
        messeage = bytearray([0x08, 0x00, 0x81, 0x11, 0x11, 0x51, 0x00, const.COLOR.get(color)])
        await self.send_message(uuid, messeage)