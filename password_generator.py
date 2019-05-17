import random
import string
from random import choice
import os

def cria_senha():


	file = open('source_words\\palavras.txt')
	file2 = open('source_words\\symbols.txt')

	palavras = file.readlines()

	simbolos = file2.readlines()

	pass_word = ''

	for i in range(14):

		if i in(0,1,2):
			letra = pass_word.join(random.choice(string.ascii_letters).lower())

			while len(pass_word) < 3:
				if(letra not in pass_word):
					pass_word = pass_word + letra

				else:
					letra = pass_word.join(random.choice(string.ascii_letters).lower())

		
		if i in(3,4,5,6):
			pass_word = pass_word + pass_word.join(str(random.randint(0,9)))

		if i == 7:
			palavra = random.choice(palavras).lower().strip('\n')
			pass_word = pass_word + (''.join(choice((str.upper, str.lower))(c) for c in palavra))

		if i in(11,12):
			pass_word = pass_word + pass_word.join(str(random.randint(0,9)))

		if i == (13):
			pass_word = pass_word + random.choice(simbolos).strip('\n')

	return pass_word



def pega_valores(nro_senhas):
	senhas = []

	k = 1
	for filename in os.listdir('generated_passwords\\'):
		k = k + 1


	file = open('generated_passwords\\passwords_'+str(k)+'.txt','w')

	senha = cria_senha()
	i = 1

	while(len(senhas) < nro_senhas):

		if(senha not in senhas):
			senhas.append(senha)

			file.write(str(i) + ' - ' + senha + '\n\n')
			i = i + 1

		else:
			senha = cria_senha()


	return senhas




x = int(input('entre com o numero de senhas:  '))

passes = (pega_valores(x))

print(passes)