import keyboard
from Utils.Offsets import *
from Settings import *


def shootTrigger(pm, CrossID, client, lTeam, CTeam):
    if keyboard.is_pressed(triggerkey) and 0 < CrossID < 64 and lTeam != CTeam:
        pm.write_int(client + dwForceAttack, 6)