nome_curso = 'Edição de vídeo'
#Para debbugar o cófigo e entender linha por linha:
#F9 e depois F5(escolher opção python file) e F10 para exibir o resultado

#Deixa string maiúscula
print(nome_curso.upper())
#Deixa tudo em minusculo
print(nome_curso.lower())
#Remover espaços em branco
print(nome_curso.strip())
#Remover espaços em branco da esquerda 
print(nome_curso.lstrip())
#Remover espaços em branco da direita 
print(nome_curso.rstrip())
#Encontrar os indices ou seja nesse caso o ç começa no indice 3 (Lembrando que o indice começa com indice zero)
print(nome_curso.find('ção'))
#Substituir a primeira palavra que eu passar com a segunda palavra
print(nome_curso.replace('vídeo', 'Música'))
print('http://sc.olx.com.br/?o=90&q=relogio'.replace('relogio', 'carro'))