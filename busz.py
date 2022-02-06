i = 0
k = 0
while i < 10:
  i += 1
  if i < 8:
      k += 1
      print(i,'. működik, sofőrre vár')
  if i > 7:
      print(i,'. nem működik, szervízre vár')
print('Működik:',k,'db busz. Nem működik:',i-k,'db busz')
a = input('vége, nyomj ENTER-t')
