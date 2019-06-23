#!/usr/bin/python
# -*- coding: utf-8 -*
"""
Exemplo tirado do site:
http://recologia.com.br/2015/07/programacao-multi-thread-em-python/
Autor original: Augusto Ribas

Modificado por: Koheleth(Aurélio)
Esse exemplo me chamou atenção por usar classes com thread
Fiz a adaptação e correções de python 2.7 para python 3.6

"""
import threading


def processo(nome, contador):
    while contador:
        print(f'Thread {nome} fazendo o processo {contador}')
        contador -= 1


# Herda da threading.Thread essa classe Thread
class minhaThread(threading.Thread):
    # construtor da classe  com parametros o principal é o threaredID
    def __init__(self, threadID, nome, contador):
        # chama o construtor da classe pai
        threading.Thread.__init__(self)
        # preenchimento das variáveis com os parâmetros
        self.threadID = threadID
        self.nome = nome
        self.contador = contador

    # uma das funções mais importantes run()
    # é uma sobrecarga da função run() da classe pai é nela que
    # colocamos as rotinas para executar nossas Threads
    def run(self):
        print(f'Iniciando Thread {self.nome} com {self.contador} processos')
        # foi escolhida uma função externa para ser executada pela thread
        processo(self.nome, self.contador)
        print(f'Finalizando {self.nome}')


def main():
    # Instanciando as classes em objetos Threads
    t1 = minhaThread(1, "Marcos", 10)
    t2 = minhaThread(2, "Aurelio", 10)
    t1.start()
    t2.start()
    # Criando uma lista com as saidas das threads
    threads = [t1, t2]
    # Mostrando a saida das threads que está na lista
    for t in threads:
        t.join()


if __name__ == '__main__':
    main()
