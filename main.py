import time
import typography
import graph

import scrollphathd as sphd
from envirophat import light, motion, weather, leds

# History

history = {'temperature':[],'pressure':[]}

# Log values

def log(t,p) :
  s = "%s | %s" % (t,p)
  history['temperature'].append(t)
  history['pressure'].append(p)
#  out = open('enviro.log', 'w')
#  out.write(s) # Recording..

def update(timer) :
  sphd.clear()
  t = weather.temperature()
  p = weather.pressure()
  # Record
  if timer % 60 == 0 : log(t,p)
  # Draw
  if (timer/10) % 2 == 0 or len(history['temperature']) < 5 :
    s = round(t if (timer/5) % 2 == 0 else p,3)
    typography.write("%s" % s)
  else:
    graph.draw(history['temperature'])
  sphd.show()
  # Trim history
  history['temperature'] = history['temperature'][-60:]
  history['pressure'] = history['pressure'][-60:]

# Run
timer = 0
try:
  while True:
    update(timer)
    time.sleep(1)
    timer += 1
except KeyboardInterrupt:
  leds.off()

