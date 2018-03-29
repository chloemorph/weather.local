import time
import typography
import graph
import scrollphathd as sphd
from envirophat import light, motion, weather, leds

# History

history = {'temperature':[],'pressure':[]}

# Log values

def log(t,p) :
  out = open('enviro.log', 'w')
  s = "%s | %s" % (t,p)
  history['temperature'].append(t)
  history['pressure'].append(p)
#  out.write(s) # Recording..

def draw_typo(t,p) :
  t_str = round(t, 3)
  typography.write("%s" % (t_str))

def update() :
  sphd.clear()
  t = weather.temperature()
  p = weather.pressure()
  log(t,p)
  graph.draw(history['temperature'])
  sphd.show()

# Run
try:
  while True:
    update()
    time.sleep(0.25)
except KeyboardInterrupt:
  leds.off()

