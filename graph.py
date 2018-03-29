import scrollphathd as sphd

def draw(history):
  segment = history[-8:]
#  high = max(history)
  print(segment)
  sphd.set_pixel(0, 0, 0.25)
