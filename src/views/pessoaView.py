from ..controllers.pessoa_controller import PessoaController
from ..models.pessoa import Pessoa

"""
    View responsável por adicionar, remover, atualizar e listar pesssoas.
"""

def adicionarPessoa():
    cpf = input("Digite o cpf da pessoa:")
    if (verificaCPF(cpf) == 1):
        print('CPF informado já cadastrado!')
    else:
        nome = input("Digite o nome da pessoa:")
        sobrenome = input("Digite o sobrenome da pessoa:")
        data_de_nascimento = input("Digite a data de nascimento da pessoa:")

        nova_pessoa = Pessoa(nome = nome,sobrenome = sobrenome, cpf = cpf, data_de_nascimento = data_de_nascimento )
        PessoaController.salvar_pessoa(nova_pessoa)
        print(' ----  Cadastro realizado com sucesso! ----')

def buscarPessoa():
    cpf = input('Digite o CPF da pessoa: ')
    for i in PessoaController.listar_pessoas():
        if (i.cpf == cpf):
            return print(f' Nome: {i.nome} \n Sobrenome: {i.sobrenome} \n CPF: {i.cpf} \n Data de Nascimento: {i.data_de_nascimento}')
        else:
            return print('CPF da pessoa informada não possui cadastro.')

def listarPessoas():
    for i in PessoaController.listar_pessoas():
        print(' ------------------------ ')
        print(f' Nome: {i.nome} \n Sobrenome: {i.sobrenome} \n CPF: {i.cpf} \n Data de Nascimento: {i.data_de_nascimento}')

def verificaCPF(cpf):
    for i in PessoaController.listar_pessoas():
        if (i.cpf == cpf):
            return 1
        else:
            return 0
