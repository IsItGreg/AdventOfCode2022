with open('inputs/12-2.txt', 'r') as f:
  lines = f.readlines()


def rps(l, r):
  game = l - r
  if game == 0:
    return 3
  elif game == 1 or game == -2:
    return 0
  else:
    return 6


def letToNum(c):
  if c == 'A' or c == 'X':
    return 1
  elif c == 'B' or c == 'Y':
    return 2
  elif c == 'C' or c == 'Z':
    return 3


score = 0
for line in lines:
  l = line[0]
  r = line[2]

  l = letToNum(l)
  r = letToNum(r)

  score += rps(l, r)
  score += r

print(score)


def spr(l, R):
  if R == 'X':
    return (l - 1 - 1) % 3 + 1
  elif R == 'Y':
    return l
  elif R == 'Z':
    return (l - 1 + 1) % 3 + 1


score = 0
for line in lines:
  l = line[0]
  r = line[2]

  l = letToNum(l)
  r = spr(l, r)

  score += rps(l, r)
  score += r

print(score)
