from math import sqrt
def distance(x1, y1, x2, y2):
  #x = x2 - x1
 # y = y2 - y1
  distance = sqrt(((x2 - x1) ** 2) + ((y2 - y1) ** 2))
  return float(('{:.2f}'.format(distance)))

print(distance(1,1,0,0))