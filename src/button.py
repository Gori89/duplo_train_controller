from machine import Pin

class Button(Pin):

    was_pressed=False

    def __init__(self, id, action, device=None, led=None):
        super().__init__(id, Pin.IN, Pin.PULL_UP)
        self.action=action
        self.device=device
        self.led=led

    async def check_status(self):
        if self.value() == 0 and not self.was_pressed:
            if self.led:
                await self.action(self.device, self.led)
            else:
                await self.action(self.device)
            self._change_button_status(True)
        elif self.value() == 1:
            self._change_button_status(False)

    def _change_button_status(self, new_status):
        self.was_pressed= new_status


