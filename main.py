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


app = App(title = "Temperature Control", bg = "#413F42", width = "480", height = "320")

containerBox = Box(app, align = "top", width = "fill", height = "fill")
probeStats = Text(containerBox, text="", color = "#ffffff")

def readTemp():
    temp = serialRead()
    text = "P1: " + str(temp) + "c \nTarget: 30c"
    probeStats.value = text

if serialSetUp():
    app.repeat(2000, readTemp)
    

app.display()