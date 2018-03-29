import scrollphathd as sphd
import time
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

def update() : 
    print "working"
    lux = light.light()
    leds.on()
    rgb = str(light.rgb())[1:-1].replace(' ', '')
    leds.off()
    log(weather.temperature(),weather.pressure())
    sphd.clear()
    sphd.set_pixel(0, 0, 0.25)
    sphd.show()

# Run
try:
    while True:
        update()
        time.sleep(1)
except KeyboardInterrupt:
    leds.off()
    out.close()
