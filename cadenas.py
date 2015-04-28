'''Ejercicio 6.8.1. Escribir funciones que dada una cadena de caracteres:

Imprima los dos primeros caracteres.
Imprima los tres últimos caracteres.
Imprima dicha cadena cada dos caracteres. Ej.: recta debería imprimir rca
Dicha cadena en sentido inverso. Ej.: hola mundo! debe imprimir !odnum aloh
Imprima la cadena en un sentido y en sentido inverso. Ej: reflejo imprime reflejoojelfer.'''

def twoChars(txt):
	return txt[:2]
def lastTreeChars(txt):
	return txt[-3:]
def oneInOne(txt):
	textTmp = ""
	for pos in range(0, len(txt), 2):
		textTmp += txt[pos]
	return textTmp
		
def reverseString(txt):
	textTemp = ""
	for i in range(len(txt)):
		textTemp += txt[-1]
		txt = txt[:-1]
	return textTemp
def reverseAndNot(txt):
	return "%s%s" % (txt, reverseString(txt))
	
cadena = "Hola Mundo!"
print("Cadena:"+cadena)
print(twoChars(cadena))
print(lastTreeChars(cadena))
print(oneInOne(cadena))
print(reverseString(cadena))
print(reverseAndNot(cadena))