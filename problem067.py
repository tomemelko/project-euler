triangle = open('p67tri.txt', 'r').read()
tri = [[int(j) for j in i.split(' ')] for i in triangle.split(':')]
while (len(tri) > 1):
  bot_row = tri[-1]
  for i in xrange(len(tri)-1):
    tri[-2][i] += max(bot_row[i:i+2])
  del tri[-1]

print tri[0][0]
