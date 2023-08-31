# -*- coding: utf-8 -*-

# YOUR FULL NAME
# UAG00098
# Problem Set 4 - Problem 5
# Description:

"""
Inputs, Processes and Output (IPO)
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
Nas questões desse desse conjunto, você deverá escrever uma biblioteca chamada library_problem_5.py que contenha funções, separando a lógica do script principal, onde serão chamadas todas as funções.

Input(s):
A entrada contém vários casos de teste. A primeira linha da entrada contém um inteiro N (1 ≤ N ≤ 100), indicando o número de casos de teste da entrada. Cada uma das N linhas seguintes contém um valor inteiro X (1 < X ≤ 107), que pode ser ou não, um número primo.

Processes:
Na matemática, um Número Primo é aquele que pode ser dividido somente por 1 (um) e por ele mesmo. Por exemplo, o número 7 é primo, pois pode ser dividido apenas pelo número 1 e pelo número 7.

Output(s):
Para cada caso de teste de entrada, imprima a mensagem “X é primo” ou “X não é primo”, de acordo com a especificação fornecida.

Exemplo 1:
Digite quantos testes realizará: 3
Teste 1: 8
8 não é primo.
Teste 2: 51
51 não é primo.
Teste 3: 7
7 é primo.
"""


def main():
    def main():
    def e_primo(num):
  """
    Verifica se um número é primo ou não.
    :param num: o número a ser verificado
    :return: True se o número for primo, False caso contrário
    """
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


def teste():
    n = int(input("Digite quantos testes realizará: "))
    for i in range(1, n+1):
        x = int(input("Teste {}: ".format(i)))
        if e_primo(x):
            print("{} é primo.".format(x))
        else:
            print("{} não é primo.".format(x))


if __name__ == '__main__':
    main()


