#!/usr/bin/python
# -*- coding: utf-8 -*
"""
Exempo tirado do seguinte site
Fonte: http://alissonmachado.com.br/python-threads/
Autor Inicial: Alisson Machado

Modificado por: Koheleth(Aurélio)
Foi acrescentado mais uma Thread seguindo esse exemplo pode ser acrescentado outras

"""
import threading
import time


def main():

    # Instanciando a Thread t1
    # aqui ela vem com argumento em tupla, mas não é obrigatório
    t1 = threading.Thread(target=primeira_thread, args=('thread sendo executada',))
    # iniciando a Thread t1
    # a partir daqui ela começa a rodar em paralelo
    t1.start()

    # Instanciando a Thread t2
    # aqui temos um exemplo de thread sem argumentos
    t2 = threading.Thread(target=segunda_thread)
    # iniciando a t2 em paralelo também
    t2.start()

    # Temos um laço que entenda como fosse a Thread principal
    # Só para o laço quando as duas thread terminarem
    while t1.isAlive() or t2.isAlive():
        print(f'(3) - corpo principal')
        time.sleep(2)

    # quando termina o laço sinalizamos o termino das três threads
    print("Thread morreu")
    print("Finalizando o programa")


def segunda_thread():
    for i in range(10):
        print(f'(2) - Segunda função')
        time.sleep(3)


def primeira_thread(mensagem='Executando...'):
    for i in range(10):
        print(f'(1) - {mensagem} primeira funçao')
        time.sleep(1)


if __name__ == '__main__':
    main()
