with open('inputs/12-1.txt', 'r') as f:
  lines = f.readlines()

  best = 0
  cur = 0
  for l in lines:
    if l != '\n':
      cur += int(l)
    else:
      if cur > best:
        best = cur
      cur = 0

  print(best)

  best = [0, 0, 0]

  cur = 0
  for l in lines:
    if l != '\n':
      cur += int(l)
    else:
      if cur > best[0]:
        best[0] = cur
        best = sorted(best)
      cur = 0

  print(best)
  print(best[0] + best[1] + best[2])
