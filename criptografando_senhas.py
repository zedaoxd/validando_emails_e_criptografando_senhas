from passlib.hash import pbkdf2_sha256 as cryp
import re
from colorama import Fore


def menu():
    while True:
        print(Fore.CYAN + '-=' * 20)
        email = input(Fore.YELLOW + 'Digite o e-mail: ')
        senha = input('Digite sua senha: ')
        print(Fore.CYAN + '-=' * 20)

        checa(email, senha)

        print('Sair ou continuar:')
        sair = input('[Y] para sair ou [N] para continuar: ')
        if sair.upper() == 'Y':
            break


def checa(email, senha):
    # Começando as checagens
    pessoa1 = Pessoa(email, senha)

    # Checando o email
    print(pessoa1.verifica_email())

    # Mostrando a senha e a senha criptografada
    print(f'Senha: {senha}')
    print(f'Senha criptografada: {pessoa1.mostra_senha()}')


class Pessoa:

    def __init__(self, email, senha):
        self.__email = email
        self.__senha = cryp.hash(senha, rounds=200_000, salt_size=16)

    def verifica_email(self):
        r = re.compile(r'^[\w-]+@(?:[a-zA-Z0-9-]+\.)+[a-zA-Z]{2,}$')
        if r.match(self.__email) is None:
            return 'E-mail inválido!'
        return 'E-mail válido!'

    def mostra_senha(self):
        return self.__senha


menu()
