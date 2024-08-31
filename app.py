def encriptar(txt, deslocamento):
    resultado = ''
    for char in txt:
        if char.isupper():
            resultado += chr((ord(char) - ord('A') + deslocamento) % 26 + ord('A'))
        elif char.islower():
            resultado += chr((ord(char) - ord('a') + deslocamento) % 26 + ord('a'))
        else:
            resultado += char
    return resultado

def desencriptar(txt, deslocamento):
    resultado = ''
    for char in txt:
        if char.isupper():
            resultado += chr((ord(char) - ord('A') - deslocamento) % 26 + ord('A'))
        elif char.islower():
            resultado += chr((ord(char) - ord('a') - deslocamento) % 26 + ord('a'))
        else:
            resultado += char
    return resultado

#def salvar_em_arquivo(texto_encriptado, deslocamento, db):
#    with open(db, 'a') as arquivo:
#        arquivo.write(f"Deslocamento: {deslocamento}\n")
#        arquivo.write(f"Texto encriptado: {texto_encriptado}\n")
#        arquivo.write("\n")

print ("MENU:")
print ("1 - encriptar")
print ("2 - desencriptar")

op = True
while op == True:
    opcao = int(input("Qual a opção desejada? "))
    if opcao < 1 or opcao > 2:
        print("Valor Invalido. Insira o número 1 ou 2")
    else:
        op = False

txt = str(input("Qual o texto? "))
controle = True

while controle == True:
    deslocamento = int(input("Qual o valor do deslocamento? "))
    if deslocamento < 1 or deslocamento > 25:
        print ("Valor Invalido. Insira um número entre 1 e 25.")
    else:
        controle = False

if opcao == 1:
    texto_encriptado = encriptar(txt, deslocamento)
    print("O texto encriptado é: ", texto_encriptado)

if opcao == 2:
    texto_desencriptado = desencriptar(txt, deslocamento)
    print("O texto original é: ", texto_desencriptado)