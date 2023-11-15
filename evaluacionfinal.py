#Nicolle Ruiz Quintero


#MENU

def menu():
    opcion = int(input("MENU\n==============\n1.CARACTER\n2.PALABRA\n==============\n"))

    if opcion == 1:
        caracter = input("COLOCA UN CARACTER: ")
        palabra = caracter
    elif opcion == 2:
        palabra = input("COLOCA UNA PALABRA: ")
    else:
        print("Opción no válida. Se usará una cadena vacía.")
        palabra = ""

    return palabra

#PASAR DE LETRA  O PALABRA A BINARIO

def letraabinario(letra):
    binario = bin(ord(letra))[2:].zfill(8)
    return binario


def palabraabinario(palabra):
  binariosletras = [(letra, letraabinario(letra), ord(letra))  for letra in palabra]
  binariopalabra = ''
  for letra, binario, _ in binariosletras:
      binariopalabra += binario
  return binariosletras, binariopalabra

#MAIN
usuario = menu()
binariosletras, binariopalabra = palabraabinario(usuario)

print("Palabra original:",usuario)
for letra, binario, asciinum in binariosletras:
  print(f"El valor del caracter {letra} en ASCII es: {asciinum}. Su representación binaria es: {binario}")
print("Binario de la palabra:", binariopalabra)
