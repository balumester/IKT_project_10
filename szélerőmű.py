i = 0
j = 0
k = 0
while i < 30:
  i += 1
  if i < 11:
      k += 1
      b = k*2000
      print(i,'-ik oszlop 2000-et termel')
  if i > 10 and i < 21:
      j += 1
      c = j*1000
      print(i,'-ik oszlop 1000-et termel')
  if i > 20:
      print(i,'-ik oszlop nem termel')
print('1-től',k,'-ik oszlopok termelése:', b)
print(k,'-től',k+j,'-ik oszlopok termelése:',c)
print('Teljes termelt áram:',b+c)
a = input('vége, nyomj ENTER-t')
