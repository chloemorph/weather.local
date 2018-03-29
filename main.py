import scrollphathd as sphd
import time
import typography

from envirophat import light, motion, weather, leds

print light.light()
print light.rgb()
print(weather.temperature())
print(weather.pressure())

# Log values

def log(temp,press) :
    out = open('enviro.log', 'w')
    s = "%s | %s" % (temp,press)
    out.write(s)

def draw(str) :
    typography.write(str)

def update() :
    lux = light.light()
    leds.on()
    rgb = str(light.rgb())[1:-1].replace(' ', '')
    leds.off()
    log(weather.temperature(),weather.pressure())
    sphd.clear()
    draw("+2-3")
    sphd.show()

# Run
try:
    while True:
        update()
        time.sleep(1)
except KeyboardInterrupt:
    leds.off()
    out.close()
