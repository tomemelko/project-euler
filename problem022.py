names = open('p22names.txt' , 'r').read().replace('"', '').split(',')
names.sort()
sum = 0
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
for n, i in enumerate(names):
  namescore = 0
  for letter in i:
    namescore += alphabet.index(letter) + 1
  sum += (n + 1) * namescore
print sum
