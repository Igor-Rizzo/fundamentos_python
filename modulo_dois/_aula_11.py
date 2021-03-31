#Trabalhando com Data
from datetime import datetime


print('Imprimir na tela a data completa')
print(datetime.now())
print('Imprimir na tela o dia')
print(datetime.now().day)
print('Imprimir na tela o mês ')
print(datetime.now().month)
print('imprimir na tela o ano ')
print(datetime.now().year)

#Criar uma data
lancamento_app = datetime(2021, 11, 23)
print('A data de lançamento do app é: ', lancamento_app)

#Agora quero receber a data de lançamento do meu app por um usuário
data_de_lancamento = datetime.strptime(input("Quando devemos lançar o aplicativo? "), '%d/%m/%Y')
print(data_de_lancamento)

#Calcular o intervalo de datas

data_atual = datetime.now()
prazo_de_entrega = data_de_lancamento - data_atual
print('O prazo para entrega do software é: ', prazo_de_entrega.days)

#DESAFIO
#Calcule quantos dias faltam até o meu aniversário

desafio_aniversario = datetime(2021, 11, 23)
dias_para_meu_aniversario = desafio_aniversario - datetime.now()
print(f'Faltam {dias_para_meu_aniversario} para o meu aniversário')
