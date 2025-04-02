from machine import ADC


class Potentiometer(ADC):

    def __init__(self, id, action, device=None):
        super().__init__(id)
        self.action=action
        self.device=device
        self.last_speed=0

    async def check_status(self):
        speed=_adjust_values(self.read_u16())
        if speed!=self.last_speed:
            await self.action(self.device, speed)
            self.last_speed=speed
    
def _adjust_values(input_value):

    speed_list=[-100, -80, -60, -40, 0, 40, 60, 80, 100]
    index=int(round(input_value/65535*(len(speed_list)-1)))
    return speed_list[max(0, min(index, len(speed_list)-1))]
