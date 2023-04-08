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
from titanium import *


app = App(title = "Temperature Control", bg = "#413F42", width = "480", height = "320")

containerBox = Box(app, align = "top", width = "fill", height = "fill")

if NetworkUp():
    weatherTemp = asyncio.run(GetWeatherTemp())
    weatherText = "Local Temp: " + str(weatherTemp) + "c"
    wt = Text(containerBox, weatherText, color = "#ffffff")
else :
    wt = Text(containerBox, "Network Error", color = "#ffffff")

SetupGPIO()


probeStats = Text(containerBox, text="P1: 35c \nTarget: 30c", color = "#ffffff")

app.display()