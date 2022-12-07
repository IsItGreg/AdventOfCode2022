with open('inputs/12-3.txt', 'r') as f:
  lines = f.readlines()


def getValue(c):
  cnum = ord(c)
  anum, Anum = ord('a'), ord('A')
  if cnum - anum >= 0:
    return cnum - anum + 1
  else:
    return cnum - Anum + 27


shared = []
for line in lines:
  line = line.strip()
  middle = len(line) // 2
  l = line[:middle]
  r = line[middle:]

  lset, rset = set(), set()
  lset.update(list(l))
  rset.update(list(r))

  shared.extend(list(lset.intersection(rset)))

print(shared)
shared = list(map(getValue, shared))
print(shared)
print(sum(shared))


shared = []
for i in range(0, len(lines), 3):
  line1 = lines[i].strip()
  line2 = lines[i + 1].strip()
  line3 = lines[i + 2].strip()

  l1set, l2set, l3set = set(), set(), set()
  l1set.update(list(line1))
  l2set.update(list(line2))
  l3set.update(list(line3))

  shared.extend(list(l1set.intersection(l2set, l3set)))

print(shared)
shared = list(map(getValue, shared))
print(shared)
print(sum(shared))
