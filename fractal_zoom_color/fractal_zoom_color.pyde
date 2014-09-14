def drawSquareTop(a, b, ll, n):
  x = a + (ll / 2)
  y = b - ll
  noStroke()
  fill(100-(abs(log(ll)/log(2) - n - 1)/(log(origin)/log(2)))*93,
       100-((log(ll)/log(2))/(log(origin)/log(2)))*70,
       100,
       30+((log(ll)/log(2))/(log(origin)/log(2)))*70)
  rect(x, y, ll, ll)
  return [x, y]

def drawSquareBottom(a, b, ll, n):
  x = a + (ll / 2)
  y = b + (ll * 2)
  noStroke()
  fill(100-(abs(log(ll)/log(2) - n - 1)/(log(origin)/log(2)))*93,
       100-((log(ll)/log(2))/(log(origin)/log(2)))*70,
       100,
       30+((log(ll)/log(2))/(log(origin)/log(2)))*70)
  rect(x, y, ll, ll)
  return [x, y]

def drawSquareRight(a, b, ll, n):
  x = a + (ll * 2)
  y = b + (ll / 2)
  noStroke()
  fill(100-(abs(log(ll)/log(2) - n - 1)/(log(origin)/log(2)))*93,
       100-((log(ll)/log(2))/(log(origin)/log(2)))*70,
       100,
       30+((log(ll)/log(2))/(log(origin)/log(2)))*70)
  rect(x, y, ll, ll)
  return [x, y]

def drawSquareLeft(a, b, ll, n):
  x = a - ll
  y = b + (ll / 2)
  noStroke()
  fill(100-(abs(log(ll)/log(2) - n - 1)/(log(origin)/log(2)))*93,
       100-((log(ll)/log(2))/(log(origin)/log(2)))*70,
       100,
       30+((log(ll)/log(2))/(log(origin)/log(2)))*70)
  rect(x, y, ll, ll)
  return [x, y]

def drawFourSquares(x, y, l, count):
  l = l / 2
  sTop = drawSquareTop(x, y, l, count)
  sBottom = drawSquareBottom(x, y, l, count)
  sRight = drawSquareRight(x, y, l, count)
  sLeft = drawSquareLeft(x, y, l, count)
  if l > 3:
    drawFourSquares(sTop[0], sTop[1], l, count)
    drawFourSquares(sBottom[0], sBottom[1], l, count)
    drawFourSquares(sRight[0], sRight[1], l, count)
    drawFourSquares(sLeft[0], sLeft[1], l, count)

origin = 256

def setup():
  size(origin * 3, origin * 3)
  colorMode(HSB, 100, 100, 100, 100)
  noLoop()

def draw():
  count = frameCount % (log(origin)/log(2))
  background(0, 0, 100)
  noStroke()
  fill(100-(abs(log(origin)/log(2) - count - 1)/(log(origin)/log(2)))*93,
       100-((log(origin)/log(2))/(log(origin)/log(2)))*70,
       100,
       30+((log(origin)/log(2))/(log(origin)/log(2)))*70)
  rect(256, 256, origin, origin)
  drawFourSquares(256, 256, origin, count)
  origin *= 1.01

def mousePressed():
  loop()

def mouseReleased():
  noLoop()
