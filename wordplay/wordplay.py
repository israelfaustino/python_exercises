#!/usr/bin/python3
import random

# variaveis
vog = 'aeiou'			# vogais
con = 'tpdfkvbnm'		# consoantes
sil = []				# silabas
qtd_sil = 3				# qtd de silabas
qtd_com = 10			# qtd de combinacoes

# concatena silabas com base nas consoantes e vogais
for i in vog:
	for j in con:
		sil.append(j+i)

random.seed()

for j in range(qtd_com):
	for i in range(qtd_sil):
		pos = random.randint(0,len(sil)-1)
		print(sil[pos],end='')
	print('')

