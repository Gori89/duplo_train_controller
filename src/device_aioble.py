##https://getwavecake.com/blog/getting-started-with-bluetooth-and-python-part-2/
import constants as const
import aioble
from bluetooth import UUID


class DeviceBle():

    async def connect(self):
        async with aioble.scan(duration_ms=const.BT_DISCOVERY_TIME_MS, interval_us=30000, window_us=30000, active=True) as scanner:
            async for result in scanner:
                if result.name() and const.MODEL_NAME in result.name():
                    print(f"Found device: {result.name()}")
                    self.device=result.device
                    break
            else:
                print(f"No {const.MODEL_NAME} found.") 
                self.device = None
        if self.device:
            try:
                self.conn=await self.device.connect(timeout_ms=2000)
                print("Connected")
            except Exception as e:
                print("Connection failed:", e)
                self.conn = None
                
        if self.conn:   
            try:
                print("Conn:",self.conn)
                self.service = await self.conn.service(UUID(const.LWP_SERVICE_UUID))
                self.char = await self.service.characteristic(UUID(const.LWP_CHAR_UUID))
                print(self.char)
            except Exception as e:
                print("Failed to discover service/char:", e)
        else:
            print("Connection faild")

    
    async def disconnect(self):
        try:
            if self.conn:
                print("Disconnecting...")
                await self.conn.disconnect()
                print("Disconnected!")
        except:
            raise Exception("Warning: Failed to disconnect. Check for hanging connection")



    async def send_command(self, type, value):

        if type.lower()==const.COMMAND_TYPE["SPEED"]:
                await self._run(int(value))
        elif type.lower()==const.COMMAND_TYPE["SOUND"]:
                await self._sound(value.upper())
        elif type.lower()==const.COMMAND_TYPE["LIGHT"]:
                await self._light(value.upper())
        else:
                print("Invalid type")
    
    async def prep(self):
        messeage = bytes([0x0A, 0x00, 0x41, 0x01, 0x01, 0x01, 0x00, 0x00, 0x00, 0x01])
        await self.char.write(messeage)

    async def _run(self, speed):
        speed=self._speed_limit(speed)
        print(speed)
        messeage = bytes([0x08, 0x00, 0x81, 0x00, 0x01, 0x51, 0x00, int(speed)])
        await self.char.write(messeage)

    async def _sound(self, sound):
        print("Sound:", sound)
        messeage =  bytes([0x08, 0x00, 0x81, 0x01, 0x11, 0x51, 0x01, const.SOUND[sound]])
        await self.char.write(messeage)
    
    async def _light(self, color):
        print("Light:",color)
        messeage = bytes([0x08, 0x00, 0x81, 0x11, 0x11, 0x51, 0x00, const.COLOR[color]])
        await self.char.write(messeage)
    
    def _speed_limit(self, speed):
        if speed>=0:
            x=min(100,speed)
        else:
            x=256+max(-100,speed)
        return x