MODEL_NAME= "Train Base"

MANUFACTOR_ID = 32

MAX_SPEED = 100
MIN_SPEED = -100

LWP_SERVICE_UUID = "00001623-1212-efde-1623-785feabcd123"
LWP_CHAR_UUID = "00001624-1212-efde-1623-785feabcd123"


BT_DISCOVERY_TIME_MS = 5000

COMMAND_TYPE = { 
    "SPEED" : "speed",
    "SOUND" : "sound",
    "LIGHT" : "light"
}

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

PIN = {
    "CONN_LED": 14,
    "CONN_BUTTON": 15,
    "BRAKE_BUTTON" : 2,
    "STATION_BUTTON" : 3,
    "WATER_BUTTON" : 4,
    "HORN_BUTTON" : 5,
    "DEPART_BUTTON" : 6,
    "LIGHT_BUTTON" : 7

}







