import time
import typography
import scrollphathd as sphd
from envirophat import light, motion, weather, leds

# Log values

def log(temp,press) :
    out = open('enviro.log', 'w')
    s = "%s | %s" % (temp,press)
    print(s)
    out.write(s)

def draw(t,p) :
    t_str = round(t, 3)
    sphd.clear()
    typography.write("%s" % (t_str))
    sphd.show()

def update() :
    t = weather.temperature()
    p = weather.pressure()
    log(t,p)
    draw(t,p)

# Run
try:
    while True:
        update()
        time.sleep(1)
except KeyboardInterrupt:
    leds.off()
    out.close()
