import scrollphathd as sphd

def draw(history):
  if len(history) < 5 : return
  segments = history[-17:]
  high = max(history[-60:])
  low = min(history[-60:])
  range = high-low
  for i,v in enumerate(segments):
    y = (v-low)/range
    sphd.set_pixel(i, 6-int(y*6), 0.25)
