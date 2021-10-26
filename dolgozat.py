#Írj egy Python programot,amely bekér egy dolgozat pontszámot(x)a felhasználótól és kiír egy érdemjegyet az alábbi szerint! 1:x<50; 2: 50<=x<60; 3: 60<=x<70; 4: 70<=x<85; 5: x>=85.

szam1=int(input('Mennyi pontot szereztél?'))
if szam1<50:
  print('Az érdemjegyed 1-es')
elif 50<=szam1<60:
  print('Az érdemjegyed 2-es')
elif 60<=szam1<70:
  print('Az érdemjegyed 3-as')
elif 70<=szam1<85:
  print('Az érdemjegyed 4-es')
elif 85<=szam1<100:
  print('Az érdemjegyed 5-ös')
