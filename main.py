# Main app

# Temperature control application
# Written for use with Libre Computers Titanium H3 with Waveshare35B SPI screen
# Probes and displays the temperature of the surounding area.
# Uses 2 thermistors and controls a output gpio for use with a relay etc to drive fans etc.

# Colors:
# Primary: #F73D93
# Secondary: #16003B
# Background: #413F42
# BG Secondary: #7F8487

#Written by Bryce Standley - 2023


# Imports
from guizero import *

from utils import *

from tempSensor import *

triggerTemp = 30
outputStatus = 0;

app = App(title = "Temperature Control", bg = "#413F42")
app.set_full_screen()

containerBox = Box(app, align = "top", width = "fill", height = "fill")
probeStats = Text(containerBox, text="", color = "#ffffff")

def readTemp():
    temp = sensorRead()
    global outputStatus
    if temp >= triggerTemp and outputStatus == 0:
        setOutput(True)
        outputStatus = 1
    elif temp < triggerTemp  and outputStatus == 1:
        setOutput(False)
        outputStatus = 0
        
    text = "P1: " + str(temp) + "c \nTarget: 30c"
    probeStats.value = text

sensorSetup()
app.repeat(500, readTemp)
    

app.display()