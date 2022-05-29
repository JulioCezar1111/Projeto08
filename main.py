# instalar pandas openpyxl, twilio (acesso ao excel e SMS)
#bibliotecas
import pandas as pd
from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "AC613c0e25c1c31672e874b70843375190"
# Your Auth Token from twilio.com/console
auth_token = "1db70e8c3fafb5e9c55dbe9282b6e7b9"
client = Client(account_sid, auth_token)

#  Passo a passo de solução

# Abrir os 6 arquivos em excel
lista_meses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho']

for mes in lista_meses:
    tabela_vendas = pd.read_excel(f'{mes}.xlsx')

    # Para cada arquivo verificar se é maior que R$ 55000
    if (tabela_vendas['Vendas'] > 55000).any():
        vendedor = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000, 'Vendedor'].values[0] #loc[linha, coluna]; values[0] da somente o valor
        vendas = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000, 'Vendas'].values[0]
        print(f'No mês {mes} alguem bateu a meta. Vendedor: {vendedor}. Vendas: {vendas}')

        # Se for maior do que R$ 55000 -> enviar um SMS com o nome, o mes e as vendas do vendedor
        message = client.messages.create(
            to="+5511963479497",
            from_="+16073036247",
            body=f'No mês {mes} alguem bateu a meta. Vendedor: {vendedor}. Vendas: {vendas}')
        print(message.sid)

# Caso não seja maior do que R$ 55000 não quero fazer nada