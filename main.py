#criando um sistema de agendamento de consulta basico

agendamento = []

def agendarConsulta():
  nome = input('Qual o seu nome? ')
  idade = input('Quantos anos você tem? ')
  especialidades = ['Cardiologista', 'Dermatologista', 'Oftalmologista', 'Nutricionista', 'Ortopedista']
  print('Escolha uma das especialidades abaixo:')
  for index, especialidade in enumerate(especialidades):
    print(f'{index + 1}. {especialidade}')

  while True:
    try:
      escolha = int(input('Digite o número da especialidade desejada: '))
      if escolha < 1 or escolha > len(especialidades):
        print('Opção inválida. Por favor, escolha uma opção válida.')
      else:
        break
    except ValueError:
      print('Opção inválida. Por favor, digite um número válido.')

  especialidade_escolhida = especialidades[escolha - 1]
  data = input('Digite a data da consulta (DD/MM): ')
  disponibilidades = [16, 17, 18]
  print('Escolha uma das disponibilidades abaixo:')
  for index, disponibilidade in enumerate(disponibilidades):
    print(f'{index + 1}. {disponibilidade} horas')

  while True:
    try:
      escolha = int(input('Digite o número da disponibilidade desejada: '))
      if escolha < 1 or escolha > len(disponibilidades):
        print('Opção inválida. Por favor, escolha uma opção válida.')
      else:
        break
    except ValueError:
      print('Opção inválida. Por favor, digite um número válido.')

  disponibilidade_escolhida = disponibilidades[escolha - 1]

  conclusao = input('Você deseja confirmar o agendamento? (S/N) ')
  if conclusao.upper() == 'S':
    dados = {
      'nome': nome,
      'idade': idade,
      'especialidade': especialidade_escolhida,
      'data': data,
      'horario marcado': disponibilidade_escolhida
    }
    agendamento.append(dados)
    print('Consulta agendada com sucesso!')
    print(agendamento)

agendarConsulta()