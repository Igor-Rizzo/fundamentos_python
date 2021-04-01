#Gerar valores com random
import random


#DESAFIO: Você quer simular a opção de jogar uma moeda e resultar em cara ou coroa. Jogue as opções dentro de uma lista e depois crie um programa que imprima 'cara' ou 'coroa'

cara_ou_coroa = ['Cara', 'Coroa']
print(random.choice(cara_ou_coroa))

""" Desafio 2: Você quer simular um sorteio dentre 5 nomes um uma lista de nomes.
Crie uma lista de 5 nomes e sorteie um nome de dentro desta lista e exiba na tela """

lista_de_cinco_nomes = ["Maria Gorete", "Adão", "Ana Paula", "Franciéli", "Maria Helena"]
print(random.choice(lista_de_cinco_nomes))


##Escolher aleatóriamente um número de 10 - 100
#Imprima um valor aleatório entre 10 e 100

print(random.randint(10, 100))