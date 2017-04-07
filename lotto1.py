import random
szamok=[]
while len(szamok)<5:
	kihuzott=random.randrange(1,91)
	if kihuzott not in szamok: szamok.append(kihuzott)
szamok.sort()
print(szamok)

