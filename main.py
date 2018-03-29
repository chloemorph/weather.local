import scrollphathd as sphd
import time

from envirophat import weather,light,leds

print light.light()
print light.rgb()
print(weather.temperature())
print(weather.pressure())

while True:
    for x in range(17):
        sphd.clear()
        for y in range(7):
            sphd.set_pixel(x, y, 0.25)
        sphd.show()
        time.sleep(1/17.0)
