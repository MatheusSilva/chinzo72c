#implementação cifra de césar e outras funcionalidades
#testado em Python 2.7

def criptografarCifraCesar(text, key): #criptografa cifra de cesar
	text_list = list(text)
	text_encrypt = ""
	for i in text_list:
		# check if char is a letter
		if (i >= 'a' and i <= 'z') or (i >= 'A' and i <= 'Z'):
			if (i >= 'a' and i <= 'z'):
				ord_c = (ord(i) - ord('a') + key) % 26
				text_encrypt += chr(ord_c + ord('a'))
			else:
				ord_c = (ord(i) - ord('A') + key) % 26
				text_encrypt += chr(ord_c + ord('A'))
		else:
			text_encrypt += i
	return text_encrypt
 
def descriptografarCifraCesar(text, key):#descriptografa cifra de cesar
	text_list = list(text)
	text_encrypt = ""
	for i in text_list:
		if (i >= 'a' and i <= 'z') or (i >= 'A' and i <= 'Z'):
			if (i >= 'a' and i <= 'z'):
				ord_c = (ord(i) - ord('a') - key) % 26
				text_encrypt += chr(ord_c + ord('a'))
			else:
				ord_c = (ord(i) - ord('A') - key) % 26
				text_encrypt += chr(ord_c + ord('A'))
		else:
			text_encrypt += i
	return text_encrypt

def revertePalavras(text):#inverte apenas as palavras 
        return text[::-1]

def converteTextoParaBinario(text):#converte texto para binario
	return "".join(format(ord(x), 'b') for x in text)    

def converteTextoParaOctal(text):#converte texto para octal
	return "".join([oct(ord(letter)) for letter in text])	

def converteTextoParaHexadecimal(text):#converte texto para hexadecimal
	return "".join("{:02x}".format(ord(c)) for c in text)       	    


mensagem = raw_input("Insira o texto a ser encriptado em cifra de cesar: ")
casasdeslocamento = int(raw_input("Insira um numero de quantas casas quer deslocar para direita: "))
#print "você digitou", mensagem

#mensagem = "um texto qualquer a se encriptado"
#casasdeslocamento = 3

encriptado = criptografarCifraCesar(mensagem, casasdeslocamento)
decriptado = descriptografarCifraCesar(encriptado, casasdeslocamento)
revertido = revertePalavras(encriptado)
convertidohex = converteTextoParaHexadecimal(revertido)
convertidobin = converteTextoParaBinario(revertido)
convertidooct = converteTextoParaOctal(revertido)

print "encriptado", encriptado
print "decriptado", decriptado
print "encriptado com texto ao contrario", revertido
print "encriptado com texto ao contrario convertido para hexadecimal", convertidohex
print "encriptado com texto ao contrario convertido para binario", convertidobin
print "encriptado com texto ao contrario convertido para octal", convertidooct
