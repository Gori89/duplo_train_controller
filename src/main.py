import asyncio
import device_aioble
import constants
import action
import time

from button import Button
from led import Led

async def main():
    print("Start main")
    device = device_aioble.DeviceBle()
    
    connection_led =Led(constants.PIN["CONN_LED"])

    connection_button = Button(constants.PIN["CONN_BUTTON"],action.connection, led=connection_led, device=device)
    ##test_button = Button(constants.PIN["CONN_BUTTON"],action.test, device=device)
    ##break_button = Button(constants.PIN["BREAK_BUTTON"], action.brake)
    ##station_button = Button(constants.PIN["STATION_BUTTON"], action.depart)
    ##water_button = Button(constants.PIN["WATER_BUTTON"], action.water)
    ##horn_button = Button(constants.PIN["HORN"], action.horn)
    ##depart_button = Button(constants.PIN["DEPART_BUTTON"], action.depart)
    ##light_button = Button(constants.PIN["LIGHT_BUTTON"], action.light_switch)

    while True:
        print("----------------")
        start=time.ticks_ms()
        await connection_button.check_status()

        time.sleep(0.1-min(time.ticks_diff(time.ticks_ms(),start),0.09))
asyncio.run(main())