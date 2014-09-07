origin = 256
size(origin * 3, origin * 3)
background(255)
colorMode(HSB, 100, 100, 100, 100)

def drawSquareTop(a, b, ll):
  x = a + (ll / 2)
  y = b - ll
  noStroke()
  fill(100-((log(ll)/log(2))/8)*93,
       100-((log(ll)/log(2))/8)*70,
       100,
       30+((log(ll)/log(2))/8)*70)
  rect(x, y, ll, ll)
  return [x, y]

def drawSquareBottom(a, b, ll):
  x = a + (ll / 2)
  y = b + (ll * 2)
  noStroke()
  fill(100-((log(ll)/log(2))/8)*93,
       100-((log(ll)/log(2))/8)*70,
       100,
       30+((log(ll)/log(2))/8)*70)
  rect(x, y, ll, ll)
  return [x, y]

def drawSquareRight(a, b, ll):
  x = a + (ll * 2)
  y = b + (ll / 2)
  noStroke()
  fill(100-((log(ll)/log(2))/8)*93,
       100-((log(ll)/log(2))/8)*70,
       100,
       30+((log(ll)/log(2))/8)*70)
  rect(x, y, ll, ll)
  return [x, y]

def drawSquareLeft(a, b, ll):
  x = a - ll
  y = b + (ll / 2)
  noStroke()
  fill(100-((log(ll)/log(2))/8)*93,
       100-((log(ll)/log(2))/8)*70,
       100,
       30+((log(ll)/log(2))/8)*70)
  rect(x, y, ll, ll)
  return [x, y]

def drawFourSquares(x, y, l):
  l = l / 2
  sTop = drawSquareTop(x, y, l)
  sBottom = drawSquareBottom(x, y, l)
  sRight = drawSquareRight(x, y, l)
  sLeft = drawSquareLeft(x, y, l)
  if l >= 1:
    drawFourSquares(sTop[0], sTop[1], l)
    drawFourSquares(sBottom[0], sBottom[1], l)
    drawFourSquares(sRight[0], sRight[1], l)
    drawFourSquares(sLeft[0], sLeft[1], l)

noStroke()
fill(7, 30, 100, 100)
rect(origin, origin, origin, origin)
drawFourSquares(origin, origin, origin)
