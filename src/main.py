import asyncio
import device_aioble
import constants
import action
import time

from button import Button
from led import Led
from potentiometer import Potentiometer
async def main():
    print("Start main")
    device = device_aioble.DeviceBle()
    
    connection_led =Led(constants.PIN["CONN_LED"])

    accelerator_pot = Potentiometer(constants.PIN["ACCELERATOR_POT"], action.speed, device=device)

    connection_button = Button(constants.PIN["CONN_BUTTON"],action.connection, led=connection_led, device=device)
    break_button = Button(constants.PIN["BRAKE_BUTTON"], action.brake, device=device)
    station_button = Button(constants.PIN["STATION_BUTTON"], action.depart, device=device)
    water_button = Button(constants.PIN["WATER_BUTTON"], action.water, device=device)
    horn_button = Button(constants.PIN["HORN_BUTTON"], action.horn, device=device)
    depart_button = Button(constants.PIN["DEPART_BUTTON"], action.depart, device=device)
    ##light_button = Button(constants.PIN["LIGHT_BUTTON"], action.light_switch)

    while True:
        start=time.ticks_ms()
        await connection_button.check_status()
        await accelerator_pot.check_status()
        await break_button.check_status()
        await station_button.check_status()
        await water_button.check_status()
        await horn_button.check_status()
        await depart_button.check_status()

        time.sleep(0.1-min(time.ticks_diff(time.ticks_ms(),start),0.09))
asyncio.run(main())