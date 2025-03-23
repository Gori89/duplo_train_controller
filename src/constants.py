from enum import Enum, StrEnum

MODEL_NAME= "Train Base"

MANUFACTOR_ID = 32

MAX_SPEED = 100
MIN_SPEED = -100

UUID = '00001624-1212-efde-1623-785feabcd123'

BT_DISCOVERY_TIME = 5

class COMMAND_TYPE(StrEnum):
    SPEED= "speed"
    SOUND= "sound"
    LIGHT= "light"

SOUND = { 
    "BRAKE" : 0x03,
    "STATION" : 0x05,
    "WATER" : 0x07,
    "HORN" : 0x09,
    "DEPART" : 0x0A,
}

COLOR = {
    "OFF" : 0x00,
    "PINK" : 0x01,
    "PURPLE" : 0x02,
    "BLUE" : 0x03,
    "LIGHT_BLUE" : 0x04,
    "TEAL" : 0x05,
    "GREEN" : 0x06,
    "YELLOW" : 0x07,
    "ORANGE" : 0x08,
    "RED" : 0x09,
    "WHITE" : 0x0A,

}







