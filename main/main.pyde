def drawSquareTop(a, b, ll, n):
  # draws square on top of origin square and returns coordinates
  # of the new square it drew
  x = a + (ll / 2)
  y = b - ll
  noStroke()
  # fill equations -- see below
  fill(100-(abs(log(ll)/log(2) - n - 1)/(log(origin)/log(2)))*93,
       100-((log(ll)/log(2))/(log(origin)/log(2)))*70,
       100,
       30+((log(ll)/log(2))/(log(origin)/log(2)))*70)
  rect(x, y, ll, ll)
  return [x, y]

def drawSquareBottom(a, b, ll, n):
  # draws square beneath origin square and returns coordinates
  # of the new square it drew
  x = a + (ll / 2)
  y = b + (ll * 2)
  noStroke()
  # fill equations -- see below
  fill(100-(abs(log(ll)/log(2) - n - 1)/(log(origin)/log(2)))*93,
       100-((log(ll)/log(2))/(log(origin)/log(2)))*70,
       100,
       30+((log(ll)/log(2))/(log(origin)/log(2)))*70)
  rect(x, y, ll, ll)
  return [x, y]

def drawSquareRight(a, b, ll, n):
  # draws square to the right of origin square and returns coordinates
  # of the new square it drew
  x = a + (ll * 2)
  y = b + (ll / 2)
  noStroke()
  # fill equations -- see below
  fill(100-(abs(log(ll)/log(2) - n - 1)/(log(origin)/log(2)))*93,
       100-((log(ll)/log(2))/(log(origin)/log(2)))*70,
       100,
       30+((log(ll)/log(2))/(log(origin)/log(2)))*70)
  rect(x, y, ll, ll)
  return [x, y]

def drawSquareLeft(a, b, ll, n):
  # draws square to the left of origin square and returns coordinates
  # of the new square it drew
  x = a - ll
  y = b + (ll / 2)
  noStroke()
  # fill equations -- see below
  fill(100-(abs(log(ll)/log(2) - n - 1)/(log(origin)/log(2)))*93,
       100-((log(ll)/log(2))/(log(origin)/log(2)))*70,
       100,
       30+((log(ll)/log(2))/(log(origin)/log(2)))*70)
  rect(x, y, ll, ll)
  return [x, y]

def drawFourSquares(x, y, l, count):
  # draws all four squares, then uses recursion to repeat the process
  # for each new square it draws

  # first set of four squares have side length 1/2 that of origin
  # square, so that variable is halved
  l = l / 2

  # call functions to draw all four squares
  sTop = drawSquareTop(x, y, l, count)
  sBottom = drawSquareBottom(x, y, l, count)
  sRight = drawSquareRight(x, y, l, count)
  sLeft = drawSquareLeft(x, y, l, count)

  # if length of square > 7 pixels, continue adding levels
  # also, if (x, y) coordinates of upper left corner of
  # origin square is outside a certain range, do not continue
  # adding squares to it
  if l > (origin/64 - 1) and x >= -1*(origin/2) and y >= -1*(origin/2) and x <= (origin*3.5) and y <= (origin*3.5):
    # draw four squares for the top square
    drawFourSquares(sTop[0], sTop[1], l, count)
    # draw four squares for the bottom square
    drawFourSquares(sBottom[0], sBottom[1], l, count)
    # draw four squares for the right square
    drawFourSquares(sRight[0], sRight[1], l, count)
    # draw four squares for the left square
    drawFourSquares(sLeft[0], sLeft[1], l, count)

# set first origin square at initial value of 256
origin = 256

def setup():
  # set size to 3 x origin square (this allows to whole 
  # initial shape to remain visible)
  size(origin * 3, origin * 3)
  # set color mode to RGB with value ranges of 0-100 for hue,
  # saturation, brightness, and opacity
  colorMode(HSB, 100, 100, 100, 100)

def draw():
  # make a variable "count" that loops from 1 to the number of
  # levels in the fractal (using frameCount)
  count = frameCount % (log(origin)/log(2))
  # set background to white
  background(0, 0, 100)
  # remove stroke
  noStroke()
  # use base-2 logarithms of square side lengths to create discrete
  # values for hue, saturation, and opacity, and change those values
  # in each successive level of the fractal and with frameCount
  fill(100-(abs(log(origin)/log(2) - count - 1)/(log(origin)/log(2)))*93,
       100-((log(origin)/log(2))/(log(origin)/log(2)))*70,
       100,
       30+((log(origin)/log(2))/(log(origin)/log(2)))*70)
  # draw the first square
  rect(256, 256, origin, origin)
  # draw four squares around the first square, four squares around
  # each of those squares, and on and on...
  drawFourSquares(256, 256, origin, count)
  # origin square width increases by up to 10% with each frame
  # when mouse is on the right side of the image, and decreases
  # by up to 10% with each frame when mouse is on the left side
  # NEW AND IMPROVED with mouseclick to switch zoom on and off
  if mouseX > (256*1.5) and mouseclick:
    origin *= 1 + (0.1)*((mouseX-256*1.5)/(256*1.5))
  elif mouseX < (256*1.5) and mouseclick:
    origin *= 1 - (0.1)*(abs(mouseX-256*1.5)/(256*1.5))
  else:
    pass

# set mouseclick variable to false
mouseclick = False

# standard switch function
def mouseClicked():
  if mouseclick:
    mouseclick = False
  else:
    mouseclick = True
    
