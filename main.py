import os
import json

def carregar_tarefas():
    if os.path.exists('tarefas.json'):
        with open('tarefas.json', 'r', encoding='utf-8') as LDT:
            return json.load(LDT)
    return []

tarefas = carregar_tarefas()

def main():
    while True:
        mostrar_menu()
        escolha = input('Escolha uma opção: ')
        if escolha == '1':
            criar_tarefa()
        elif escolha == '2':
            remover_tarefas()
        elif escolha == '3':
            listar_tarefas()
        elif escolha == '4':
            alt_estado_tarefa()
        elif escolha == '5':
            limpar_tela()
            break
        else:
            print('Opção inválida')

def mostrar_menu():
    print('=======TaskMate=======')
    print('1. Criar uma tarefa.')
    print('2. Remover uma tarefa.')
    print('3. Listar tarefas.')
    print('4. Alternar estado de conclusão da tarefa.')
    print('5. Sair.\n')

def criar_tarefa():
    nome_da_tarefa = input('\nDigite o nome da sua tarefa: ')
    descricao_da_tarefa = input('\nDê uma descrição a sua tarefa: ')
    pi = pedir_data('prazo inicial')
    pf = pedir_data('prazo final')
    concluida = False
    status = 'Concluída.' if concluida == True else 'Não concluída.'
    
    tarefa = {
        'nome': nome_da_tarefa,
        'descrição': descricao_da_tarefa,
        'prazo inicial': pi,
        'prazo final': pf,
        'Status': status,
    }
    for item in tarefas:
        if item['nome'].lower() == nome_da_tarefa.lower():
            print(f'\nA tarefa {item['nome']} ja está cadastrada.')
            voltar()
            return 

    if not nome_da_tarefa:
        print('Insira pelo menos um nome válido para criar uma tarefa.')
        voltar()
    
    else:
        tarefas.append(tarefa)
        salvar_tarefas()
        print('\nTarefa criada com sucesso.')
        voltar()

def remover_tarefas():
    nome = input('Digite o nome da tarefa que você deseja remover: ')
    for item in tarefas:
        if item['nome'].lower() == nome.lower():
            tarefas.remove(item)
            salvar_tarefas()
            voltar()
            break
    else:
        print(f'Nenhuma tarefa cadastrada como {nome} foi encontrada.')
        voltar()

def alt_estado_tarefa():
    alterar = input('Digite o nome da tarefa que você deseja concluir: ')
    for coisa in tarefas:
        if alterar.lower() == coisa['nome'].lower():
            if coisa['Status'] == 'Não concluída.':
                coisa['Status'] = 'Concluída.'
                print(f'Tarefa {coisa['nome']} alterada para Concluída')
                salvar_tarefas()
                voltar()
            else:
                coisa['Status'] = 'Não Concluída.'
                print(f'Tarefa {coisa['nome']} alterada para Não Concluída')
                salvar_tarefas()
                voltar()
                break
        else:
            print(f'A Tarefa {alterar} não está cadastrada no sistema.')
            voltar()

def listar_tarefas():
    if not tarefas:
        print('Sem tarefas cadastradas.\n')
        voltar()
    else:
        print('\nTarefas cadastradas:')
        for tarefa in tarefas:
            for chave, valor in tarefa.items():
                print(f'{chave}: {valor}')
            print('')
        voltar()

def pedir_data(tipo):
    while True:
        prazo = input(f'\nDigite um {tipo}: ')
        if validar_data(prazo, tipo):
            return prazo

def validar_data(data_tarefa, tipo):
    if data_tarefa == '':
        print(f'Sem {tipo} definido.')
        return True
    elif len(data_tarefa) == 10 and data_tarefa[4] == '-' and data_tarefa[7] == '-':
        try:
            ano, mes, dia = data_tarefa.split('-')
            print(f'1-{ano}, 2-{mes}, 3-{dia}')
            return True
        except ValueError:
            print('Formato inválido de data.\n')
            return False
    else:
        print('Formato inválido de data\n')
        return False

def salvar_tarefas():
    with open('tarefas.json', 'w', encoding='utf-8') as LDT:
        json.dump(tarefas, LDT, indent=4, ensure_ascii=False)

def voltar():
    input('Aperte ENTER para voltar ao menu principal. ')
    limpar_tela()

def limpar_tela():
    print("\n" * 100)

if __name__ == "__main__":
    main()